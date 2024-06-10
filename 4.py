# imagine you are developing a library management system. write a python class 'Book' with attributes 'title', 'author' and ISBN, and a method to display   book details. then create asubclass 'Ebook' that adds an attribute 'file_format' and override the display method to include the file format.


class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
    
    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.ISBN}")

class Ebook(Book):
    def __init__(self, title, author, ISBN, file_format):
        super().__init__(title, author, ISBN)
        self.file_format = file_format
    
    def display_details(self):
        super().display_details()
        print(f"File Format: {self.file_format}")

# Example usage
book = Book("1984", "George Orwell", "1234567890")
ebook = Ebook("1984", "George Orwell", "1234567890", "PDF")

print("Book Details:")
book.display_details()
print("\nEbook Details:")
ebook.display_details()
