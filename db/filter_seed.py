import re
import sys

KEEP_COLS = {
    "Botanical Name", "Common Name", "Attracts Wildlife", "Flower Color",
    "Flowering Season", "Sun", "Water Requirement", "Companions",
    "Communities", "Tips", "Pests", "Plant Url"
}

def parse_values(values_str):
    values = []
    current = ""
    in_string = False
    i = 0
    while i < len(values_str):
        ch = values_str[i]
        if in_string:
            if ch == "'" and i + 1 < len(values_str) and values_str[i + 1] == "'":
                current += "''"
                i += 2
                continue
            elif ch == "'":
                current += ch
                in_string = False
            else:
                current += ch
        else:
            if ch == "'":
                current += ch
                in_string = True
            elif ch == ",":
                values.append(current.strip())
                current = ""
            else:
                current += ch
        i += 1
    if current.strip():
        values.append(current.strip())
    return values

input_path = "/home/andre/Documents/code/flower/db/seed.sql"
output_path = "/home/andre/Documents/code/flower/db/seed_filtered.sql"

SEPARATOR = ") VALUES ("
PREFIX = "INSERT INTO public.flowers ("

out_lines = []
skipped = 0

with open(input_path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line.startswith(PREFIX):
            continue

        idx = line.find(SEPARATOR)
        if idx == -1:
            skipped += 1
            continue

        cols_part = line[len(PREFIX):idx]
        vals_part = line[idx + len(SEPARATOR):]
        if vals_part.endswith(");"):
            vals_part = vals_part[:-2]

        cols = re.findall(r'"([^"]+)"', cols_part)
        vals = parse_values(vals_part)

        if len(cols) != len(vals):
            print(f"WARNING: {len(cols)} cols vs {len(vals)} vals — skipping", file=sys.stderr)
            skipped += 1
            continue

        pairs = [(c, v) for c, v in zip(cols, vals) if c in KEEP_COLS]
        kept_cols = ", ".join(f'"{c}"' for c, _ in pairs)
        kept_vals = ", ".join(v for _, v in pairs)
        out_lines.append(f'INSERT INTO public.flowers ({kept_cols}) VALUES ({kept_vals});\n')

with open(output_path, "w", encoding="utf-8") as f:
    f.writelines(out_lines)

print(f"Done: {len(out_lines)} rows written, {skipped} skipped → {output_path}")
