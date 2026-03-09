from Book import Book
from Member import Member


class Library:

    def __init__(self):
        self.__books = []
        self.__members = []

    def get_books(self) -> list[Book]:
        return self.__books

    def get_members(self) -> list[Member]:
        return self.__members

    def add_book(self, book: Book):
        books = self.__books
        if book in books:
            print(f"{book.get_title()} titled book already exists!")
        else:
            self.__books.append(book)

    def register_member(self, member: Member):
        members = self.__members
        if member in members:
            print(f"Member {member.get_name()} already registered!")
        else:
            self.__members.append(member)

    def find_book_by_title(self, title: str) -> Book:
        books = self.__books
        for book in books:
            if book.get_title() == title:
                return book
        return None

    def borrow_book(self, member_id: int, title: str):
        temp_book = self.find_book_by_title(title)
        temp_member = None
        for member in self.__members:
            if member.get_member_id() == member_id:
                temp_member = member
                break
        if temp_book.get_borrow_status():
            print("This book is borrowed by someone else")
        if temp_book.get_borrow_status() == False and temp_member:
            temp_member.borrow(temp_book)
        if not temp_member:
            print(f"Member id -> {member_id} does not exists!")
        if not temp_book:
            print("Book not found")

    def return_book(self, member_id: int, title: str):
        members=self.__members
        temp_member=None
        for member in members:
            if member.get_member_id()==member_id:
                temp_member=member
                break
        if not temp_member:
            print("Member not found!")
        else:
            temp_book=self.find_book_by_title(title)
            if not temp_book:
                print("Book not found!")
            else:
                if temp_book.get_borrow_status()==True:
                    temp_member.return_book(temp_book)
                else:
                    print("Book is not borrowed yet!")
    def show_available_books(self):
        books = self.__books
        for book in books:
            if book.get_borrow_status() == False:
                print(book)
