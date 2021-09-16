# HackerRank problem for Regex find methods. Link: https://www.hackerrank.com/challenges/re-findall-re-finditer/problem

import re
# The expression re.findall() returns all the non overlapping matches of patterns in a string as a list of strings.
print("Result of re.findall: ", re.findall(r'\w','http://www.hackerrank.com/'))

# The expression re.finditer() returns an iterator yielding MatchObject instances over all non-overlapping matches for the re pattern in the string.
m = re.finditer(r'\w','http://www.hackerrank.com/')
print("Result of re.finditer: ", m)
items = list(m)
print([items[i].group() for i in range(len(items))])

# Task: You are given a string . It consists of alphanumeric characters, spaces and symbols(+,-).
# Your task is to find all the substrings of  that contains  or more vowels.
# Also, these substrings must lie in between  consonants and should contain vowels only.
import re 
result = re.findall(r"([AEIOU]{2,})(?=[^/s+-AEIOU])" ,input(), re.I) 
print("\n".join(result) if len(result) > 0 else "-1")