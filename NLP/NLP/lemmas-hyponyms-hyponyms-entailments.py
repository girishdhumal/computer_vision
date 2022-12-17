import nltk
from nltk.corpus import wordnet
print(wordnet.synsets("father"))
print(wordnet.synset("father.n.01").lemma_names())
for e in wordnet.synsets("father"):
    print(f'{e} --> {e.lemma_names()}')
    print(wordnet.synset('father.n.01').lemmas())
    print(wordnet.lemma('father.n.01.father').synset())
    print(wordnet.lemma('father.n.01.father').name())
    syn = wordnet.synset('father.n.01')
    print(syn.hyponyms)
    print([lemma.name() for synset in syn.hyponyms() for lemma in synset.lemmas()])
    vehicle = wordnet.synset('vehicle.n.01')
    car = wordnet.synset('car.n.01')
    print(car.lowest_common_hypernyms(vehicle))
