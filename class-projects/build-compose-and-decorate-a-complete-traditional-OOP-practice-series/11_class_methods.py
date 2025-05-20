class Book:
    total_books = 0
    
    def __init__(self, title):
        self.title = title
        Book.increment_book_count()
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        return cls.total_books

# Example usage
if __name__ == "__main__":
    book1 = Book("Python Programming")
    book2 = Book("Data Structures")
    print(f"Total books: {Book.total_books}")