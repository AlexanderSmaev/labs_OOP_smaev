class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Задано значение для pages не типа int.")
        if new_pages <= 0:
            raise ValueError("Задано не положительное значение для pages.")
        self._pages = new_pages

    def __str__(self):
        return f"Бумажная книга {self.name!r}. Автор {self.author}. Количество страниц {self._pages}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, float):
            raise TypeError("Задано значение для duration не типа float.")
        if new_duration <= 0:
            raise ValueError("Задано не положительное значение для duration.")
        self._duration = new_duration

    def __str__(self) -> str:
        return f"Электронная книга {self.name!r}. Автор {self.author}. Продолжительность {self._duration}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"


paper_book_1 = PaperBook("Руслан и Людмила", "А.С. Пушкин", 200)
print(paper_book_1)
print(repr(paper_book_1))
paper_book_1.pages = 210
print(paper_book_1)
print(repr(paper_book_1))

print()
print()

audio_book_1 = AudioBook("Руслан и Людмила", "А.С. Пушкин", 200.)
print(audio_book_1)
print(repr(audio_book_1))
audio_book_1.duration = 25.
print(audio_book_1)
print(repr(audio_book_1))
