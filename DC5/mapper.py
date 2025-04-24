# Mapper Code
import sys
for line in sys.stdin:
    line = line.strip()
    if line.startswith("dt"):
        continue
    parts = line.split(",")
    if len(parts) != 7:
        continue
    date = parts[0]
    year = date.split("-")[0]
    try:
        temperature = float(parts[1])
        print(f"{year}\t{temperature}")
    except ValueError:
        continue