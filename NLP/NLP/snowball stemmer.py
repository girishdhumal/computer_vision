from nltk.stem import SnowballStemmer
snowball=SnowballStemmer(language="english")


words=['Vikas','generous','generate','generation','generously']
for word in words:
    print(word,"--->",snowball.stem(word))
