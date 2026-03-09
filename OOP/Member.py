from Book import Book

class Member:
    
    def __init__(self,member_id: int,name: str):
        self.__member_id=member_id
        self.__name=name
        self.__borrowed_books=[]
        
    def get_member_id(self) -> int:
        return self.__member_id
    
    def get_name(self) -> str:
        return self.__name
    
    def get_borrowed_books(self) -> list[Book]:
        return self.__borrowed_books
    
    def borrow(self,book: Book):
        book.borrow_book()
        self.__borrowed_books.append(book)
        
    def return_book(self,book):
        self.__borrowed_books.remove(book)
        book.return_book()
        
    def view_borrowed_books(self):
        for book in self.__borrowed_books:
            print(book)
