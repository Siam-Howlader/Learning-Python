from Book import Book
class PrintedBook(Book):
    
    def __init__(self, title: str, author: str, isbn: str, pages: int):
        
        self.__pages = pages
        super().__init__(title, author,isbn)
    def get_pages(self) -> int:
        return self.__pages
    
    def __str__(self) -> str:
        return f"Book title: {super().get_title()}, Book author: {super().get_author()}, ISBN: {super().get_isbn()}, Pages: {self.get_pages()}"
