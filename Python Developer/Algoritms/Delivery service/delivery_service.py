# ID посылки 121234127.

def min_platforms(robots: list[int], limit: int) -> int:
    """
    Функция для определения минимального количества транспортных платформ,
    необходимого для перевозки всех роботов.

    Параметры:
        - robots: массив целых чисел, представляющих вес отдельных роботов;
        - limit: максимальный вес, которая выдерживает платформа.

    Возвращает:
        минимальное количество платформ, необходимое для перевозки всех
    роботов.
    """

    left_point = 0
    right_point = len(robots) - 1
    platforms_count = 0

    robots = sorted(robots)

    while left_point <= right_point:
        total_weight = robots[left_point] + robots[right_point]
        if total_weight <= limit:
            left_point += 1
        platforms_count += 1
        right_point -= 1

    return platforms_count


if __name__ == '__main__':
    robots = [int(robot) for robot in input().split()]
    limit = int(input())
    print(min_platforms(robots, limit))
