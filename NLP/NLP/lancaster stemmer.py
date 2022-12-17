from nltk.stem import LancasterStemmer
lancaster=LancasterStemmer()

words=['Vikas','putting','puts','eaten','eating']
for word in words:

    print(word,"--->",lancaster.stem(word))
