import random


class TwoWheelAuto:
    """
    Родительский класс 2-КОЛЕСНЫЙ ТРАНСПОРТ

    :param max_speed: максимальная скорость траспорта в км/ч
    :param breaks_type: один из типов тормозной системы траспорта из списка ["V_brake", "Disk_brake"]
    :param transport_health: первоначальная работоспособность траспорта в % до поезкди, по умолчанию равна 100 %

    Предполагается, что траспорт совершает некую поездку, перед поездкой владелец
    проверил работоспособность транспорта, задав значение в конструкторе, после поездки
    произошел случайным образом износ траспорта, сам же владелец на состояние траспорта
    не может влиять, поэтому атрибут нельзя менять во время поездки, но можно получить его
    значение до и после поездки

    Примеры:
    >>> bicycle = TwoWheelAuto(30., "V_brake")

    """
    def __init__(self, max_speed: float, breaks_type: str, transport_health: int = 100):
        self.max_speed = max_speed
        self.breaks_type = breaks_type
        self._transport_health = transport_health

    @property
    def transport_health(self) -> int:
        """
        Метод, который выдает значение работоспособности траспорта до поезки и после нее

        Примеры:
        >>> bicycle = TwoWheelAuto(30., "V_brake")
        >>> transport_health = bicycle.transport_health
        """
        return self._transport_health

    @property
    def max_speed(self) -> float:
        """
        Метод, который выдает заданное пользователем значение максимальной скорости траспорта в км/ч

        Примеры:
        >>> bicycle = TwoWheelAuto(30., "V_brake")
        >>> max_speed = bicycle.max_speed
        """
        return self._max_speed

    @max_speed.setter
    def max_speed(self, new_max_speed: float) -> None:
        """
        Метод, который позволяет менять значение максимальной скорости траспорта в км/ч во время поездки
        :param new_max_speed: новое значение величины максимальной скорости

        :raise ValueError: если значение new_max_speed <= 0, то вызываем ошибку: скорость
        не может быть <=0 во время поездки

        Примеры:
        >>> bicycle = TwoWheelAuto(30., "V_brake")
        >>> bicycle.max_speed = 40.0
        """
        if not isinstance(new_max_speed, float):
            raise TypeError("Задано значение для max_speed не типа float.")
        if new_max_speed <= 0:
            raise ValueError("Задано не положительное значение для max_speed.")
        self._max_speed = new_max_speed

    @property
    def breaks_type(self) -> str:
        """
        Метод, который выдает заданный пользователем тип используемой тормозной системы траспорта из списка
        ["V_brake", "Disk_brake"]

        Примеры:
        >>> bicycle = TwoWheelAuto(30., "V_brake")
        >>> breaks_type = bicycle.breaks_type
        """
        return self._breaks_type

    @breaks_type.setter
    def breaks_type(self, new_breaks_type: str) -> None:
        """
        Метод, который позволяет менять значение тормозной системы траспорта во время поездки
        :param new_breaks_type: новое тип тормозной системы траспорта из списка ["V_brake", "Disk_brake"]

        Примеры:
        >>> bicycle = TwoWheelAuto(30., "V_brake")
        >>> bicycle.breaks_type = "Disk_brake"
        """
        if new_breaks_type not in ["V_brake", "Disk_brake"]:
            raise ValueError("Задан неизвестный тип тормозов breaks_type.")
        self._breaks_type = new_breaks_type

    def __str__(self):
        """
        Метод, который позволяет получить "человечное" представление класса при вызове, например print()
        """
        return f"2-колесный транспорт с макс. скоростью {self._max_speed} км/ч и типом тормозов {self._breaks_type}. " \
               f"Работоспособность транcпорта {self._transport_health} %"

    def __repr__(self):
        """
        Метод, который позволяет получить "машинное" представление класса при вызове, например print(repr())
        """
        return f"{self.__class__.__name__}(max_speed={self._max_speed!r}, breaks_type={self._breaks_type!r}, " \
               f"transport_health={self._transport_health!r})"

    def travel_time(self, road_length: float) -> int:
        """
        Метод, который позволяет считать время, затрачиваемое на прохождение траспортом заданного пути
        :param road_length: значение пути, которое должен пройти траспорт во время поездки, в км


        :raise ValueError: если значение пути <=0, вызывается ошибка

        Примеры:
        >>> bicycle = TwoWheelAuto(30., "V_brake")
        >>> travel_time = bicycle.travel_time(400.)
        """
        if not isinstance(road_length, float):
            raise TypeError("Задано значение для road_length не типа float.")
        if road_length <= 0:
            raise ValueError("Задано не положительное значение для road_length.")
        time = road_length / self.max_speed
        return round(time)

    def transport_health_after_travel(self) -> None:
        """
        Метод, который позволяет получить конечную работоспособность транспорта после поездки в %
        Работоспособность из-за случайного износа, полученного во время поездки, не увеличивается, но конечная
        работоспособность не может быть меньше 0 %

        Примеры:
        >>> bicycle = TwoWheelAuto(30., "V_brake")
        >>> bicycle.transport_health_after_travel()
        >>> transport_health_after_travel = bicycle.transport_health
        """
        wear = random.randrange(self._transport_health + 1)
        self._transport_health -= wear


class BikeWith400CCEngine(TwoWheelAuto):
    """ Дочерний класс МОТОЦИКЛ от родительского 2-КОЛЕСНЫЙ ТРАНСПОРТ

    :param max_speed: максимальная скорость траспорта в км/ч
    :param breaks_type: один из типов тормозной системы траспорта из списка ["V_brake", "Disk_brake"]
    :param transport_health: первоначальная работоспособность траспорта в % до поезкди, по умолчанию равна 100 %
    :param fuel_index: один из типов топлива из списка [95, 97, 98], влитого на АЗС
    :param injected_fuel: объем влитого в бак топлива в см^3
    :param fuel_purity: чистота влитого топлива в долях, по умолчанию считается как случайная величина, владелец мотоцикла
    доверяет выбранной АЗС и не проверял влитое топливо

    Примеры:
    >>> bike = BikeWith400CCEngine(max_speed=100.0, breaks_type="Disk_brake", fuel_index=95, injected_fuel=300.)
    """

    "объем двигателя мотоцикла. Т.к. данный класс используется для описания мотоциклов с объемом двигателя 400 см^3, данный атрибут принадлежит всему классу"
    ENGINE_DISPLACEMENT = 400. # в см^3

    def __init__(self, max_speed: float, breaks_type: str, fuel_index: int, injected_fuel: float,
                 transport_health: int = 100, fuel_purity: float = round(random.random(), 2)):
        super().__init__(max_speed, breaks_type, transport_health)
        self.fuel_index = fuel_index
        self.injected_fuel = injected_fuel
        self._fuel_purity = fuel_purity


    @property
    def fuel_purity(self) -> float:
        """
        Метод, который выдает значение чистоты влитого топлива. Чистоту влитого толпива во время поездки
        менять нельзя, поэтому setter отсутсвует

        Примеры:
        >>> bike = BikeWith400CCEngine(max_speed=100.0, breaks_type="Disk_brake", fuel_index=95, injected_fuel=300.)
        >>> fuel_purity = bike.fuel_purity
        """
        return self._fuel_purity

    @property
    def fuel_index(self) -> int:
        """
        Метод, который выдает значение индекса влитого топлива

        Примеры:
        >>> bike = BikeWith400CCEngine(max_speed=100.0, breaks_type="Disk_brake", fuel_index=95, injected_fuel=300.)
        >>> fuel_index = bike.fuel_index
        """
        return self._fuel_index

    @fuel_index.setter
    def fuel_index(self, new_fuel_index: int) -> None:
        """
        Метод, который позволяет менять индекс используемого топлива
        :param new_fuel_index: новое значение индекса топлива из списка [95, 97, 98]

        :raise ValueError: если значение индекса влитого топлива не из списка [95, 97, 98], вызывается ошибка

        Примеры:
        >>> bike = BikeWith400CCEngine(max_speed=100.0, breaks_type="Disk_brake", fuel_index=95, injected_fuel=300.)
        >>> bike.fuel_index = 98
        """
        if new_fuel_index not in [95, 97, 98]:
            raise ValueError("Задан неизвестный тип топлива fuel_index.")
        self._fuel_index = new_fuel_index

    @property
    def injected_fuel(self) -> float:
        """
        Метод, который выдает значение количества влитого топлива

        Примеры:
        >>> bike = BikeWith400CCEngine(max_speed=100.0, breaks_type="Disk_brake", fuel_index=95, injected_fuel=300.)
        >>> injected_fuel = bike.injected_fuel
        """
        return self._injected_fuel

    @injected_fuel.setter
    def injected_fuel(self, new_injected_fuel: float) -> None:
        """
        Метод, который позволяет считать время, затрачиваемое на прохождение траспортом заданного пути
        :param new_injected_fuel: новое значение влитого топлива в см^3

        :raise ValueError: если значение влитого топлива <=0, вызывается ошибка
        :raise ValueError: если значение влитого топлива > объема двигателя мотоцикла, вызывается ошибка

        Примеры:
        >>> bike = BikeWith400CCEngine(max_speed=100.0, breaks_type="Disk_brake", fuel_index=95, injected_fuel=300.)
        >>> bike.injected_fuel = 40.0
        """
        if not isinstance(new_injected_fuel, float):
            raise TypeError("Задано значение для injected_fuel не типа float.")
        if new_injected_fuel <= 0:
            raise ValueError("Задано не положительное значение для injected_fuel.")
        if new_injected_fuel > 400:
            raise ValueError("Задано значение для injected_fuel превышающее объем двигателя ENGINE_DISPLACEMENT.")
        self._injected_fuel = new_injected_fuel

    def __str__(self):
        """
        Метод, который позволяет получить "человечное" представление класса при вызове, например print()
        """
        return f"Мотоцикл с объемом двигателя 400 см^3, макс. скоростью {self._max_speed} км/ч и типом " \
               f"тормозов {self._breaks_type}. Работоспособность транcпорта {self._transport_health} %"

    def __repr__(self):
        """
        Метод, который позволяет получить "машинное" представление класса при вызове, например print(repr())
        """
        return f"{self.__class__.__name__}(max_speed={self._max_speed!r}, breaks_type={self._breaks_type!r}, " \
               f"fuel_index={self._fuel_index!r}, injected_fuel={self._injected_fuel!r}, " \
               f"transport_health={self._transport_health!r}, fuel_purity={self._fuel_purity!r})"


    def travel_time(self, road_length: float) -> int:
        """
        Перегруженный метод, который позволяет считать время, затрачиваемое на прохождение мотоциклом заданного пути.
        Т.к. мотоцикл заправлен топливом с определенной чистотой (например, на АЗС "добрый" человек разбалвил),
        выраженной в долях, то пройденный путь считается иначе, чем если бы был просто 2-КОЛЕСНЫЙ ТРАНСПОРТ, а именно:
        чем меньше чистота топлива, тем долше придется ехать.

        :param road_length: значение пути, которое должен пройти траспорт во время поездки, в км

        :raise ValueError: если значение пути <=0, вызывается ошибка

        Примеры:
        >>> bike = BikeWith400CCEngine(100., "Disk_brake", 95, 300.)
        >>> travel_time = bike.travel_time(1000.)
        """
        if not isinstance(road_length, float):
            raise TypeError("Задано значение для road_length не типа float.")
        if road_length <= 0:
            raise ValueError("Задано не положительное значение для road_length.")
        time = road_length * self._fuel_purity / self.max_speed
        return round(time)


bicycle_1 = TwoWheelAuto(30., "V_brake", 87)
print(bicycle_1.transport_health)
print(bicycle_1)
print(repr(bicycle_1))
print(bicycle_1.travel_time(1000.))
bicycle_1.transport_health_after_travel()
print(bicycle_1.transport_health)

print()
print()

bike_1 = BikeWith400CCEngine(max_speed=100.0, breaks_type="Disk_brake", fuel_index=95, injected_fuel=300.)
print(bike_1.transport_health)
print(bike_1)
print(repr(bike_1))
print(bike_1.travel_time(1000.))
bike_1.transport_health_after_travel()
print(bike_1.transport_health)

