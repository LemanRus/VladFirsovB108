# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

import os
import re

path_workers = os.path.join("data", "workers")
path_hours = os.path.join("data", "hours_of")
path_salary = os.path.join("data", "salary")


class Worker:
    def __init__(self, biography, hours_worked_path):
        biography_facts = re.split(r'\W+', biography)
        self.name = biography_facts[0]
        self.surname = biography_facts[1]
        self.salary = int(biography_facts[2])
        self.job = biography_facts[3]
        self.norm_hours = int(biography_facts[4])

        with open(hours_worked_path, "r", encoding="UTF-8") as hours:
            pass_head = 1
            for line in hours:
                if pass_head:
                    pass_head = 0
                    continue
                worker_hours = re.split(r'\W+', line)
                if worker_hours[0] == self.name and worker_hours[1] == self.surname:
                    self.hours_worked = int(worker_hours[2])

    def make_payroll_accounting(self, path_to_salary):
        if self.norm_hours == self.hours_worked:
            salary = self.salary
        elif self.norm_hours > self.hours_worked:
            salary = self.salary * self.hours_worked / self.norm_hours
        else:
            salary = self.salary + self.salary * (self.hours_worked - self.norm_hours) / self.norm_hours * 2
        with open(path_to_salary, "a", encoding="UTF-8") as salary_file:
            if os.path.getsize(path_to_salary) == 0:
                print("{:10}{:10}{:10}".format("Имя", "Фамилия", "Зарплата"), file=salary_file)
            print("{:10}{:10}{:<10.2f}".format(self.name, self.surname, salary), file=salary_file)


workers = []

with open(path_workers, "r", encoding="UTF-8") as workers_file:
    pass_head = 1
    for line in workers_file:
        if pass_head:
            pass_head = 0
            continue
        workers.append(Worker(line, path_hours))

for worker in workers:
    worker.make_payroll_accounting(path_salary)
