
# Iterate Forever
class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value

if __name__ == "__main__":
    repeater = Repeater("Hello")

    for i in repeater:
        print(i)
