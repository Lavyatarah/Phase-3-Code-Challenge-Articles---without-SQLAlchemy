from Author import Author
from Magazine import Magazine
from Articles import Article

author1 = Author("John Doe")
author2 = Author("Jane Smith")

magazine1 = Magazine("Tech Magazine", "Technology")
magazine2 = Magazine("Sci-Fi Magazine", "Science Fiction")

article1 = Article(author1, magazine1, "Introduction to AI")
article2 = Article(author2, magazine1, "The Future of Technology")
article3 = Article(author1, magazine2, "Exploring New Worlds")

print("Author:", author1.name())
print("Article Title:", article1.title())
print("Magazine Name:", magazine1.name())
print("Magazine Category:", magazine1.category())

author1.add_article(magazine1, "AI Ethics")
author2.add_article(magazine1, "Quantum Computing")
author1.add_article(magazine2, "Time Travel")

print("Author Articles:", [article.title() for article in author1.articles()])
print("Author Magazines:", [magazine.name() for magazine in author1.magazines()])
print("Contributors for Magazine:", [author.name() for author in magazine1.contributors()])