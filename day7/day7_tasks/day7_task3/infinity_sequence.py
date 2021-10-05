# Generating an Infinite Sequence

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

if __name__ == "__main__":
    for i in infinite_sequence():
        print(i, end=" ")