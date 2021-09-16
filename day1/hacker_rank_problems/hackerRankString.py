def split_and_join(line):
    line = line.split(" ")
    return "-".join(line)

if __name__ == '__main__':
    line = input("Enter a string: ")
    result = split_and_join(line)
    print(result)