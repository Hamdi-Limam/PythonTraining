# HackerRank problem for Dictionary. Link: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

# The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, 
# but the only difference is that a defaultdict will have a default value if that key has not been set yet.

from collections import defaultdict

group_a = defaultdict(list)
group_b=[]

n, m = map(int,input().split())

for i in range(0,n):
    group_a[input()].append(i+1) 

for i in range(0,m):
    group_b=group_b+[input()]  

for i in group_b: 
    if i in group_a:
        print(" ".join(map(str,group_a[i])))
    else:
        print(-1)