list1 = ["From", "a", "list", "of", "strings",
         "remove", "all", "strings", "longer", "than", "5"]
s = ['']

for i in range(0, len(list1)):
    if len(list1[i]) > len(s[0]):
        s.clear()
        s[0] = list1[i]
    elif len(list1[i]) == len(s[0]):
        s.append(list1[i])
    elif len(list1[i]) < len(s[0]):
        continue

print(s)
