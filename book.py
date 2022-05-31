class Book:
    isbns = []

    def __init__(self, title, isbn, price):
        if isbn in Book.isbns:
            print(f"Book with same ISBN {isbn} already exists")
        else:
            Book.isbns.append(isbn)
            self.title = title
            self.isbn = isbn
            self.price = price
            self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn.upper()

    def get_price(self):
        return self.price

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print(f'This book ISBN has {new_isbn} been updated')

    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print('Invalid rating')

    def __eq__(self, other):
        return self.title == other.title and self.isbn == other.isbn and self.price == other.price

    def get_average_rating(self):

        # iterates through all values in self.ratings
        # calculate the average rating
        # it should return this average

        total_rating = 0

        for rating in self.ratings:
            total_rating = total_rating + rating
        num_of_rating = len(self.ratings)

        average = total_rating / num_of_rating
        return average

    def __hash__(self):
        return hash((self.title, self.isbn))
