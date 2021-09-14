# HackerRank problem for Validating Roman Numerals. Link: https://www.hackerrank.com/challenges/validate-a-roman-number/problem

# Import Regex module
import re

def verify_roman_num(roman_num):
    thousand = 'M{0,3}' # M between 0 & 3
    # ? zero or one
    hundred = '(C[MD]|D?C{0,3})' # 400 OR 900 | 100-300 OR 500-800 
    ten = '(X[CL]|L?X{0,3})'
    digit = '(I[VX]|V?I{0,3})'
    print(bool(re.match("^"+ thousand + hundred+ ten + digit +'$', roman_num)))

verify_roman_num(input("Enter a Roman number: "))