def is_prime(a):
    if a > 1:
        for i in range(2, a - 1):
            if a % i == 0:
                return 0
        return 1
    else:
        return 0


print(bool(is_prime(7)))

