import nltk
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
nltk.download('punkt')

snow_stemmer = SnowballStemmer(language='english')

f = open("Catch-22.txt", "r")
w = open("Catch-22_3.txt", "a")

text_lines_list = f.readlines()
porter = PorterStemmer()


def stemSentence(sentence):
    token_words = word_tokenize(sentence)
    token_words
    stem_sentence = []
    for word in token_words:
        stem_sentence.append(porter.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)


for line in text_lines_list:
    stem_sentence = stemSentence(line)
    w.write(stem_sentence)

w.close()
f.close()
