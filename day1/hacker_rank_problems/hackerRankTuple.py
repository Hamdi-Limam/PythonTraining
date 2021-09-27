# HackerRank problem about tuples. Link: https://www.hackerrank.com/challenges/python-tuples/problem

if __name__ == '__main__':
    n = int(input())
    print(hash(tuple(map(int, input().split()))))


