# /// script
# requires-python = ">=3.9"
# dependencies = ["ecdsa"]
# ///
#
# Generates ECDSA secp256k1 inputs for the Noir signature circuit.
# Usage:
#   uv run generate_inputs.py              → writes Prover.toml
#   uv run generate_inputs.py --test       → also prints Noir byte-array literals for inline tests

import hashlib
import sys
from pathlib import Path

from ecdsa import SECP256k1, SigningKey
from ecdsa.util import sigencode_string, sigdecode_string

# Deterministic private key (for learning only — never reuse in production)
private_key_bytes = hashlib.sha256(b"zk-from-zero-test-key").digest()
sk = SigningKey.from_string(private_key_bytes, curve=SECP256k1)
vk = sk.get_verifying_key()

pub_key_x = vk.to_string()[:32]
pub_key_y = vk.to_string()[32:]

# Message hash (this is what Noir's verify_signature expects directly)
message = b"zk-from-zero signature test"
hashed_message = hashlib.sha256(message).digest()

# sign_digest_deterministic uses pure RFC 6979 (no extra random entropy),
# so the same key + message always produces the same signature.
signature = sk.sign_digest_deterministic(
    hashed_message, sigencode=sigencode_string, extra_entropy=b""
)

# Normalize s to low-s form (BIP-62) — required by Noir's verify_signature
ORDER = SECP256k1.order
r_bytes = signature[:32]
s_int = int.from_bytes(signature[32:], "big")
if s_int > ORDER // 2:
    s_int = ORDER - s_int
s_bytes = s_int.to_bytes(32, "big")
signature = r_bytes + s_bytes

# Verify locally
vk.verify_digest(signature, hashed_message, sigdecode=sigdecode_string)
print("Local verification OK", file=sys.stderr)


def to_hex_list(buf: bytes) -> str:
    return ", ".join(f"0x{b:02x}" for b in buf)


def to_noir_literal(buf: bytes, per_line: int = 8) -> str:
    hexes = [f"0x{b:02x}" for b in buf]
    lines = []
    for i in range(0, len(hexes), per_line):
        lines.append("        " + ", ".join(hexes[i : i + per_line]) + ",")
    return "\n".join(lines)


# Always write Prover.toml
toml = f"""pub_key_x = [{to_hex_list(pub_key_x)}]
pub_key_y = [{to_hex_list(pub_key_y)}]
signature = [{to_hex_list(signature)}]
hashed_message = [{to_hex_list(hashed_message)}]
"""
out = Path(__file__).parent / "Prover.toml"
out.write_text(toml)
print(f"Wrote {out}")
print(f"  pub_key_x: {pub_key_x.hex()}")
print(f"  pub_key_y: {pub_key_y.hex()}")
print(f"  msg_hash:  {hashed_message.hex()}")
print(f"  sig_r:     {r_bytes.hex()}")
print(f"  sig_s:     {s_bytes.hex()}")

if "--test" in sys.argv:
    print("\n// Paste these into your #[test] function:\n")
    print(f"    let pub_key_x: [u8; 32] = [\n{to_noir_literal(pub_key_x)}\n    ];")
    print(f"    let pub_key_y: [u8; 32] = [\n{to_noir_literal(pub_key_y)}\n    ];")
    print(f"    let signature: [u8; 64] = [\n{to_noir_literal(signature)}\n    ];")
    print(f"    let hashed_message: [u8; 32] = [\n{to_noir_literal(hashed_message)}\n    ];")
