# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Room:
    """
    Документация на класс.
    Класс описывает комнату.
    """
    def __init__(self, bed:int, table: int):
        if bed < 0:
            raise ValueError("число кроватей больше или равно нулю")
        if table < 0:
            raise ValueError("число столов больше или равно нулю")
        if not isinstance(bed, int):
            raise TypeError ("кроватей целое число")
        if not isinstance(table, int):
            raise TypeError ("столов целое число")
        self.bed = bed
        self.table = table

        def new_bed(self, number_b : int):
            """
                Документация на метод.
                Метод добавляет новые кровати в комнату.
                : param number_b : количество новых кроватей
                """
            ...
        def new_table(self, number_t : int):
            """
                Документация на метод.
                Метод добавляет новые столы в комнату.
                : param number_t : количество новых столов
                """
            ...

class Exam:
    """
    Документация на класс.
    Класс описывает результат экзамена.
    """
    def __init__(self, studentgood:int, studentbad:int):
        if studentgood < 0:
            raise ValueError("число студентов сдавших экзамен больше 0 или равно нулю")
        if studentbad < 0:
            raise ValueError("число студентов не сдавших экзамен больше 0 или равно нулю")
        if not isinstance(studentgood, int):
            raise TypeError ("число студентов сдавших экзамен целое число")
        if not isinstance(studentbad, int):
            raise TypeError ("число студентов не сдавших экзамен целое число")
        self.studentgood = studentgood
        self.studentbad = studentbad

        def student (self, studentgood:int, studentbad:int, all_st:int):
            """
                Документация на метод.
                Метод считает всех студентов пришедших на экзамен.
                : param all_st : количество всех студентов пришедших на экзамен
                """
            ...
        def sick_(self, sick_st : int, studentbad:int ):
            """
                Документация на метод.
                Метод добавляет заболевших студентов к не сдавшим.
                : param  sick_st: количество  заболевших студентов
                >>> exam = Exam(10, 5)
                >>> exam.sick_(2)
                """
            ...
class Party:
    """
    Документация на класс.
    Класс описывает вечеринку.
    """
    def __init__(self, pair:int, lonely:int):
        if pair < 0:
            raise ValueError("число пар пришедших на вечеринку больше 0 или равно нулю")
        if lonely < 0:
            raise ValueError("число одиноких людей пришедших на вечеринку  больше 0 или равно нулю")
        if not isinstance(pair, int):
            raise TypeError ("число пар пришедших на вечеринку  целое число")
        if not isinstance(lonely, int):
            raise TypeError ("число одиноких людей пришедших на вечеринку целое число")
        self.pair = pair
        self.lonely = lonely

        def all_peple(self, pair:int, lonely:int, all_:int):
            """
                Документация на метод.
                Метод считает всех людей пришедших на вечеринку.
                : param all_st : количество всех людей пришедших на вечеринку
                """
            ...
        def new_(self, new_ : int):
            """
                Документация на метод.
                Метод добавляет людей которых не приглашали на вечеринку к общему числу людей.
                : param  new_: количество людей которых не приглашали на вечеринку
                """
            ...


if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest

