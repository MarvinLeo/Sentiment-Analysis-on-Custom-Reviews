import nltk
import random
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.model_selection import train_test_split
from nltk.classify import ClassifierI
from nltk.tokenize import word_tokenize

def mode(arr) :
    m = max([arr.count(a) for a in arr])
    return [x for x in arr if arr.count(x) == m][0] if m>1 else None

class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        choice_votes = votes.count(mode(votes))
        conf = float(choice_votes) / len(votes)
        return conf


## read the parameters
# documents_file = open("pickled_algos/documents.pickle", "rb")
# documents = pickle.load(documents_file)
# documents_file.close()

word_features5k_file = open("pickled_algos/word_features5k.pickle", "rb")
word_features = pickle.load(word_features5k_file)
word_features5k_file.close()

def create_features(text):
    words = word_tokenize(text)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

## loading the classifiers
# features_file = open("pickled_algos/features_sets.pickle", "rb")           ##need to save the features somewhere
# features_sets = pickle.load(features_file)
# features_file.close()
#
# training_set, testing_set = train_test_split(features_sets, test_size=0.2)
##read the classifiers
file = open("pickled_algos/naivebayes5k.pickle", "rb")
classifier = pickle.load(file)
file.close()

file = open("pickled_algos/MNB_5k.pickle", "rb")
MNB_classifier = pickle.load(file)
file.close()

file = open("pickled_algos/BernoulliNB_5k.pickle", "rb")
BernoulliNB_classifier = pickle.load(file)
file.close()

file = open("pickled_algos/Logistic_5k.pickle", "rb")
LogisticRegression_classifier = pickle.load(file)
file.close()

file = open("pickled_algos/SGD_5k.pickle", "rb")
SGDClassifier_classifier = pickle.load(file)
file.close()

file = open("pickled_algos/LinearSVC_5k.pickle", "rb")
LinearSVC_classifier = pickle.load(file)
file.close()

file = open("pickled_algos/NuSVC_5k.pickle", "rb")
NuSVC_classifier = pickle.load(file)
file.close()

voted_classifier = VoteClassifier(classifier, MNB_classifier, BernoulliNB_classifier, LogisticRegression_classifier,
                                  SGDClassifier_classifier, LinearSVC_classifier, NuSVC_classifier)
#
# print "Voted_classifier accuracy:", nltk.classify.accuracy(voted_classifier, testing_set)*100

def sentiment(text):
    feats = create_features(text)
    return voted_classifier.classify(feats), voted_classifier.confidence(feats)

## use this as module

