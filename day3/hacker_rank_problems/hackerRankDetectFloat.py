# HackerRank problem about detecting Float numbers. Link:https://www.hackerrank.com/challenges/introduction-to-regex/problem
import re

for _ in range(int(input())):
    print(bool(re.search(r"^(?:[.]\d+)?(?:(\+|-).\d+)?(?:(\+|-)\d+\.{1}\d+)?(?:\d+\.{1}\d+)?$", input())))