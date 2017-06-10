# Problem 3: Largest prime factor


def is_prime(n):
    if n == 2:
        return True
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
        return True


def add_prime(highest_prime):
    loop = True
    highest_prime += 1
    while loop:
        if is_prime(highest_prime) != True:
            highest_prime += 1
            break
        break
    print(highest_prime)
    return highest_prime


def find_largest_in_list(prime_list):
    highest = 0
    for prime in prime_list:
        if prime > highest:
            highest = prime
    return highest


def prime_loop(dividend):
    highest_prime = 0
    prime_list = []
    factorization = []
    while True:
        if dividend == 1:
            break
        highest_prime = add_prime(highest_prime)
        prime_list.append(highest_prime)
        for prime in prime_list:
            if dividend % prime == 0:
                dividend /= prime
                print("dividend", )
                print(dividend)
                factorization.append(prime)
                break
    result = find_largest_in_list(prime_list)
    return result

print(prime_loop(600851475143))
