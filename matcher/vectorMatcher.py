from gensim import models, corpora
from sklearn import svm

from .matcher import Matcher


class VectorMatcher(Matcher):
    def __init__(self):

        self.vecModel = None
        # TODO

    def match(self, query):
        pass
        # TODO
