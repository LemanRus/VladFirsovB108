# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


class Triangle:
    def __init__(self, point1, point2, point3):
        self.point1 = complex(*point1)  # Комплексные числа по определению есть координаты на плоскости, просто удобно
        self.point2 = complex(*point2)
        self.point3 = complex(*point3)

    def calculate_sides(self):  # Вспомогательная функция, чтобы не дублировать код, считает длины сторон
        a = abs(self.point1 - self.point2)
        b = abs(self.point2 - self.point3)
        c = abs(self.point3 - self.point1)
        return a, b, c

    def calculate_perimeter(self):
        perimeter = sum(self.calculate_sides())
        return perimeter

    def calculate_area(self):  # Результат float не совсем точный, можно прописывать читаемый формат вывода
        a, b, c = self.calculate_sides()
        half_perimeter = self.calculate_perimeter() / 2
        area = (half_perimeter * (half_perimeter - a) * (half_perimeter - b) * (half_perimeter - c)) ** 0.5
        return area

    def calculate_height(self, pos_of_top):
        """
        Считает высоту треугольника из указанной точки
        :param pos_of_top: координаты вершины треугольника, из которой необходимо опустить высоту
        :return: длина высоты, опущенной из указанной точки на противоположную сторону
        """
        top_point = complex(*pos_of_top)
        tops = dict(zip((self.point3, self.point1, self.point2), self.calculate_sides()))
        height = 2 * (self.calculate_area()) / tops.get(top_point)
        return height


triangle = Triangle((5, 5), (6, 6), (9, 15))
# print(triangle.calculate_sides())
print(triangle.calculate_perimeter())
print(triangle.calculate_area())
print(triangle.calculate_height((9, 15)))


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь


class Trapeze:
    def __init__(self, point1, point2, point3, point4):  # Нужно ли для уровня easy проверять, что дана точно трапеция?
        self.point1 = complex(*point1)
        self.point2 = complex(*point2)
        self.point3 = complex(*point3)
        self.point4 = complex(*point4)

    def calculate_sides(self):
        a = abs(self.point1 - self.point2)
        b = abs(self.point2 - self.point3)
        c = abs(self.point3 - self.point4)
        d = abs(self.point4 - self.point1)
        return a, b, c, d

    def calculate_perimeter(self):
        perimeter = sum(self.calculate_sides())
        return perimeter

    def calculate_area(self):  # Результат float не совсем точный, можно прописывать читаемый формат вывода
        a, b, c, d = self.calculate_sides()
        area = (a + b) / 2 * (c**2 - (((a - b)**2 + c**2 - d**2) / (2 * (a - b)))**2)**0.5
        return area

    def is_eq_sides(self):  # Снова для easy - нужно ли искать непараллельные стороны? Или нумерация по часовой подойдёт?
        a, b, c, d = self.calculate_sides()
        if round(b, 3) == round(d, 3):
            return True
        else:
            return False


trapeze = Trapeze((5, 5), (6, 6), (9, 15), (14, 10))
print(trapeze.calculate_sides())
print(trapeze.calculate_perimeter())
print(trapeze.calculate_area())
print(trapeze.is_eq_sides())
