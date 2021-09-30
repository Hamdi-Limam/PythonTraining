# print prime numbers from 0 to 10000 in python

def find_prime_numbers():
    primes = [2]
    for i in range(3, 10001):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes


if __name__ == "__main__":
    print(find_prime_numbers())

# Using List comprehension
# print([i for i in range(2, 101) if all(i % m != 0 for m in range(2, i))])
