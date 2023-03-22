sentence = input("Type sentence: ")
c = 0
n = 0

for i in sentence:
    if i.isalpha():
        c += 1
    elif i.isdigit():
        n += 1
    else:
        continue

print(f"Number of letters: {c}")
print(f"Number of digits: {n}")
