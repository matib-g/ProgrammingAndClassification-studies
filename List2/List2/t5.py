from nltk.probability import FreqDist
import nltk
import nltk.book
from nltk.book import text1, text2, text3, text4, text5, text6, text7, text8, text9
import nltk.corpus
from nltk.corpus import webtext
from nltk.corpus import gutenberg
nltk.download('gutenberg')

fdist6 = FreqDist(text6)
fdist7 = FreqDist(text7)
fdist6.keys()
fdist7.keys()
tx6 = fdist6['knight']
tx7 = fdist7['knight']
s = tx6 + tx7

print(tx6)
print(tx7)
print(s)
