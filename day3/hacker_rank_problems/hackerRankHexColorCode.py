# HackerRank problem about detecting Hex color code. Link: https://www.hackerrank.com/challenges/hex-color-code/problem

import re
lines = []
for _ in range(int(input())):
   lines.append(input())

for match in re.finditer(r'(#([\dA-F]{3}){1,2})(?=[;,)])', '\n'.join(lines), flags=re.IGNORECASE):
    print(match.group(0))
