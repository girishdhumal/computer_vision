import nltk
from nltk import*
nltk.download('punkt')
sent="India is a republic nation. we are proud Indians"
print(nltk.word_tokenize(sent))
