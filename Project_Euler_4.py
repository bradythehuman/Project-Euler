# Problem 4: Largest palindrome product

# Find the largest palindrome made from the product of two 3-digit numbers.

palindromes = []
lrg_pal = 0

for x in range(100,1000):
    for y in range(100, 1000):
        result = str(x * y)
        if result == result[0::-1]:
            palindromes.append(int(result))

for pal in palindromes:
    if pal > lrg_pal:
        lrg_pal = pal

print(lrg_pal)