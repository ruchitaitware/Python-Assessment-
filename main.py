from user import User
from book import Book
from fiction import Fiction
from non_fiction import NonFiction
from tomerater import TomeRater
import populate

if __name__ == '__main__':
    Hawkings = User('Hawkings', 'hawkings@gmail.com')

    email = Hawkings.get_email()
    print(email)

    Hawkings.change_email('shawkings@gmail.com')

    user = User("Hawkings", "hawkings@gmail.com")
    print(user.__repr__())

    user = User("Hawkings", "hawkings@gmail.com")
    user.name = 'Hawkings'
    user.email = 'hawkings@gmail.com'

    science = Book('science', '12345')
    title = science.get_title()
    print(title)

    isbn = science.get_isbn()
    print(isbn)

    science.set_isbn('6789')

    science.add_rating(2)
    print(science.ratings)

    science.add_rating(3)
    print(science.ratings)

    book = Book("science", 12345)
    book.title = 'science'
    book.isbn = '12345'

    chinua = Fiction('Things Fall Apart', 'Chinua Achebe', 7293740137)
    author = chinua.get_author()
    print(author)

    fiction = Fiction("Things Fall Apart", "Chinua Achebe", 72937401371)
    print(fiction.__repr__())

    society_of_mind = NonFiction("Society of Mind", "Artificial Intelligence", "beginner", 34876289321)
    subject = society_of_mind.get_subject()
    print(subject)

    society_of_mind = NonFiction("Society of Mind", "Artificial Intelligence", "beginner", 34876289322)
    level = society_of_mind.get_level()
    print(level)

    non_fiction = NonFiction("Society of Mind", "Artificial intelligence", "beginner", 34876289323)
    print(non_fiction.__repr__())

    user = User("Hawkings", "hawkings@email.com")
    user.read_book("Things Fall Apart", 3)
    average = user.get_average_rating()
    print(average)

    book = Book("science", "123456")
    book.add_rating(1)
    book.add_rating(4)
    average = book.get_average_rating()
    print(average)

    tomerater = TomeRater()

    # create book
    book1 = tomerater.create_book("Society of Mind", 3487628932)













