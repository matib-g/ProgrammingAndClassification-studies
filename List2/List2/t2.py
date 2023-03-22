import nltk
import string
import collections

d = 3
text = 'Implement a Cesar cipher using with a given shift parameter d in Python'


def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = plaintext.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)


m = caesar(text, d)
print(m)
