import nltk
from nltk import*
from nltk.probability import FreqDist
nltk.download('punkt')

sent="India is a republic nation. we are a proud Indians. India is a great nation."
words=word_tokenize(sent)
print(words)
distribution=FreqDist(sent)
print(distribution)
distribution. most_common (2)
