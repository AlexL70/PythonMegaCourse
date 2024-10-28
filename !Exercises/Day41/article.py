import pandas as pd

DATA_PATH = 'data/articles.csv'

df = pd.read_csv(DATA_PATH)

class Article:
    def __init__(self, article_id: int):
        if df.loc[df['id'] == article_id].empty:
            raise Exception(f"Article with id {article_id} not found.")
        self._id = article_id
        self.name = df.loc[df['id'] == article_id, 'name'].squeeze()
        self.price = df.loc[df['id'] == article_id, 'price'].squeeze()
        self.in_stock = df.loc[df['id'] == article_id, 'in stock'].squeeze()

    def buy(self):
        if self.in_stock > 0:
            self.in_stock -= 1
            df.loc[df['id'] == self._id, 'in_stock'] = self.in_stock
            df.to_csv(DATA_PATH, index=False)
        else:
            raise Exception(f"Sorry. Article \"{self.name}\" is out of stock.")