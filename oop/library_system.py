class Book:
    """Base class for a book."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        """String representation for a Book instance."""
        return f"Book: {self.title} by {self.author}"

    def display_info(self):
        """Return a string representation of the book (fallback)."""
        return self.__str__()


class EBook(Book):
    """Derived class for an electronic book."""
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # File size in KB

    def __str__(self):
        """String representation for an EBook instance."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class for a printed book."""
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count  # Number of pages

    def __str__(self):
        """String representation for a PrintBook instance."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class to manage a collection of books."""
    def __init__(self):
        self.books = []  # Composition: A list to store books

    def add_book(self, book):
        """Add a book to the library."""
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added: {book}")
        else:
            print("Error: Only instances of Book or its subclasses can be added.")

    def list_books(self):
        """List all books in the library."""
        if not self.books:
            print("The library has no books.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f" - {book}")

