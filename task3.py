"""
Вопрос №3

На языке Python предложить алгоритм, который быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел.
Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным).
Объяснить, почему вы считаете, что функция соответствует заданным критериям.

Вывод:
На данный момент сортировка TimSort, которая используется, как встроенная сортировка в Python,
является наиболее подходящей.

Ход алгоритма:
    1) Разделение входного массива на подмассивы по специальному алгоритму.
    2) Использование сортировки вставкой для каждого подмассива.
    3) Сборка подмассивов с помощью сортировки слиянием.

Плюсы:
    1) В среднем и худшем случае выполняется за О(n*log(n)), в лучшем случае - за О(n), что подходит для любых случаев.
    2) Сохраняет порядок одинаковых элементов, что даёт устойчивость при сортировке.
    3) За счёт сортировок вставки и слияния быстро работает с отсортированными подмассивами.

Минусы:
    1) Метод требует много памяти - О(n).
"""
from random import randint


if __name__ == '__main__':
    unsorted_list = [randint(-10, 10) for _ in range(randint(0, 100))]
    sorted_list = sorted(unsorted_list)
    print(sorted_list)
