class Student:
    def __init__(self, student_id, name, marks, age, fee_paid):
        self.student_id = student_id
        self.name = name
        self.marks = marks
        self.age = age
        self.fee_paid = fee_paid
        self.total_fee = 50000

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def calculate_cgpa(self):
        avg = self.calculate_average()
        return avg / 10

    def fee_balance(self):
        return self.total_fee - self.fee_paid


class College:
    def __init__(self, code, name, location):
        self.code = code
        self.name = name
        self.location = location
        self.students = []

    def register_student(self, student):
        self.students.append(student)

    def display_details(self):
        print("College Code:", self.code)
        print("College Name:", self.name)
        print("Location:", self.location)
        print("\nStudent Details:")

        for s in self.students:
            print("\nID:", s.student_id)
            print("Name:", s.name)
            print("Average:", s.calculate_average())
            print("CGPA:", s.calculate_cgpa())
            print("Age:", s.age)
            print("Fee Balance:", s.fee_balance())


college = College("ANITS01", "ANITS", "Visakhapatnam")

s1 = Student(1, "Rahul", [80, 85, 78], 20, 30000)
s2 = Student(2, "Priya", [90, 88, 92], 21, 40000)
s3 = Student(3, "Arjun", [70, 75, 72], 20, 25000)

college.register_student(s1)
college.register_student(s2)
college.register_student(s3)

college.display_details()
