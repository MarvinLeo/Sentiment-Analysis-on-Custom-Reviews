#-----------------------------------------------------------#
# Make sure to run this file to create your own documents for training
#-----------------------------------------------------------#
import nltk
from nltk.corpus import movie_reviews
from nltk.tokenize import word_tokenize
import pickle
import sys
reload(sys)
sys.setdefaultencoding("ISO-8859-1")

#the words set and samples to save
all_words = []
documents = []

#read the samples
#you can create your own positive or negetive file
pos = open("documents/positive.txt", "r").read()
neg = open("documents/negative.txt", "r").read()

##choose the words type for features
## j is adject, r is adverb, v is verb
#allowed_word_types = ["J", "R", "V"]
allowed_word_types = ["J"]

##loeding all the files into all words and samples
line = 0
print "pos started"
for p in pos.split("\n"):
    documents.append((p, "pos"))
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())
    line += 1
    if line % 50 == 0:
        print line, "lines of Pos finished"
print "POS samples finished"
line = 0
print "neg started"
for p in neg.split("\n"):
    documents.append((p, "neg"))
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())
    line += 1
    if line % 50 == 0:
        print line, "lines of neg finished"
print "NEG samples finished"

## add the movies reviews words as well
for w in movie_reviews.words():
    all_words.append(w.lower())         #read all the words; build a words lib

save_documents = open("pickled_algos/documents.pickle", "wb")
pickle.dump(documents, save_documents)
save_documents.close()

save_all_words = open("pickled_algos/all_words.pickle", "wb")
pickle.dump(all_words, save_all_words)
save_all_words.close()
print "Loading samples and all_word finishied"

##Then your own sample libraries and words are built