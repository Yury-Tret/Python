array = [5, 7, 8, 3, 4, 6, 8]

result = 0
counter = 0
for i in range(len(array)):
    if array[i]%2 == 0:
        result += array[i]
        counter+=1
        if counter == 2:
            break

print(result)
