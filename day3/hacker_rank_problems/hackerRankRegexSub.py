# HackerRank problem about Regex substitution. Link: https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem

# The re.sub() tool (sub stands for substitution) evaluates a pattern and, for each valid match, it calls a method (or lambda).
# The method is called for all matches and can be used to modify strings in different ways.
# The re.sub() method returns the modified string as an output.
# Example:
import re
#Squaring numbers
def square(match):
    number = int(match.group(0))
    return str(number**2)

print(re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9"))

# Solution for the problem
import re
n = int(input())
k = input()
for _ in range(n-1):
   k = f"{k}\n{input()}"

k = re.sub('(?<=\s)(\|{2})(?=\s)', 'or', k)
print(re.sub('(?<=\s)(&{2})(?=\s)', 'and', k))

# Shorter solution
# import re
# print('\n'.join(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group()=='&&' else 'or', input()) for _ in range(int(input().strip()))))