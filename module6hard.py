import math


class Figure:
    def __init__(self, color, *sides):
        self.__sides = []
        self.__color = list(color)
        self.filled = False

        # Установка сторон
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count  # Заполняем единицами

    @property
    def sides_count(self):
        return 0

    def get_color(self):
        return self.__color

    def set_color(self, rgb):
        r, g, b = rgb
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_color(self, r, g, b):
        return isinstance(r, int) and isinstance(g, int) and isinstance(b, int) and \
            0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        return self.__sides

    def get_perimeter(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi) if self.get_sides() else 0

    def get_square(self):
        return math.pi * (self.__radius ** 2)

    def get_radius(self):
        return self.__radius


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == 3:
            a, b, c = sides
            s = (a + b + c) / 2  # Полупериметр
            self.__height = (2 * math.sqrt(s * (s - a) * (s - b) * (s - c))) / a  # Высота

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == 1:
            self.__sides = [sides[0]] * self.sides_count  # 12 одинаковых сторон

    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3


# Пример кода для проверки:
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color((55, 66, 77))  # Изменится
print(circle1.get_color())  # [55, 66, 77]
cube1.set_color((300, 70, 15))  # Не изменится
print(cube1.get_color())  # [222, 35, 130]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())  # [6, 6, 6, ..., 6]
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())  # [15]

# Проверка периметра (круга), это и есть длина:
print(circle1.get_perimeter())  # Окружность (приближенно) -> пример длины

# Проверка объёма (куба):
print(cube1.get_volume())  # 216
