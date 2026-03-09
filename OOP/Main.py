from Library import Library
from PrintedBook import PrintedBook
from EBook import EBook
from Member import Member

if __name__=="__main__":
    
    library = Library()
    
    book1 = PrintedBook("Python Basics", "John Smith", "123", 350)
    book2 = EBook("AI Guide", "Alan Turing", "456", "5MB")
    book3 = EBook("Ansi C", "Alan Smith", "789", "8MB")
    
    member1 = Member(1, "Alice")
    member2 = Member(2, "Hussain")
    
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
                     
    library.register_member(member1)
    library.register_member(member2)

    library.borrow_book(1, "Ansi C")
    library.borrow_book(2, "AI Guide")
    library.borrow_book(1, "Python Basics")
    
    member1.view_borrowed_books()
    library.show_available_books()
    
    library.return_book(1, "Ansi C")
    library.return_book(2, "AI Guide")
    
    library.show_available_books()
