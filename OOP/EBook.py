from Book import Book
class EBook(Book):
    
    def __init__(self,title: str,author: str,isbn: str,file_size: str):
        self.__file_size=file_size
        super().__init__(title,author,isbn)
        
    def get_file_size(self) -> str:
        return self.__file_size
    
    def __str__(self) -> str:
        return f"Book title: {super().get_title()}, Book author: {super().get_author()}, ISBN: {super().get_isbn()}, File size: {self.__file_size}"
