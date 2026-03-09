class Book:
    
    def __init__(self,title: str,author: str,isbn: str):
        self.__title=title
        self.__author=author
        self.__isbn=isbn
        self.__is_borrowed=False
        
    def get_title(self) -> str:
        return self.__title
    
    def get_author(self) -> str:
        return self.__author
    
    def get_isbn(self) -> str:
        return self.__isbn

    def get_borrow_status(self):
        return self.__is_borrowed
    
    def set_title(self,title: str):
        self.__title=title

    def set_author(self,author: str):
        self.__author=author

    def set_isbn(self,isbn: str):
        self.__isbn=isbn

    def set_borrow_status(self,status: bool):
        self.__is_borrowed=status
    
    def borrow_book(self):
        self.__is_borrowed=True
        
    def return_book(self):
        self.__is_borrowed = False
    
    def __str__(self) -> str:
        return f"Book title: {self.__title}, Book author: {self.__author}, ISBN: {self.__isbn}, availability: {self.__is_borrowed}"
        