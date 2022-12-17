# PorterStemmer 
from nltk.stem import PorterStemmer 
word_stemmer = PorterStemmer() 
print("Porter Stemmer=",word_stemmer.stem('writing')) 
#LancasterStemmer 
import nltk 
from nltk.stem import LancasterStemmer 
Lanc_stemmer = LancasterStemmer() 
print("Lancaster Stemmer=",Lanc_stemmer.stem('writing')) 
#RegexpStemmer 
import nltk
from nltk.stem import RegexpStemmer 
Reg_stemmer = RegexpStemmer('ing$|s$|e$|able$', min=4) 
print("Regexp Stemmer=",Reg_stemmer.stem('writing')) 
#SnowballStemmer
import nltk 
from nltk.stem import SnowballStemmer 
english_stemmer = SnowballStemmer('english') 
print("Snowball Stemmer=",english_stemmer.stem ('writing')) 
#WordNetLemmatizer 
from nltk.stem import WordNetLemmatizer 
lemmatizer = WordNetLemmatizer() 
print("word :\tlemma") 
print("rocks :", lemmatizer.lemmatize("rocks"))
print("corpora :", lemmatizer.lemmatize("corpora")) 
# a denotes adjective in "pos" 
print("WordNet Stemmer=","better :", lemmatizer.lemmatize("better", pos ="a"))
