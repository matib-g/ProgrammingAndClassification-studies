
while True:
    try:
        a = float(input("Type the minimal value: a = "))
        b = float(input("Type the maximal value: b = "))
        c = int(input("Type the divider: "))
    except ValueError:
        print("a and b should by a number and c should be an integer. Try again.")
        continue
    if a > b:
        print("The b must be greater than a! Try again")
        continue
    else:
        break

divisors = []

for i in range(int(a), int(b)+1):
    if i % c == 0:
        divisors.append(i)

print(divisors)
