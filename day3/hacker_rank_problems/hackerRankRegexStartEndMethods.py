# HackerRank Problem about Re.start() & Re.end(). Link: https://www.hackerrank.com/challenges/re-start-re-end/problem

# start() & end() These expressions return the indices of the start and end of the substring matched by the group.
import re
m = re.search(r'\d+','ab1234sds')
print(f"Result of start(): {m.start()}\nResult of end(): {m.end()}")

# Solution of the problem.
S = input()
k = input()
import re
pattern = re.compile(k)
r = pattern.search(S)
if not r:
    print((-1, -1))
while r:
    print("({0}, {1})".format(r.start(), r.end() - 1))
    r = pattern.search(S,r.start() + 1)