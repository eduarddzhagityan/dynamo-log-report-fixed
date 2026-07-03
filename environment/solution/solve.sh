#!/bin/bash

python3 <<'PY'
import json
import re
from collections import Counter

ips = set()
paths = []
total = 0

with open("/app/access.log") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        total += 1
        ips.add(line.split()[0])
        m = re.search(r'"[A-Z]+ ([^ ]+)', line)
        if m:
            paths.append(m.group(1))

report = {
    "total_requests": total,
    "unique_ips": len(ips),
    "top_path": Counter(paths).most_common(1)[0][0]
}

with open("/app/report.json", "w") as out:
    json.dump(report, out, indent=2)
PY
