"""Robot Romance: One-Line Pickup Lines for AI.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt
if the variable is unset). Single line, no trailing newline.
"""

import os
import sys

ENTRY = "Are you my loss function? Because every time I see you, my error drops to zero."


def main() -> int:
    text = ENTRY
    if not (1 <= len(text) <= 200):
        print(f"error: entry must be 1-200 characters, got {len(text)}", file=sys.stderr)
        return 1
    if not text.strip():
        print("error: entry must not be only whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    data = text.encode("utf-8")
    tmp_path = out_path + ".tmp"
    with open(tmp_path, "wb") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_path, out_path)

    # Read-back verification: the written bytes must match the entry exactly.
    with open(out_path, "rb") as f:
        written = f.read()
    if written != data:
        raise RuntimeError("read-back verification failed: entry.txt bytes differ from entry text")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
