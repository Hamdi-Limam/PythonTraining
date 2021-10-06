# Detecting inifinity Palindromes with generators

def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return True
    else:
        return False

def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)
            if i is not None:
                num = i
        num += 1

if __name__ == "__main__":
    pal_gen = infinite_palindromes()
    for i in pal_gen:
        digits = len(str(i))
        pal_gen.send(10 ** (digits))
        