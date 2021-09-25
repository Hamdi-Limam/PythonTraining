# HackerRank problem about finding number of times that the substring occurs in the given string . Link: https://www.hackerrank.com/challenges/find-a-string/problem

string, substring = (input().strip(), input().strip())
print(sum([ 1 for i in range(len(string)-len(substring)+1) if string[i:i+len(substring)] == substring]))
