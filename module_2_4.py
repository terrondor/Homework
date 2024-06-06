numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
numbers.remove(1)
for i in numbers:
    if i == 2:
        primes.append(i)
    else:
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                not_primes.append(i)
                is_prime = False
                break
        if is_prime:
            primes.append(i)

print('Primes: ', primes)
print('Not Primes: ', not_primes)