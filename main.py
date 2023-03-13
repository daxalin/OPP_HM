class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def ended_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def get_average(self, grades):
        if grades:
            sum_of_grade = 0
            amount_of_grades = 0
            for grade in grades.values():
                sum_of_grade += sum(grade)
                amount_of_grades += len(grade)
            return round(sum_of_grade / amount_of_grades, 1)
        else:
            return 0

    def __str__(self):
        res = (f"Имя: {self.name}\nФамилия: {self.surname}\n"
               f"Средняя оценка за домашние задания: {self.get_average(self.grades)}\n"
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
               f"Завершенные курсы: {', '.join(self.finished_courses)}")
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a student')
            return
        return self.get_average(self.grades) < other.get_average(other.grades)

    def __le__(self, other):
        if not isinstance(other, Student):
            print('Not a student')
            return
        return self.get_average(self.grades) <= other.get_average(other.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average(self, grades):
        if grades:
            sum_of_grade = 0
            amount_of_grades = 0
            for grade in grades.values():
                sum_of_grade += sum(grade)
                amount_of_grades += len(grade)
            return round(sum_of_grade / amount_of_grades, 1)
        else:
            return 0

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_average(self.grades)}"
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a lecturer')
            return
        return self.get_average(self.grades) < other.get_average(other.grades)

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a lecturer')
            return
        return self.get_average(self.grades) <= other.get_average(other.grades)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}"
        return res


def average_grade_in_subject(class_name, course):
    list_instances = [_ for _ in globals().values() if isinstance(_, class_name)]
    list_grades = [_.grades[course] for _ in list_instances if course in _.grades.keys()]
    average_grade = sum([sum(i) for i in list_grades]) / sum([len(i) for i in list_grades])
    return f'Средняя оценка среди {class_name.__name__} по предмету {course} - {average_grade}'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Java', 'Math']
best_student.ended_courses("English")

the_boy = Student('Harry', 'Potter', 'male')
the_boy.courses_in_progress += ['Python', 'Java']
the_boy.ended_courses('Math')

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

the_best_mentor = Reviewer('Hermiona', 'Ride')
the_best_mentor.courses_attached += ['Java', 'Math']

nice_lecturer = Lecturer("Pia", "Hide")
nice_lecturer.courses_attached += ["Java", 'Python']

good_lecturer = Lecturer("Sveta", "Koneva")
good_lecturer.courses_attached += ["Math", 'Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
the_best_mentor.rate_hw(best_student, 'Java', 8)
cool_mentor.rate_hw(the_boy, 'Python', 7)
the_best_mentor.rate_hw(the_boy, 'Java', 10)

best_student.rate_lec(nice_lecturer, "Java", 9)
best_student.rate_lec(nice_lecturer, "Python", 10)
best_student.rate_lec(good_lecturer, "Math", 3)
best_student.rate_lec(good_lecturer, "Python", 4)


print(nice_lecturer)
print()
print(good_lecturer)
print()
print(best_student)
print()
print(the_boy)
print()
print(cool_mentor)
print()
print(the_best_mentor)
print()
print(best_student < the_boy)
print(best_student > the_boy)
print(best_student >= the_boy)
print(the_boy >= best_student)

print(nice_lecturer >= good_lecturer)
print(nice_lecturer < good_lecturer)
print(average_grade_in_subject(Student, 'Python'))
print(average_grade_in_subject(Lecturer, 'Python'))