file=open(r"C:\Users\Vikas\Desktop\stem.txt")
print(file)
my_lines_list=file.readlines()
print(my_lines_list)
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
sentence="Pythoners are very intelligent and work very pythonly and now they are pythoning their way to success."
porter=PorterStemmer()
def stemming(sentence):
    token_words=word_tokenize(sentence)
    print(token_words)
    stem_sentence=[]
    for word in token_words:
        stem_sentence.append(porter.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)
print(my_lines_list[0])
print("Stemmed sentence")
x=stemming(my_lines_list[0])
print(x)
stem_file=open(r"C:\Users\Admin\OneDrive\Desktop\stem1.txt",mode="a+",  encoding="utf-8")
for line in my_lines_list:
    stem_sentence=stemming(line)
    stem_file.write(stem_sentence)
stem_file.close()
