import nltk
from nltk.tag import DefaultTagger

exptagger = DefaultTagger('NN')
nltk.download('treebank')
from nltk.corpus import treebank

testsentences = treebank.tagged_sents()[1000:]
print(exptagger.accuracy(testsentences))
# Tagging a list of sentences
import nltk
from nltk.tag import DefaultTagger

exptagger = DefaultTagger('NN')
print(exptagger.tag_sents([['Hi', ','], ['How', 'are', 'you', '?']]))
