BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id_ = id_
        self.name = name
        self.pages = pages

    def get_book_id(self) -> int:
        return self.id_

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})"


class Library:
    def __init__(self, books=[]):
        self.books = books

    def get_next_book_id(self) -> int:
        if len(self.books) == 0:
            return 1
        else:
            return self.books[-1].get_book_id() + 1

    def get_index_by_book_id(self, id_to_find: int) -> int:
        for current_index, current_book in enumerate(self.books):
            if id_to_find == current_book.get_book_id():
                return current_index
        raise ValueError("Книги с запрашиваемым id не существует")



if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__

    print()
    print()
    library = Library(list_books)
    print(f"Следующий id равен {library.get_next_book_id()}")
    find_id=2
    print(f"Индекс книги с id={find_id} равен {library.get_index_by_book_id(find_id)}")

