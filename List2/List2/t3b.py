from nltk.tokenize import word_tokenize
import nltk
import string
import collections
from nltk.corpus import stopwords
nltk.download('stopwords')

f = open("Catch-22.txt", "r")
w = open("Catch-22_2.txt", "a")

text = f.read()
text_tokens = word_tokenize(text)
tokens_without_sw = [
    word for word in text_tokens if not word in stopwords.words()]

w.write(tokens_without_sw)
w.close()
f.close()
