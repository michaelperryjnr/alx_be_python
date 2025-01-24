class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False


        def check_out(self):
            if not self.is_checked_out:
                self.is_checked_out = True
                return True
            
            return False
        

        def return_book(self):
            if self.is_checked_out:
                self.is_checked_out = False
                return True
            
            return False
        


class Library:
    def __init__(self):
        self._books = []


    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return True
        return False
    

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return True
        return False
    

    def list_available_books(self):
        for book in self._books:
            if not book.is_checked_out:
                print(f"{book.title} by {book.author}")