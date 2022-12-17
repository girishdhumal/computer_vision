import nltk
from nltk import*
nltk.download('punkt')
sentence="India is a republic nation. we are proud Indians"
print(nltk.sent_tokenize(sentence))
