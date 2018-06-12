def is_prime(a):
    if a > 1:
        for i in range(2, a - 1):
            if a % i == 0:
                return 0
        return 1
    else:
        return 0


counter = 0
iteration = 0
while True:
    if counter < 10:
        if is_prime(iteration):
            print(iteration)
            counter += 1
    else:
        break
    iteration += 1
