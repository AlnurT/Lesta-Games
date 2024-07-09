"""
Вопрос №2

На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO.
Объяснить плюсы и минусы каждой реализации.

Оценивается:
- Полнота и качество реализации
- Оформление кода
- Наличие сравнения и пояснения по быстродействию

Вывод:
Если требуется низкое потребление памяти, то нужно выбирать список, а если нужны читаемость и малый объём кода,
то выбираем двухстороннюю очередь (deque).
"""
from collections import deque


class CircularFifoList:
    """
    Реализация через список.

    Плюсы:
        1) Использование стандартного списка
        2) Быстрые чтение, запись и подсчёт размера: О(1)

    Минусы:
        1) Большое потребление памяти (значения None в списке)
        2) Сложность и размер кода: проверки и работа с указателями
    """
    def __init__(self, size: int):
        self.size = size
        self.buffer = [None] * size
        self.head = 0
        self.tail = 0

    def write(self, num):
        """Запись в список"""
        if self.buffer[self.head]:
            self.tail = (self.tail + 1) % self.size

        self.buffer[self.head] = num
        self.head = (self.head + 1) % self.size

    def read(self):
        """Чтение, вывод и удаление значения"""
        if self.buffer[self.tail] is None:
            return

        num = self.buffer[self.tail]
        self.buffer[self.tail] = None
        self.tail = (self.tail + 1) % self.size
        return num

    def clear(self):
        """Полная очистка"""
        self.buffer = [None] * self.size

    def get_buffer(self):
        """Вывод списка со значениями"""
        if self.buffer[self.head] or self.head < self.tail:
            return self.buffer[self.tail:] + self.buffer[:self.head]

        return self.buffer[self.tail: self.head]

    def get_buffer_size(self):
        """Вывод размера списка со значениями"""
        if self.buffer[self.head]:
            return self.size
        elif self.head >= self.tail:
            return self.head - self.tail

        return self.size + self.head - self.tail


class CircularFifoDeque:
    """
    Реализация через очередь.

    Плюсы:
        1) Прямое назначение для использования очереди
        2) Быстрые чтение, запись и подсчёт размера: О(1)
        3) Читаемость и малый размер кода: отсутствие сложных проверок и указателей из-за наличия встроенной цикличности

    Минусы:
        1) Большее потребление памяти для deque по сравнению с обычным списком
    """
    def __init__(self, size: int):
        self.size = size
        self.buffer = deque(maxlen=size)

    def write(self, num):
        """Запись в очередь"""
        self.buffer.append(num)

    def read(self):
        """Чтение, вывод и удаление значения"""
        return self.buffer.popleft() if len(self.buffer) else None

    def clear(self):
        """Полная очистка"""
        self.buffer = deque(maxlen=self.size)

    def get_buffer(self):
        """Вывод списка со значениями очереди"""
        return list(self.buffer)

    def get_buffer_size(self):
        """Вывод размера очереди"""
        return len(self.buffer)


def get_circular_fifo():
    method = int(input("Используем: \n"
                       "1 способ - список\n"
                       "2 способ - двухстороннюю очередь\n"
                       "Способ: "))
    size = int(input("Размер буфера: "))
    buffer = CircularFifoList(size) if method == 1 else CircularFifoDeque(size)
    command_hash = {
        1: buffer.write,
        2: buffer.read,
        3: buffer.clear,
        4: buffer.get_buffer,
        5: buffer.get_buffer_size
    }

    while True:
        print("\nВиды операций: \n"
              "1 - записать\n"
              "2 - прочитать\n"
              "3 - очистить\n"
              "4 - получить буфер\n"
              "5 - получить размер буфера\n"
              "0 - завершить")
        code = int(input("\nВведите код операции: "))
        if code == 0:
            break
        elif code == 1:
            num = input("Введите число: ")
            res = command_hash[1](num)
        else:
            res = command_hash[code]()

        print("Выполнено" if res is None else res)

        if buffer.get_buffer_size() == 0:
            print("Буфер пуст")
        elif buffer.get_buffer_size() == size:
            print("Буфер заполнен")


if __name__ == '__main__':
    get_circular_fifo()
