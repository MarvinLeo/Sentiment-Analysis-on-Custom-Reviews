import nltk
import pickle
from nltk import word_tokenize
from nltk.classify import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import LinearSVC, NuSVC
from sklearn.model_selection import train_test_split
from nltk.classify import ClassifierI

def mode(arr) :
    m = max([arr.count(a) for a in arr])
    return [x for x in arr if arr.count(x) == m][0] if m>1 else None

## In this project a Voting Emsemble Learning methods is used
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

##read the words library propressed
all_words_file = open("pickled_algos/all_words.pickle", "rb")
all_words = pickle.load(all_words_file)
all_words_file.close()

##read the propressed samples
documents_file = open("pickled_algos/documents.pickle", "rb")
documents = pickle.load(documents_file)
documents_file.close()

##only part of the most frequent words are needed for training, use 5k as initial
top_words = 5000
word_features = [words for (words, c) in all_words.most_common(top_words)]

## save the word features for further use(prediction)
save_words_features = open("pickled_algos/word_features5k.pickle", "wb")
pickle.dump(word_features, save_words_features)
save_words_features.close()

## create features function for each sample
def create_features(text):
    words = word_tokenize(text)
    features = {}
    for word in word_features:
        features[word] = (w in words)
    return features

features_sets = [(create_features(sample), label) for (sample, label) in documents]

## split the training sets into training and validation sets
training_set, validation_set = train_test_split(features_sets, test_size=0.2)


###create all the classifier we gonna use
classifier = nltk.NaiveBayesClassifier.train(training_set)
print "Original Naive Bayes Algo accuracy:", nltk.classify.accuracy(classifier, validation_set)*100
classifier.show_most_informative_features(15)
## save the classifier
save_classifier = open("pickled_algos/naivebayes5k.pickle", "wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
# print "MNB_classifier accuracy:", nltk.classify.accuracy(MNB_classifier, testing_set)*100
# MNB_classifier.show_most_informative_features(15)   ##show which features are most distinctive
save_classifier = open("pickled_algos/MNB_5k.pickle", "wb")
pickle.dump(MNB_classifier, save_classifier)
save_classifier.close()


BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
# print "BernoulliNB_classifier accuracy:", nltk.classify.accuracy(BernoulliNB_classifier, testing_set)*100
save_classifier = open("pickled_algos/BernoulliNB_5k.pickle", "wb")
pickle.dump(BernoulliNB_classifier, save_classifier)
save_classifier.close()
#
LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
#print "LogisticRegression_classifier accuracy:", nltk.classify.accuracy(LogisticRegression_classifier, testing_set)*100
save_classifier = open("pickled_algos/Logistic_5k.pickle", "wb")
pickle.dump(LogisticRegression_classifier, save_classifier)
save_classifier.close()
#
SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
# print "SGDClassifier_classifier accuracy:", nltk.classify.accuracy(SGDClassifier_classifier, testing_set)*100
save_classifier = open("pickled_algos/SGD_5k.pickle", "wb")
pickle.dump(SGDClassifier_classifier, save_classifier)
save_classifier.close()
#
# # SVC_classifier = SklearnClassifier(SVC())
# # SVC_classifier.train(training_set)
# # print "SVC_classifier accuracy:", nltk.classify.accuracy(SVC_classifier, testing_set)*100

#
LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
# print "LinearSVC_classifier accuracy:", nltk.classify.accuracy(LinearSVC_classifier, testing_set)*100
save_classifier = open("pickled_algos/LinearSVC_5k.pickle", "wb")
pickle.dump(LinearSVC_classifier, save_classifier)
save_classifier.close()

NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
# print "NuSVC_classifier accuracy:", nltk.classify.accuracy(NuSVC_classifier, testing_set)*100
save_classifier = open("pickled_algos/NuSVC_5k.pickle", "wb")
pickle.dump(NuSVC_classifier, save_classifier)
save_classifier.close()

voted_classifier = VoteClassifier(classifier, MNB_classifier, BernoulliNB_classifier, LogisticRegression_classifier,
                                  SGDClassifier_classifier, LinearSVC_classifier, NuSVC_classifier)

print "Voted_classifier accuracy:", nltk.classify.accuracy(voted_classifier, validation_set)*100
