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
                f'Средняя оценка за домашние задания: {self.average_student()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}\n')

    def __eq__(self, other):
        return self.average_student() == other.average_student()

    def __ne__(self, other):
        return self.average_student() != other.average_student()

    def __lt__(self, other):
        return self.average_student() < other.average_student()

    def __gt__(self, other):
        return self.average_student() > other.average_student()

    def __le__(self, other):
        return self.average_student() <= other.average_student()

    def __ge__(self, other):
        return self.average_student() >= other.average_student()

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and
                course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_student(self):
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
    grades = {}

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_lecturer()}\n')

    def __eq__(self, other):
        return self.average_lecturer() == other.average_lecturer()

    def __ne__(self, other):
        return self.average_lecturer() != other.average_lecturer()

    def __lt__(self, other):
        return self.average_lecturer() < other.average_lecturer()

    def __gt__(self, other):
        return self.average_lecturer() > other.average_lecturer()

    def __le__(self, other):
        return self.average_lecturer() <= other.average_lecturer()

    def __ge__(self, other):
        return self.average_lecturer() >= other.average_lecturer()

    def average_lecturer(self):
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


def avg_all_students(*students):
    total_avg = 0
    count_students = 0
    for student in students:
        total_avg += student.average_student()
        count_students += 1
    if count_students == 0:
        return 0
    return total_avg / count_students


def avg_all_lecturers(*lecturers):
    total_avg = 0
    count_students = 0
    for lecturer in lecturers:
        total_avg += lecturer.average_lecturer()
        count_students += 1
    if count_students == 0:
        return 0
    return total_avg / count_students


student1 = Student('Иван', 'Иванов', 'Мужской')
student1.courses_in_progress += ['Python', 'C++', 'Java']
student1.finished_courses += ['JavaScript']
student2 = Student('Ирина', 'Иринова', 'Женский')
student2.courses_in_progress += ['Python', 'Ruby']
student2.finished_courses += ['PHP']

lecturer1 = Lecturer('Петр', 'Петров')
lecturer1.courses_attached += ['Python', 'C++', 'Java']
lecturer2 = Lecturer('Зоя', 'Захарова')
lecturer2.courses_attached += ['Python', 'Ruby']

reviewer1 = Reviewer('Мария', 'Сидорова')
reviewer1.courses_attached += ['Python', 'PHP']
reviewer2 = Reviewer('Павел', 'Кузнецов')
reviewer2.courses_attached += ['JavaScript', 'Python']

student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer2, 'Python', 8)
student2.rate_lecturer(lecturer1, 'Python', 6)
student2.rate_lecturer(lecturer2, 'Python', 9)

reviewer1.rate_hw(student1, 'Python', 7)
reviewer1.rate_hw(student2, 'Python', 8)
reviewer2.rate_hw(student1, 'Python', 6)
reviewer2.rate_hw(student2, 'Python', 6)

print('Аспиранты')
print('---------')
print(reviewer1)
print(reviewer2, end='')
print('======================================================================\n')
print('Лекторы')
print('-------')
print(lecturer1)
print(lecturer2)
print(f'Средняя оценка первого и второго лектора равны: {lecturer1 == lecturer2}')
print(f'Средняя оценка первого и второго лектора неравны: {lecturer1 != lecturer2}')
print(f'Средняя оценка первого лектора меньше второго: {lecturer1 < lecturer2}')
print(f'Средняя оценка первого лектора больше второго: {lecturer1 > lecturer2}')
print(f'Средняя оценка первого лектора меньше или равно второго: {lecturer1 <= lecturer2}')
print(f'Средняя оценка первого лектора больше или равно второго: {lecturer1 >= lecturer2}')
print('======================================================================\n')
print('Студенты')
print('--------')
print(student1)
print(student2)
print(f'Средняя оценка первого и второго студента равны: {student1 == student2}')
print(f'Средняя оценка первого и второго студента неравны: {student1 != student2}')
print(f'Средняя оценка первого студента меньше второго: {student1 < student2}')
print(f'Средняя оценка первого студента больше второго: {student1 > student2}')
print(f'Средняя оценка первого студента меньше или равно второго: {student1 <= student2}')
print(f'Средняя оценка первого студента больше или равно второго: {student1 >= student2}')
print('======================================================================\n')
print('Средние оценки\n')
print(f'Средняя оценка за домашние задания по всем студентам: '
      f'{avg_all_students(student1, student2)}')
print(f'Средняя оценка за лекции всех лекторов: '
      f'{avg_all_lecturers(lecturer1, lecturer2)}')
