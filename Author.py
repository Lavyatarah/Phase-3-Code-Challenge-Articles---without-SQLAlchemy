class Author:
    all_authors = []

def __init__(self, name):
    self._name = name
    self._articles = []
    self._magazines = []
    self.__class__.all_authors.append(self)

def name(self):
    return self._name

def articles(self):
    return self._articles

def magazines(self):
    return self._magazines

def add_article(self, magazine, title):
    article = articles(self, magazine, title)
    self._articles.append(article)
    magazine.add_article(article)

def topic_areas(self):
    return list(set([article.magazine().category() for article in self._articles]))
def name(self):
    return self._name

def articles(self):
    return self._articles

def magazines(self):
    return self._magazines

def add_article(self, magazine, title):
    article = articles(self, magazine, title)
    self._articles.append(article)
    magazine.add_article(article)

def topic_areas(self):
    return list(set([article.magazine().category() for article in self._articles]))

def magazines(self):
    return self._magazines

def add_article(self, magazine, title):
    article = articles(self, magazine, title)
    self._articles.append(article)
    magazine.add_article(article)

def topic_areas(self):
    return list(set([article.magazine().category() for article in self._articles]))