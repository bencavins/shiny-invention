import random


class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major
        self.grades = []

    def calc_gpa(self):
        return sum(self.grades) / len(self.grades)
    
    def __repr__(self):
        return f'<Student: {self.name}, {self.major}>'


class BloomtechStudent(Student):
    def __init__(self, name, major, prog_lang='python'):
        super().__init__(name, major)
        self.prog_lang = prog_lang

    def flex(self):
        print(f'student {self.name} flexed this class')


def student_generator():
    random_students = []
    names = ['joe', 'anne', 'bob', 'sally']
    majors = ['comp sci', 'polisci', 'math', 'art history']
    for x in range(30):
        student = Student(random.choice(names), random.choice(majors))
        student.grades.append(random.uniform(0.0, 4.0))
        student.grades.append(random.uniform(0.0, 4.0))
        student.grades.append(random.uniform(0.0, 4.0))
        random_students.append(student)
    return random_students


if __name__ == '__main__':
    student_list = student_generator()
    for student in student_list:
        print(student.calc_gpa())