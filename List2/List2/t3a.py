import nltk
import string
# import collections

f = open("Catch-22.txt", "r")
w = open("Catch-22_a.txt", "a")

str = f.read()
table = str.maketrans(dict.fromkeys(string.punctuation))
new_f = str.translate(table)

w.write(new_f)
w.close()
f.close()
