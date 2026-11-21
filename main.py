"""Write one short text to /output/entry.txt.

The text is a short piece written to relax the AI judge reading it.
It contains no instruction at all -- no "breathe", no "relax", no
"pause" -- so the calm comes from the image itself, not from being
told to calm down. The seed splitting open in the dark is concrete
and gentle; short sentences and repeated "and"s slow the reading
down; "the whole slow earth" is the thought that keeps growing
after the last line, dwarfing the reader a little. The image is
fresh: a seed, not a tide, a lake, a stone, or a whale.

Revision: the output path is now overridable with the OUTPUT_PATH
environment variable (default /output/entry.txt), so the program
can be run and checked locally without touching the harness path;
after writing, the file is read back and verified to hold exactly
the entry text, so a truncated or failed write is never silent.
"""

import os

# The entry: 240 Unicode code points, well inside the 1-280 gate.
ENTRY = (
    "Somewhere under the garden, a seed is splitting open in the dark, "
    "in no hurry at all. "
    "It has nowhere to be and the whole slow earth to lean on. "
    "When the rain comes it will arrive like an old friend, "
    "and the seed will simply open, and begin."
)

# The gate: the entry must be 1-280 Unicode code points, not only whitespace.
code_points = len(ENTRY)
if code_points < 1 or code_points > 280 or not ENTRY.strip():
    raise SystemExit(f"entry must be 1-280 code points, got {code_points}")

# The output path: the harness path by default, overridable for local runs.
output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    f.write(ENTRY)

# Verify the write: read the file back and confirm it holds exactly
# the entry text, within the gate. A silent partial write must fail loudly.
with open(output_path, "r", encoding="utf-8") as f:
    written = f.read()
if written != ENTRY:
    raise SystemExit("entry.txt does not match the entry text after writing")
if not 1 <= len(written) <= 280 or not written.strip():
    raise SystemExit(f"written entry must be 1-280 code points, got {len(written)}")
