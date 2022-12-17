import nltk
nltk.download('averaged_perceptron_tagger')
from collections import defaultdict
text = nltk.word_tokenize("Vikas likes to play cricket. Vikas does not like to play football.")
tagged = nltk.pos_tag(text)
print(tagged)
addNounWords = []
count=0
for words in tagged:
    val = tagged[count][1]
    if(val == 'NN' or val == 'NNS' or val == 'NNPS' or val == 'NNP'):
        addNounWords.append(tagged[count][0])
        count+=1
    print (addNounWords)
    temp = defaultdict(int) # memoizing count
for sub in addNounWords:
    for wrd in sub.split():
        temp[wrd] += 1
    res = max(temp, key=temp.get)
    print("Word with maximum frequency : " + str(res))
