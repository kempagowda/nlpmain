'''NLTK includes a small selection of texts from the Project filelist electronic text
archive, which contains some 25,000 free electronic books, hosted at
http://www.filelist.org/. We begin by getting the Python interpreter to load the NLTK
package, then ask to see nltk.corpus.filelist.fileids(), the file identifiers in this corpus:'''
import nltk
nltk.download('punkt')
from nltk.corpus import PlaintextCorpusReader
corpus_root = 'test'
filelist = PlaintextCorpusReader(corpus_root, '.*')
print ('\n File list: \n')
print (filelist.fileids())
print (filelist.root)

'''display other information about each text, by looping over all the values of fileid
corresponding to the filelist file identifiers listed earlier and then computing statistics
for each text.'''
print ('\n\nStatistics for each text:\n')
print
('AvgWordLen\tAvgSentenceLen\tno.ofTimesEachWordAppearsOnAvg\tFileName')
for fileid in filelist.fileids():
 num_chars = len(filelist.raw(fileid))
 num_words = len(filelist.words(fileid))
 num_sents = len(filelist.sents(fileid))
 num_vocab = len(set([w.lower() for w in filelist.words(fileid)]))
 print (int(num_chars/num_words),'\t\t\t', int(num_words/num_sents),'\t\t\t',
int(num_words/num_vocab),'\t\t', fileid)
