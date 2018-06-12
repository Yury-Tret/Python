def count_digits(a):
    counter = 1
    while True:
        a = a // 10
        if a > 0 or a < -1:
            counter+=1
        else:
            return counter

print(count_digits(-342))

