# Problem 5: Smallest Multiple

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

number = 2
loop = True
while loop:
    print(number)
    divisible = True
    for x in range(1, 21):
        if number % x == 0:
            pass
        else:
            divisible = False
    if divisible:
        print("Smallest multiple found")
        print(number)
        loop = False
    number += 2
