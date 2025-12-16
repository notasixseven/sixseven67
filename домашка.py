class Student:
    all_students = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.all_students.append(self)

    @classmethod
    def get_average_grade_by_course(cls, course):
        all_grades = []
        for student in cls.all_students:
            if course in student.grades:
                all_grades.extend(student.grades[course])
        if all_grades:
            return round(sum(all_grades) / len(all_grades), 2)
        return 0.0

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if 1 <= grade <= 10:
                if course in lecturer.grades:
                    lecturer.grades[course].append(grade)
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return 'Ошибка'

    def grades_avg(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades.extend(grades)
        if all_grades:
            return round(sum(all_grades) / len(all_grades), 2)
        return 0.0

    def __str__(self):
        stud_info = (f"Имя: {self.name}\n"
                     f"Фамилия: {self.surname}\n"
                     f"Средняя оценка за домашние задания: {self.grades_avg()}\n"
                     f"Курсы в процессе изучения: {', '.join(self.courses_in_progress) if self.courses_in_progress else 'нет'}\n"
                     f"Завершенные курсы: {', '.join(self.finished_courses) if self.finished_courses else 'нет'}")
        return stud_info

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.grades_avg() < other.grades_avg()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.grades_avg() > other.grades_avg()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.grades_avg() == other.grades_avg()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if 1 <= grade <= 10:
                if course in student.grades:
                    student.grades[course].append(grade)
                else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    all_lecturers = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.all_lecturers.append(self)

    @classmethod
    def get_average_grade_by_course(cls, course):
        all_grades = []
        for lecturer in cls.all_lecturers:
            if course in lecturer.grades:
                all_grades.extend(lecturer.grades[course])
        if all_grades:
            return round(sum(all_grades) / len(all_grades), 2)
        return 0.0

    def avg_grade(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades.extend(grades)
        if all_grades:
            return round(sum(all_grades) / len(all_grades), 2)
        return 0.0

    def __str__(self):
        lec_info = (f"Имя: {self.name}\n"
                    f"Фамилия: {self.surname}\n"
                    f"Средняя оценка за лекции: {self.avg_grade()}")
        return lec_info

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.avg_grade() < other.avg_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.avg_grade() > other.avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.avg_grade() == other.avg_grade()


class Reviewer(Mentor):
    def __str__(self):
        rev_info = (f"Имя: {self.name}\n"
                    f"Фамилия: {self.surname}")
        return rev_info




student1 = Student('Sage', 'Pork', 'male')
student2 = Student('Cristiana', 'Ranalda', 'male')
lecturer1 = Lecturer('Charlie', 'Jackson')
lecturer2 = Lecturer('John', 'Shola')
reviewer1 = Reviewer('George', 'Sabaev')
reviewer2 = Reviewer('Piter', 'Poter')


student1.courses_in_progress.extend(['c++', 'Python'])
student2.courses_in_progress.extend(['c++', 'Java'])
student1.finished_courses.append('Введение в программирование')



lecturer1.courses_attached.extend(['c++', 'Python'])
lecturer2.courses_attached.extend(['c++', 'Java'])


student1.rate_lec(lecturer1, 'c++', 9)
student1.rate_lec(lecturer1, 'c++', 8)
student2.rate_lec(lecturer1, 'c++', 10)

student1.rate_lec(lecturer2, 'c++', 7)
student2.rate_lec(lecturer2, 'c++', 6)
student2.rate_lec(lecturer2, 'c++', 8)





reviewer1.courses_attached.extend(['c++', 'Python'])
reviewer2.courses_attached.extend(['c++', 'Java'])


reviewer1.rate_hw(student1, 'c++', 9)
reviewer1.rate_hw(student1, 'c++', 8)
reviewer1.rate_hw(student2, 'c++', 7)
reviewer1.rate_hw(student2, 'c++', 6)

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)

reviewer2.rate_hw(student2, 'Java', 8)
reviewer2.rate_hw(student2, 'Java', 7)

print(Student.get_average_grade_by_course('c++'))
print(Lecturer.get_average_grade_by_course('c++'))