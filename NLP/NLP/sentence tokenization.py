import nltk
from nltk import tokenize
nltk.download('punkt')
nltk.download('words')

para="Hello! My Name is Vikas Gupta. Today you will be learning NLTK."
sents = tokenize.sent_tokenize(para)
print("\n sentence Tokenize=================== \n",sents)


#word tokenization
print("\n word Tokenize=================== \n")


for index in range (len(sents)):
    words = tokenize.word_tokenize(sents[index])
    print(words)
