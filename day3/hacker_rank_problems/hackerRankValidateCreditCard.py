# HackerRank problem for validating credit card number. Link: https://www.hackerrank.com/challenges/validating-credit-card-number/problem

import re
n = int(input())
lines = []
for _ in range(n):
    lines.append(input())

digits_pattern = re.compile(r"^[456]\d{15}$|^[456](\d{3}-)(\d{4}-){2}\d{4}$")

for i in lines:
    verify_repeat = re.search(r"(\d)-*?\1-*?\1-*?\1", i, re.I)
    print("Valid" if verify_repeat == None and digits_pattern.search(i) else "Invalid")