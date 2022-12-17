import nltk
from nltk import tokenize
nltk.download('punkt')
nltk.download('words')

para="Hola! Mi nombre es Vikas Gupta. Hoy aprenderás NLTK."
sents = tokenize.sent_tokenize(para,language = 'spanish')

print("\n sentence Tokenize=================== \n",sents) #word tokenization
print("\n word Tokenize=================== \n")


for index in range (len(sents)):
    words = tokenize.word_tokenize(sents[index],language = 'spanish')
    print(words)
