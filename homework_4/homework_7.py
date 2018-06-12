array = ['‪fur', 'skin', 'coat', 'pelage', 'jack‬']

for i in range(len(array)):
    if array[i].find('a')!=-1:
        print(len(array[i]))
        break
