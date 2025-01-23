class Book:
    # A class representing a book with title, author, and publication year.

    def __init__(self, title, author, year):
        """
        Initialize a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        # Return a user-friendly string representation of the book.
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # Return an official representation of the book instance.
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        # Print a message upon object deletion.
        print(f"Deleting {self.title}")

