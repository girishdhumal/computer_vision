import nltk
from nltk.corpus import PlaintextCorpusReader
corpus_root = r'C:\Users\Vikas\AppData\Roaming\Python\Python310\site-packages\nltk\test\unit\test_corpora.py'
filelist = PlaintextCorpusReader(corpus_root,'.*')
print ('\n File list: \n')
print (filelist.fileids())
print (filelist.root)

print ('\n\n Statistics for each text:\n')
print('AvgWordLen\tAvgSentenceLen\tno.ofTimesEachWordAppearsOnAvg\tFileName')
for fileid in filelist.fileids():
    num_chars = len(filelist.raw(fileid))
    num_words = len(filelist.words(fileid))
    num_sents = len(filelist.sents(fileid))
    num_vocab = len(set([w.lower() for w in filelist.words(fileid)]))
    print (int(num_chars/num_words),'\t\t\t', int(num_words/num_sents),'\t\t\t', int(num_words/num_vocab),'\t\t', fileid)
