import random

randomList = []
for i in range(0, 19):
    x = random.randint(10, 99)
    randomList.append(x)

print("Random list: " + randomList)

for i in range(0, len(randomList)):
    s = s + randomList[i]
meanValue = s/len(randomList)
print("The mean value of random list is: " + meanValue)

max = 0
for i in range(0, len(randomList)):
    if randomList[i] > max:
        max = randomList[i]
print("Maximal value is: " + max)
