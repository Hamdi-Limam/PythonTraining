# HackerRank problem about loops. Link: https://www.hackerrank.com/challenges/python-loops/problem
if __name__ == '__main__':
    n = int(input("Please enter the array size, must be between 1 and 20: "))
    while n < 1 or n > 20:
        n = int(input("Please enter the array size, must be between 1 and 20: "))
    for i in range(n):
        print(i*i)