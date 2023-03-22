list1 = []
list2 = []
commons = []


while True:
    a = input('Type an element to list x (or "ExList" to exit): ')
    if a == "ExList":
        break
    else:
        list1.append(a)
        print(list1)

while True:
    b = input('Type an element to list y (or "ExList" to exit): ')
    if b == "ExList":
        break
    else:
        list2.append(b)
        print(list2)

for i in range(0, len(list1)):
    for j in range(0, len(list2)):
        if list1[i] == list2[j]:
            commons.append(list1[i])
            break

print(f"Common elements: {commons}")
