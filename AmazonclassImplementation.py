from datetime import date

class Product:
    def __init__(self, product_id, price, prime_eligible, number_in_stock, date_added):
        self.set_product_id(product_id)
        self.set_price(price)
        self.set_prime_eligible(prime_eligible)
        self.set_number_in_stock(number_in_stock)
        self.set_date_added(date_added)

    def get_product_id(self):
        return self._product_id

    def set_product_id(self, product_id):
        self._product_id = product_id

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def get_prime_eligible(self):
        return self._prime_eligible

    def set_prime_eligible(self, prime_eligible):
        self._prime_eligible = prime_eligible

    def get_number_in_stock(self):
        return self._number_in_stock

    def set_number_in_stock(self, number_in_stock):
        self._number_in_stock = number_in_stock

    def get_date_added(self):
        return self._date_added

    def set_date_added(self, date_added):
        self._date_added = date_added

    def print(self):
        print(f"Product ID: {self.get_product_id()}")
        print(f"Price: ${self.get_price():.2f}")
        print(f"Prime Eligible: {'Yes' if self.get_prime_eligible() else 'No'}")
        print(f"Number in Stock: {self.get_number_in_stock()}")
        print(f"Date Added: {self.get_date_added()}")

class Book(Product):
    def __init__(self, product_id, price, prime_eligible, number_in_stock, date_added, title, author, num_pages, publisher, publication_date):
        super().__init__(product_id, price, prime_eligible, number_in_stock, date_added)
        self.set_title(title)
        self.set_author(author)
        self.set_num_pages(num_pages)
        self.set_publisher(publisher)
        self.set_publication_date(publication_date)

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_author(self):
        return self._author

    def set_author(self, author):
        self._author = author

    def get_num_pages(self):
        return self._num_pages

    def set_num_pages(self, num_pages):
        self._num_pages = num_pages

    def get_publisher(self):
        return self._publisher

    def set_publisher(self, publisher):
        self._publisher = publisher

    def get_publication_date(self):
        return self._publication_date

    def set_publication_date(self, publication_date):
        self._publication_date = publication_date

    def print(self):
        super().print()
        print(f"Title: {self.get_title()}")
        print(f"Author: {self.get_author()}")
        print(f"Number of Pages: {self.get_num_pages()}")
        print(f"Publisher: {self.get_publisher()}")
        print(f"Publication Date: {self.get_publication_date()}")

# Example usage
if __name__ == "__main__":
    # Creating three example books using information from Amazon

    book1 = Book(
        product_id="0143126563",
        price=12.99,
        prime_eligible=True,
        number_in_stock=100,
        date_added=date(2022, 6, 12),
        title="To Kill a Mockingbird",
        author="Harper Lee",
        num_pages=336,
        publisher="Harper Perennial Modern Classics",
        publication_date=date(2006, 5, 23)
    )

    book2 = Book(
        product_id="1982137274",
        price=14.49,
        prime_eligible=True,
        number_in_stock=200,
        date_added=date(2021, 1, 15),
        title="Atomic Habits",
        author="James Clear",
        num_pages=320,
        publisher="Avery",
        publication_date=date(2018, 10, 16)
    )

    book3 = Book(
        product_id="031649934X",
        price=24.99,
        prime_eligible=True,
        number_in_stock=50,
        date_added=date(2023, 3, 5),
        title="The Last Thing He Told Me",
        author="Laura Dave",
        num_pages=320,
        publisher="Simon & Schuster",
        publication_date=date(2021, 5, 4)
    )

    # Printing the example book details
    print("Book 1 Details:")
    book1.print()
    print("\nBook 2 Details:")
    book2.print()
    print("\nBook 3 Details:")
    book3.print()

    # Testing getter and setter methods
    print("\nTesting getter and setter methods:")
    book1.set_price(11.99)
    print(f"Updated price of Book 1: ${book1.get_price():.2f}")
    
    book2.set_title("Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones")
    print(f"Updated title of Book 2: {book2.get_title()}")
    
    book3.set_author("Laura Dave and Some Co-author")
    print(f"Updated author of Book 3: {book3.get_author()}")
