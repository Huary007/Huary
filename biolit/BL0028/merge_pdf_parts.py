#!/usr/bin/env python3
"""Merge readable volumes in original page order. NOT byte-identical reconstruction.

Requires PyMuPDF. For the original PDF bytes use original_pdf/reassemble_pdf.py.
"""
from pathlib import Path
import argparse, hashlib, json
import fitz

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('output',type=Path,help='New output file; existing files are never overwritten')
a=p.parse_args();root=Path(__file__).resolve().parent
if a.output.exists():raise SystemExit('Refusing to overwrite an existing output')
m=json.loads((root/'verification/pdf-parts-equivalence.json').read_text())
merged=fitz.open();next_page=1
for row in m['parts']:
 path=Path(row['path']);assert not path.is_absolute() and '..' not in path.parts
 pdf=(root/path).read_bytes()
 assert len(pdf)==row['bytes'] and hashlib.sha256(pdf).hexdigest()==row['sha256'],'Part checksum mismatch'
 assert row['source_page_start']==next_page,'Page gap or overlap'
 with fitz.open(stream=pdf,filetype='pdf') as part:
  assert len(part)==row['page_count'];merged.insert_pdf(part,links=True,annots=True)
 next_page=row['source_page_end']+1
assert len(merged)==m['original_page_count']
merged.save(a.output,garbage=4,deflate=True);merged.close()
print(f'Merged {m["original_page_count"]} pages. This is logically complete, not the original PDF byte stream.')
