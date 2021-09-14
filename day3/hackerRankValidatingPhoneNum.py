# HackerRank Problem for Validating phone numbers. Link: https://www.hackerrank.com/challenges/validating-the-phone-number/problem
# A valid mobile number is a ten digit number starting with a  or .

# Importing Regex
import re

def verify_phone_num(phone_num):
    return "YES" if bool(re.match(r'[789]\d{9}$', phone_num)) else "NO"


N = int(input("Enter number of inputs: "))
while N<1 or N > 10:
    N = input("Enter number of inputs: ")

phone_numbers = [input() for _ in range(N)]

for i in range(len(phone_numbers)):
    print(verify_phone_num(phone_numbers[i]))


# Short solution
M = int(input())

for _ in range(M):
    print("YES" if bool(re.match(r'[789]\d{9}$', input())) else "NO")