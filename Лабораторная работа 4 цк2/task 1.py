class Supermarket:
    """базовый класс описывыающий магазины"""
    def __init__(self, area: int, appointment: str):
        self.area = area
        self.appointment = appointment

    def __str__(self) -> str:
        return f'Площадь"{self.area}"'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.area!r},{self.appointment})'

    @staticmethod
    def ar(a: int, b: int) -> int:
        """метод считает площадь магазинов.
        a - длина помещения,
        b - ширина
        """
        return a*b

    def appo (self, opinion: str) -> str:
        """метод спрашивает нравится ли магазин - ответ да или нет"""
        ...

class Pyaterochka(Supermarket):
    """дочерний класс описывыающий магазин Пятерочка"""
    def __init__(self, area: int, appointment: str, color : str):
        super().__init__(area, appointment)
        self.color = color

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.area!r}, {self.appointment}, {self.color!r})'

    def appo(self, answer: str, opinion: str) -> int:
        """ метод перегружает метод из базого класса и дополняет его вопросов 'Оценка магазина по 5 балльной шкале'"""
        super().appo(opinion)
        ...



class Magnit(Supermarket):
    """дочерний класс описывыающий магазин Магнит"""
    def __init__(self, area: int, appointment: str, slogan: str):
        super().__init__(area, appointment)
        self.slogan = slogan

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.area!r}, {self.appointment}, {self.slogan!r})'


    def appo(self, answer: str, opinion: str) -> int:
        """ метод перегружает метод из базого класса и дополняет его вопросов 'Оценка магазина по 5 балльной шкале'"""
        super().appo(opinion)
        ...


