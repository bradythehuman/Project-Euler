# Problem 2: Even Fibonacci Numbers

fib = []
term_minus_2 = 0
term_minus_1 = 1
loop_index = 0

while True:
    current_term = term_minus_2 + term_minus_1
    if current_term <= 4000000:
        fib.append(current_term)
    else:
        break
    term_minus_2 = term_minus_1
    term_minus_1 = current_term
    loop_index += 1

total = 0

for num in fib:
    if num % 2 == 0:
        total += num

print(total)
