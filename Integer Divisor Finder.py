n = int(input("Enter an integer: "))
divisors = []
for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)
print(f"Divisors of {n}: {divisors}")
print(f"Number of divisors found: {len(divisors)}")
