from receipt import Receipt
from article import Article
from article import df

print(df)
try:
    article_id: int = int(input("Choose an article to by: "))
except ValueError:
    print("Please enter a valid number")
    exit(1)
article = Article(article_id)
article.buy()
receipt = Receipt(article)
receipt.generate()