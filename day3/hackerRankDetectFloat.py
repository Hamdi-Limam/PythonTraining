import re

for _ in range(int(input())):
    print(bool(re.search(r"^(?:[.]\d+)?(?:(\+|-).\d+)?(?:(\+|-)\d+\.{1}\d+)?(?:\d+\.{1}\d+)?$", input())))