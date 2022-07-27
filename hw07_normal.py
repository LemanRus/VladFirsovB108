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
        particular_student.class_room = self.name

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
    def __init__(self, name, patronymic, surname, *parents):  # На случай неполных или шведских семей)))
        super().__init__(name, patronymic, surname)
        self.parents = parents
        self.class_room = ""

    def list_parents(self):
        print("Родители ученика по имени {}.{}. {}:".format(self.name[0], self.patronymic[0], self.surname))
        for parent in self.parents:
            print(parent.name, parent.patronymic, parent.surname)

    def show_my_class_room(self):
        print(self.class_room)


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

student1 = Student("Сергей", "Иванович", "Сидоров", parent1, parent2)  # Сибсы
student2 = Student("Екатерина", "Ивановна", "Сидорова", parent1, parent2)
student3 = Student("Дмитрий", "Дмитриевич", "Морозов", parent3, parent4)
student4 = Student("Пётр", "Дмитриевич", "Морозов", parent3, parent4)
student5 = Student("Елизавета", "Дмитриевна", "Морозова", parent3, parent4)

outside_student = Student("Андрей", "Васильевич", "Петров", None)  # Левый чел для проверки

teacher1 = Teacher("Иван", "Аркадьевич", "Арсеньев", "Математика")
teacher2 = Teacher("Мария", "Ивановна", "Васильева", "Русский язык")
teacher3 = Teacher("Людмила", "Степановна", "Аганина", "Химия")  # Теперь там есть жизнь, прям как Трон)))

school.hire_teacher(teacher1)  # Нанимаем учителей
school.hire_teacher(teacher2)
school.hire_teacher(teacher3)

class_7B = ClassRoom("7Б", "Математика", "Химия")  # Назначим расписание
class_9A = ClassRoom("9А", "Математика", "Русский язык")
class_11A = ClassRoom("11А", "Математика", "Русский язык", "Химия")

school.assign_class_room(class_7B)  # Классы (которые школьные) организованы в школе
school.assign_class_room(class_9A)
school.assign_class_room(class_11A)

# Для проверки предлагаю раскомментировать любой код ниже

# class_7B.accept_student(student1)
# class_7B.accept_student(student4)
# class_9A.accept_student(student2)
# class_9A.accept_student(student3)
# class_11A.accept_student(student5)
#
# school.list_classes()
#
# school.list_teachers(class_7B)
# school.list_teachers(class_9A)
# school.list_teachers(class_11A)
#
# class_7B.list_students()
# class_9A.list_students()
# class_11A.list_students()
#
# class_7B.student_objects(student1)
# class_7B.student_objects(student2)
# class_9A.student_objects(student3)
# class_9A.student_objects(student4)
# class_9A.student_objects(outside_student)
# class_11A.student_objects(student5)
# class_11A.student_objects(student1)
#
# student1.list_parents()
# student2.list_parents()
# student3.list_parents()
# student4.list_parents()
# student5.list_parents()

