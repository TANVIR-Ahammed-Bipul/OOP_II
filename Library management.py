class LibraryItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            print(f"{self.title} by {self.author} has been checked out.")
            self.checked_out = True
        else:
            print(f"{self.title} by {self.author} is already checked out.")

    def return_item(self):
        if self.checked_out:
            print(f"{self.title} by {self.author} has been returned.")
            self.checked_out = False
        else:
            print(f"{self.title} by {self.author} is not checked out.")


class Book(LibraryItem):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre


class Magazine(LibraryItem):
    def __init__(self, title, author, issue):
        super().__init__(title, author)
        self.issue = issue


# Example usage:
book = Book("Harry Potter", "J.K. Rowling", "Fantasy")
magazine = Magazine("National Geographic", "Various", "March 2024")

book.check_out()
magazine.check_out()

book.return_item()
magazine.return_item()
