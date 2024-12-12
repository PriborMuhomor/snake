import math


def polar_angle(x, y):
    # Вычисляем угол в радианах от -pi до pi
    angle = math.atan2(y, x)

    # Преобразуем в диапазон от 0 до 2*pi
    if angle < 0:
        angle += 2 * math.pi

    return angle


# Пример использования
x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))

angle = polar_angle(x, y)
print(f"Полярный угол: {angle} радиан")