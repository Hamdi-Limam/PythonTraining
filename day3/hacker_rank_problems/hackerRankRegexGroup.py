# Hacker Rank for Regex Groups. Link: https://www.hackerrank.com/challenges/re-group-groups/problem

# Importing Regex module
import re
# \1 is backreference to group #1, matches the result of capture group 1
m = re.search(r'([a-zA-Z0-9])\1', input().strip())

# m.group(0) -> The entire match 
# m.group(1) -> The first parenthesized subgroup.
print(m.group(1) if m else -1)