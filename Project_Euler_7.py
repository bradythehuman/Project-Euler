# Problem 7: 10001st prime

# What is the 10001st prime number?


def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5 + 1), 2):
        if n % i == 0:
            return False
    return True


def find_prime(prime_num):
    test_num = 0
    while prime_num > 0:
        test_num += 1
        if is_prime(test_num):
            print(test_num)
            prime_num -= 1
    return test_num

find_prime(10001)
