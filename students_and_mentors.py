class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and
                course in lecturer.courses_attached and
                course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade_homework(self):
        if len(self.grades.values()) == 0:
            return 0
        return sum(self.grades.values()) / len(self.grades.values())

    def __str__(self):
        return f'Имя: {self.name}\n\
                 Фамилия: {self.surname}\n\
                 Средняя оценка за домашние задания: {self.average_grade_homework()}\n\
                 Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n\
                 Завершенные курсы: {", ".join(self.finished_courses)}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    grades = {}

    def average_grade_lection(self):
        if len(self.grades.values()) == 0:
            return 0
        return sum(self.grades.values()) / len(self.grades.values())

    def __str__(self):
        return f'Имя:{self.name}\n\
                 Фамилия:{self.surname}\n\
                 Средняя оценка за лекции:{self.average_grade_lection()}'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and
                course in self.courses_attached and
                course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя:{self.name}\nФамилия:{self.surname}'
