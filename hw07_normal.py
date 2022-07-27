# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class School:
    def __init__(self, name):
        self.name = name
        self.class_rooms = []
        self.teachers = []

    def hire_teacher(self, particular_teacher):
        self.teachers.append(particular_teacher)

    def assign_class_room(self, class_room):
        self.class_rooms.append(class_room)

    def list_teachers(self, class_room):  # list в смысле перечислить, списка не возвращаем
        teachers_list = []
        for obj in class_room.objects:
            for teacher in self.teachers:
                if obj == teacher.object:
                    teachers_list.append(teacher)
        print(f"В классе {class_room.name} преподают:")
        for teacher in teachers_list:
            print(teacher.name, teacher.patronymic, teacher.surname)

    def list_classes(self):
        print(f"Все классы школы {self.name}:")
        for class_room in self.class_rooms:
            print(class_room.name)


class ClassRoom:
    def __init__(self, name, *objects_names):
        self.name = name
        self.objects = objects_names
        self.students = []

    def accept_student(self, particular_student):
        self.students.append(particular_student)

    def list_students(self):
        print(f"Ученики класса {self.name}:")
        for student in self.students:
            print("{}.{}. {}".format(student.name[0], student.patronymic[0], student.surname))

    def student_objects(self, student):  # Вроде бы просится в класс Student, но тогда тому понадобится передавать дополнительные объекты
        if student in self.students:
            print("Предметы ученика по имени {}.{}. {}:".format(student.name[0], student.patronymic[0], student.surname))
            for obj in self.objects:
                print(obj)
        else:
            print("{}.{}. {} не учится в этом классе".format(student.name[0], student.patronymic[0], student.surname))


class Person:
    def __init__(self, name, patronymic, surname):
        self.name = name
        self.patronymic = patronymic
        self.surname = surname


class Student(Person):
    def __init__(self, name, patronymic, surname, class_room, *parents):  # На случай неполных или шведских семей)))
        super().__init__(name, patronymic, surname)
        self.class_room = class_room
        self.parents = parents

    def list_parents(self):
        print("Родители ученика по имени {}.{}. {}:".format(self.name[0], self.patronymic[0], self.surname))
        for parent in self.parents:
            print(parent.name, parent.patronymic, parent.surname)


class Parent(Person):  # Проверки по полу делать не будем, считаем, што это школа в толерантном обществе)))
    pass               # В задании мама и папа, но это стандартно и скучно))))


class Teacher(Person):
    def __init__(self, name, patronymic, surname, object_name):
        super().__init__(name, patronymic, surname)
        self.object = object_name


school = School("№18")  # Построили школу

parent1 = Parent("Иван", "Анатольевич", "Сидоров")  # Родители - существуют
parent2 = Parent("Марина", "Петровна", "Сидорова")
parent3 = Parent("Дмитрий", "Григорьевич", "Морозов")
parent4 = Parent("Анастасия", "Владимировна", "Морозова")

outside_student = Student("Андрей", "Васильевич", "Петров", None)  # Левый чел для проверки

teacher1 = Teacher("Иван", "Аркадьевич", "Арсеньев", "Математика")
teacher2 = Teacher("Мария", "Ивановна", "Васильева", "Русский язык")
teacher3 = Teacher("Людмила", "Степановна", "Аганина", "Химия")

school.hire_teacher(teacher1)
class_1B = ClassRoom("1B", "Математика", "Обществознание")
school.assign_class_room(class_1B)



student1 = Student("Сергей", "Иванович", "Сидоров", "1B", parent1, parent2)
student1.list_parents()

class_1B.accept_student(student1)

school.list_teachers(class_1B)
school.list_classes()

class_1B.list_students()
class_1B.student_objects(student1)
