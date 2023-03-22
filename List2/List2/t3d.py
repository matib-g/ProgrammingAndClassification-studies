import nltk
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
nltk.download('punkt')

f = open("Catch-22.txt", "r")
text_lines_list = f.readlines()

d = dict()

for line in text_lines_list:
    line = line.strip()
    line = line.lower()
    words = line.split(" ")
    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1

sort_d = dict(sorted(d.items(), key=lambda item: item[1]))
for key in list(sort_d.keys()):
    if sort_d[key] >= 100:
        print(key, ":", sort_d[key])

#sort_d = sorted(d.items(), key=lambda x: x[1], reverse=True)

# for i in sort_d:
#    if sort_d[i] >= 100:
#        print(i[0], ":", i[1])

f.close()
