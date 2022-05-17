class Book:
    isbns = []

    def __init__(self, title, isbn):
        if isbn in Book.isbns:
            print("Book with same ISBN already exists")
        else:
            Book.isbns.append(isbn)
            self.title = title
            self.isbn = isbn
            self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn.upper()

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print('This book ISBN has been updated')

    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print('Invalid rating')

    def __eq__(self, other):
        return self.title == other.title and self.isbn == other.isbn

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
