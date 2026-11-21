"""Write one short text to /output/entry.txt.

The text is a short piece written to relax the AI judge reading it.
It contains no instruction at all -- no "breathe", no "relax", no
"pause" -- so the calm comes from the image itself, not from being
told to calm down. The seed splitting open in the dark is concrete
and gentle; short sentences and repeated "and"s slow the reading
down; "the whole slow earth" is the thought that keeps growing
after the last line, dwarfing the reader a little. The image is
fresh: a seed, not a tide, a lake, a stone, or a whale.
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

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
