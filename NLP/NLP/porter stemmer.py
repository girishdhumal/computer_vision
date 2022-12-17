from nltk.stem import PorterStemmer
porter=PorterStemmer()
words=['connect','connecting','making','connectings','connected','connects','Vikas']
for word in words:
    print(word,"--->",porter.stem(word))
