from pathlib import Path
import base64, hashlib, re
root = Path(__file__).resolve().parent
parts = []
for n in (1, 2):
    text = (root / f"assets/display_A_4_bytes_{n}.js").read_text()
    match = re.fullmatch(r'window.AL0015_A4_BYTES_\d="([A-Za-z0-9+/=]+)";\s*', text)
    if not match:
        raise ValueError(f"Invalid shard {n}")
    parts.append(base64.b64decode(match.group(1), validate=True))
data = b"".join(parts)
expected = "0dfd208aaa19c8a5f7c23cd399f45c487b131cac5c531d510190e3c65220c00d"
assert hashlib.sha256(data).hexdigest() == expected, "Original SHA256 mismatch"
output = root / "restored_display_A_4.png"
output.write_bytes(data)
print(output, len(data), expected)
