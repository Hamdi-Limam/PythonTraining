# HackerRank problem for Regex split function. Link: https://www.hackerrank.com/challenges/re-split/problem
import re

regex_pattern = r"[.,]" # means it matches any character in the set (, .)
regex_pattern_two = r"\D" # means it matches any character that's not a digit

print("\n".join(re.split(regex_pattern, input())))
print("\n".join(re.split(regex_pattern_two, input())))