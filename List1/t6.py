string = input("Type a string: ")
letters = []
stringAgain = ""

for i in range(0, len(string)):
    if string[i] == "a":
        continue
    else:
        letters.append(string[i])

for l in letters:
    stringAgain += l

print(f'String without "a": {stringAgain}')
