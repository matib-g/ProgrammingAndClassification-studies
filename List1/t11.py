list1 = []

while True:
    try:
        a = int(
            input('Type an list of integer numbers (or some other character to break): '))
    except ValueError:
        break
    else:
        list1.append(a)

    for j in range(len(list1)):
        if list1[j] < 0:
            list1.pop(j)

print(list1)
