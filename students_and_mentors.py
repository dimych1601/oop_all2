class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self._average()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}\n')

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average(self):
        total_subject_grades = 0
        count_subject_grades = 0
        for subject, value in self.grades.items():
            total_subject_grades += sum(value)
            count_subject_grades += len(value)
        if count_subject_grades == 0:
            return 0
        return total_subject_grades / count_subject_grades


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self._average()}\n')

    def _average(self):
        total_subject_grades = 0
        count_subject_grades = 0
        for subject, value in self.grades.items():
            total_subject_grades += sum(value)
            count_subject_grades += len(value)
        if count_subject_grades == 0:
            return 0
        return total_subject_grades / count_subject_grades


class Reviewer(Mentor):
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n')

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


student1 = Student('Иван', 'Иванов', 'Мужской')
student1.courses_in_progress += ['Python', 'C++', 'Java']
student1.finished_courses += ['JavaScript']
student2 = Student('Ирина', 'Иринова', 'female')
student2.courses_in_progress += ['Python', 'Ruby']
student2.finished_courses += ['PHP']

lecturer1 = Lecturer('Петр', 'Петров')
lecturer2 = Lecturer('Зоя', 'Захарова')

reviewer1 = Reviewer('Мария', 'Сидорова')
reviewer1.courses_attached += ['Python', 'PHP']
reviewer2 = Reviewer('Павел', 'Кузнецов')
reviewer2.courses_attached += ['JavaScript', 'Python']

student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer2, 'Python', 8)
student2.rate_lecturer(lecturer1, 'Python', 8)
student2.rate_lecturer(lecturer2, 'Python', 9)

reviewer1.rate_hw(student1, 'Python', 7)
reviewer1.rate_hw(student2, 'Python', 8)
reviewer2.rate_hw(student1, 'Python', 6)
reviewer2.rate_hw(student2, 'Python', 6)

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)
