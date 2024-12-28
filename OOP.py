class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def lec_rate(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.lec_grade:
                lector.lec_grade[course] += [grade]
            else:
                lector.lec_grade[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        x = 0
        for i in self.grades.values():
            x += sum(i)
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {x / len(self.grades)}\n'
                f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {', '.join(self.finished_courses)}')

    def __gt__(self, other):
        avg = sum([sum(i) for i in self.grades.values()]) / len(self.grades)
        avg_2 = sum([sum(i) for i in other.grades.values()]) / len(other.grades)
        if avg > avg_2:
            return "Best of the best"
        else:
            return "Not today"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lec_grade = {}

    def __str__(self):
        x = 0
        for i in self.lec_grade.values():
            x += sum(i)
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {sum([sum(i) for i in self.lec_grade.values()]) / len(self.lec_grade)}'

    def __gt__(self, other):
        avg = sum([sum(i) for i in self.lec_grade.values()]) / len(self.lec_grade)
        avg_2 = sum([sum(i) for i in other.lec_grade.values()]) / len(other.lec_grade)
        if avg > avg_2:
            return "Best of the best"
        else:
            return "Not today"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'



def st_marks(course, *stud):
    c = 0
    for i in stud:
        for k, v in i.grades.items():
            if k == course:
                c += sum([i for i in v])

    return c / len(stud)


def lec_marks(course, *lec):
    c = 0
    for i in lec:
        for k, v in i.lec_grade.items():
            if k == course:
                c += sum([i for i in v])

    return c / len(lec)



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.add_courses('Java')

not_bs = Student('Hot', 'Rain', 'male')
not_bs.courses_in_progress += ['Python']
not_bs.courses_in_progress += ['Java']
not_bs.add_courses('C++')

cool_rev = Reviewer('Some', 'Buddy')
cool_rev.courses_attached += ['Python']
cool_rev.courses_attached += ['Java']
cool_rev.rate_hw(best_student, 'Python', 10)
cool_rev.rate_hw(best_student, 'Java', 6)

cool_rev_2 = Reviewer('Any', 'Buddy')
cool_rev_2.courses_attached += ['Python']
cool_rev_2.courses_attached += ['Java']
cool_rev_2.rate_hw(not_bs, 'Python', 6)
cool_rev_2.rate_hw(not_bs, 'Java', 3)


cool_lector = Lecturer('Jon', 'Bon')
cool_lector.courses_attached += ['Java']
cool_lector.courses_attached += ['C++']

cool_lector_2 = Lecturer('Don', 'Jon')
cool_lector_2.courses_attached += ['Java']
cool_lector_2.courses_attached += ['C++']

best_student.courses_in_progress += ['C++']
not_bs.courses_in_progress += ['C++']

best_student.lec_rate(cool_lector, 'Java', 8)
best_student.lec_rate(cool_lector, 'C++', 4)

not_bs.lec_rate(cool_lector_2, 'Java', 4)
not_bs.lec_rate(cool_lector_2, 'C++', 9)

print(best_student)
print(not_bs)
print(cool_lector)
print(cool_lector_2)
print(cool_rev_2)
print(cool_rev)
print(cool_lector > cool_lector_2)
print(best_student > not_bs)

print(st_marks('Python', best_student, not_bs))
print(lec_marks('C++', cool_lector, cool_lector_2))