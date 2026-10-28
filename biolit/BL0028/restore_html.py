#!/usr/bin/env python3
"""Recreate the byte-identical accepted self-contained HTML using stdlib only."""
from pathlib import Path
import argparse, base64, hashlib, json

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('output',type=Path,help='New output file; existing files are never overwritten')
a=p.parse_args();root=Path(__file__).resolve().parent
m=json.loads((root/'html-assets.json').read_text())
sha=lambda b:hashlib.sha256(b).hexdigest()
data=(root/'deck.html').read_bytes()
assert sha(data)==m['external_html_sha256'],'External HTML checksum mismatch'
for row in m['assets']:
 path=Path(row['path']);assert not path.is_absolute() and '..' not in path.parts
 image=(root/path).read_bytes()
 assert len(image)==row['bytes'] and sha(image)==row['sha256'],f'Asset checksum mismatch: {path}'
 uri=('data:'+row['mime']+';base64,').encode()+base64.b64encode(image)
 data=data.replace(row['path'].encode(),uri)
assert len(data)==m['original_html_bytes'] and sha(data)==m['original_html_sha256'],'Rebuilt HTML checksum mismatch'
with a.output.open('xb') as f:f.write(data)
print(f'Restored {len(data)} bytes; SHA-256 {sha(data)}')
