# HackerRank problme for validating UID. Link: https://www.hackerrank.com/challenges/validating-uid/problem
import re
n = int(input())
lines = []
for _ in range(n):
    lines.append(input())

uppercase_pattern = re.compile("^(.*?[A-Z].*?){2,}$")
digits_pattern = re.compile("^(.*?[\d].*?){3,}$")
for i in lines:
    verify_repeat = re.findall(r"[\dA-Z]", i, re.I)
    alphanumeric_verify = re.findall(r"[^\dA-Z]", i, re.I)
    print("Valid" if len(i) == 10 and len(verify_repeat) == len(set(verify_repeat)) and uppercase_pattern.search(i) and digits_pattern.search(i) and len(alphanumeric_verify) == 0 else "Invalid")