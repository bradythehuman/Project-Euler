# Problem 1: Multiples of 3 and 5

num = 1
multiples = []

while num < 1000:
    if num % 3 == 0 or num % 5 == 0:
        multiples.append(num)
    num += 1

total = 0
i = 0

while i < len(multiples):
    total += multiples[i]
    i += 1

print(multiples)
print(total)
