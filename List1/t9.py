from collections import Counter


def freqLetters(string):
    c = Counter(string)
    m = [0, '']
    for i in c:
        if c[i] > m[0]:
            m[0] = c[i]
            m[1] = i
    return m[1]


string = input("Enter some string: ")
print("Most frequent element in " + string + ": " + freqLetters(string))
