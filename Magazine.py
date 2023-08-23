class Magazine:
    all_magazines = []
    
def __init__(self, name, category):
    self._name = name
    self._category = category
    self._articles = []
    self.__class__.all_magazines.append(self)

def name(self):
    return self._name

def category(self):
    return self._category

def all(self):
    return self.__class__.all_magazines

def add_article(self, article):
    self._articles.append(article)

def contributors(self):
    return list(set([article.author() for article in self._articles]))

def article_titles(self):
    return [article.title() for article in self._articles]

@classmethod
def find_by_name(cls, name):
    for magazine in cls.all_magazines:
        if magazine.name() == name:
            return magazine

def contributing_authors(self):
    author_count = {}
    for article in self._articles:
        author = article.author()
        if author in author_count:
            author_count[author] += 1
        else:
            author_count[author] = 1
    return [author for author, count in author_count.items() if count > 2]