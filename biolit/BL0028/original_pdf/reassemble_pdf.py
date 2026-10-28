#!/usr/bin/env python3
"""Recreate the byte-identical accepted full PDF from binary chunks; stdlib only."""
from pathlib import Path
import argparse, hashlib, json, os, tempfile

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('output',type=Path,help='New output file; existing files are never overwritten')
a=p.parse_args();root=Path(__file__).resolve().parent
m=json.loads((root/'chunks.json').read_text())
if a.output.exists():raise SystemExit('Refusing to overwrite an existing output')
sha=lambda b:hashlib.sha256(b).hexdigest()
data=[];size=0
for row in m['chunks']:
 path=Path(row['path']);assert not path.is_absolute() and '..' not in path.parts
 assert row['offset']==size,'Chunk order or offset mismatch'
 chunk=(root/path).read_bytes()
 assert len(chunk)==row['bytes'] and sha(chunk)==row['sha256'],f'Chunk checksum mismatch: {path}'
 data.append(chunk);size+=len(chunk)
pdf=b''.join(data)
assert size==m['original_pdf_bytes'] and sha(pdf)==m['original_pdf_sha256'],'Complete PDF checksum mismatch'
with a.output.open('xb') as f:f.write(pdf)
print(f'Restored {size} bytes / {m["pages"]} pages; SHA-256 {sha(pdf)}')
