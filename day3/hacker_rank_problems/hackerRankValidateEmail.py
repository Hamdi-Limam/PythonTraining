# HackerRank problem for validating and parsing email addressess. Link: https://www.hackerrank.com/challenges/validating-named-email-addresses/problem
# Docs for email.utils. Link: https://docs.python.org/3/library/email.utils.html

import re

for _ in range(int(input())):
    name, email = tuple((input().split(" ")))
    if bool(re.search(r"^<[A-Za-z][A-Za-z0-9-._]+@[A-Za-z]+\.[a-z]{1,3}>$", email)):
        print(f"{name} {email}")
