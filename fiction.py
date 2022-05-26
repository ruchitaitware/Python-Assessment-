from book import Book


class Fiction(Book):
    def __init__(self, title, author, isbn, price):
        super(). __init__(title, isbn, price)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return f'{self.title} by {self.author}'





