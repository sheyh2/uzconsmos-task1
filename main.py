import math


def count_rectangles(n, m):
    # Функция для подсчета количества прямоугольников в сетке n x m
    return (n * (n + 1) // 2) * (m * (m + 1) // 2)


def find_best_grid(target):
    # Оценка верхней границы для n и m, основываясь на приближении
    upper_bound = int(math.sqrt(2 * target)) + 1

    closest_diff = float('inf')
    best_n, best_m = -1, -1
    best_count = -1

    # Перебираем возможные размеры сетки
    for n in range(1, upper_bound):
        for m in range(1, upper_bound):
            rect_count = count_rectangles(n, m)

            # Если кол-во прямоугольников не превышает кол-во целевой прямоугольников
            if rect_count <= target:
                diff = target - rect_count
                if diff < closest_diff:
                    closest_diff = diff
                    best_n, best_m = n, m
                    best_count = rect_count

    return best_n, best_m, best_count


def print_result():
    target = int(input('Введите целевое число: '))
    n, m, count = find_best_grid(target)

    # Выводим результат
    print(f"Лучший размер сетки: {n} x {m}")
    print(f"Площадь: {n * m}")
    print(f"Количество прямоугольников: {count}")


print_result()
