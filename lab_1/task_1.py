# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union
import doctest


class Table:
    def __init__(self, width: Union[float, int], height: Union[float, int], depth: Union[float, int]):
        """
        Создание объекта "Стол"

        :param width: длина стола
        :param height: высота стола
        :param depth: глубина стола

        Примеры:
        >>> table = Table(20.2, 20.2, 20.2) # инициализация экземпляра класса
        """
        if not isinstance(width, (int, float)):
            raise TypeError("Длина стола должна быть типа int или float")
        if width <= 0:
            raise ValueError("Длина стола должна быть положительным числом")
        self.width = width

        if not isinstance(height, (int, float)):
            raise TypeError("Высота стола должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота стола должна быть положительным числом")
        self.height = height

        if not isinstance(depth, (int, float)):
            raise TypeError("Глубина стола должна быть типа int или float")
        if depth <= 0:
            raise ValueError("Глубина стола должна быть положительным числом")
        self.depth = depth

    def is_square_table(self) -> bool:
        """
        Метод, который проверяет, является ли стол квадратным

        :return: Является ли стол квадратным

        Примеры:
        >>> table = Table(20.2, 20.2, 20.2)
        >>> table.is_square_table()
        """
        ...

    def cut_table_legs(self, remove_height: Union[float, int]) -> None:
        """
        Обрезание высоты ножек стола.
        :param remove_height: значение высоты, на которую нужно укоротить имеющиеся ножки стола

        :raise ValueError: Если значение высоты, на которую нужно укоротить ножки, больше высоты
        самих ножек, то вызываем ошибку. Также вызываем ошибку, если значение высоты, на которую
        нужно укоротить ножки, отрицательная

        Примеры:
        >>> table = Table(20.2, 20.2, 20.2)
        >>> table.cut_table_legs(10.1)
        """
        if not isinstance(remove_height, (int, float)):
            raise TypeError("Значение высоты, на которую нужно укоротить имеющиеся ножки стола,"
                            " должно быть типа int или float")
        if remove_height < 0:
            raise ValueError("Значение высоты, на которую нужно укоротить имеющиеся ножки стола,"
                             "должно неотрицательным числом")
        if remove_height > self.height:
            raise ValueError("Значение высоты, на которую нужно укоротить имеющиеся ножки стола,"
                             "не может превышать значения высоты имеющихся ножек стола")
        ...


class Book:
    def __init__(self, name: str, pages: int, spine: str):
        """
        Создание объекта "Книга"

        :param name: название книги
        :param pages: количество страниц в книге
        :param spine: тип корешка книги (либо Soft, либо Hard)

        Примеры:
        >>> book = Book("Book name", 500, "Soft") # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название книги должно быть типа str")
        if len(name) == 0:
            raise ValueError("Название книги не может быть пустой строкой")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество страниц книги должно быть типа int")
        if pages <= 0:
            raise ValueError("У книги количество страниц не может быть меньше или равно 0")
        self.pages = pages

        if spine not in ["Soft", "Hard"]:
            raise ValueError("Тип корешка книги может быть либо Soft, либо Hard")
        self.spine = spine

    def type_of_spine(self) -> str:
        """
        Метод, который возвращает тип корешка книги

        :return: возвращается значение Soft или Hard

        Примеры:
        >>> book = Book("Book name", 500, "Soft")
        >>> book.type_of_spine()
        """
        ...

    def update_pages_number(self, new_pages: int) -> None:
        """
        Метод, который меняет количество страниц в книге
        :param new_pages: новое количество страниц в книге

        :raise ValueError: Если новое количество страниц в книге меньше либо равно нулю, то вызываем ошибку.

        Примеры:
        >>> book = Book("Book name", 500, "Soft")
        >>> book.update_pages_number(200)
        """
        if not isinstance(new_pages, int):
            raise TypeError("Новое количество страниц книги должно быть типа int")
        if new_pages <= 0:
            raise ValueError("У книги новое количество страниц не может быть меньше или равно 0")
        ...


class CarModel:
    def __init__(self, manufacture_name: str, gauge: int):
        """
        Создание объекта "Модель машины"

        :param manufacture_name: производитель модели (среди Busch, Herpa, Wiking, Rietze, Brekina)
        :param gauge: масштаб модели (может быть либо 87 (т.е. 1:87), либо 120 (т.е. 1:120), либо 160 (т.е. 1:160))

        Примеры:
        >>> car_model = CarModel("Herpa", 120) # инициализация экземпляра класса
        """
        if manufacture_name not in ["Busch", "Herpa", "Wiking", "Rietze", "Brekina"]:
            raise ValueError("Имя производителя модели машины не определено")
        self.manufacture_name = manufacture_name

        if gauge not in [87, 120, 160]:
            raise ValueError("Масштаб модели машины неверный")
        self.gauge = gauge

    def change_gauge(self, new_gauge: int) -> None:
        """
        Метод, который меняет масштаб модели машины
        :param new_gauge: новый масштаб модели

        :raise ValueError: Если новый масштаб не находится среди целочисленных значений 87 (т.е. 1:87),
        либо 120 (т.е. 1:120), либо 160 (т.е. 1:160), то вызываем ошибку.

        Примеры:
        >>> car_model = CarModel("Herpa", 120)
        >>> car_model.change_gauge(87)
        """
        if new_gauge not in [87, 120, 160]:
            raise ValueError("Новый масштаб модели машины неверный")
        ...

    def change_manufacture_name(self, new_manufacture_name: str) -> None:
        """
        Метод, который меняет производителя модели машины
        :param new_manufacture_name: новый производитель модели

        :raise ValueError: Если новый производитель модели не находится среди Busch, Herpa, Wiking,
        Rietze, Brekina, то вызываем ошибку.

        Примеры:
        >>> car_model = CarModel("Herpa", 120)
        >>> car_model.change_manufacture_name("Busch")
        """
        if new_manufacture_name not in ["Busch", "Herpa", "Wiking", "Rietze", "Brekina"]:
            raise ValueError("Новое имя производителя модели машины не определено")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
