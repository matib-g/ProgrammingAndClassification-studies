list1 = ["From", "a", "list", "of", "strings",
         "remove", "all", "strings", "longer", "than", "5"]

for j in range(0, len(list1)):
    if len(list1[j]) > 5:
        list1.pop(j)

print(list1)
