class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name (self):
        return self._name

    @property
    def author (self):
        return self._author

class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name,author)
        if not isinstance(pages, int):
            raise TypeError
        self.pages = pages

    def __str__(self):
        super().__str__()

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages = {self.pages!r})"

    @property
    def pages (self):
        return self.pages

    @pages.setter
    def pages(self, new_p):
        if not isinstance(new_p, int):
            raise TypeError
        if new_p <= 0:
            raise ValueError
        self.pages = new_p

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        super().__str__()

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration = {self.duration})"

    @property
    def duration(self):
        return self.duration

    @ duration.setter
    def duration(self, new_):
        if not isinstance(new_, float):
            raise TypeError
        if new_<= 0:
            raise ValueError
        self.duration = new_