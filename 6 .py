class Gradebook:
    def __init__(self):
        self.students = {}

    def add_student(self, student_name):
        if student_name not in self.students:
            self.students[student_name] = {}
        else:
            print(f"Student {student_name} already exists.")

    def add_grade(self, student_name, subject, grade):
        if student_name in self.students:
            if subject in self.students[student_name]:
                self.students[student_name][subject].append(grade)
            else:
                self.students[student_name][subject] = [grade]
        else:
            print(f"Student {student_name} does not exist. Please add the student first.")

    def get_student_grades(self, student_name):
        if student_name in self.students:
            return self.students[student_name]
        else:
            print(f"Student {student_name} does not exist.")
            return None

    def calculate_average_grade(self, student_name):
        if student_name in self.students:
            total_grades = 0
            count = 0
            for subject, grades in self.students[student_name].items():
                total_grades += sum(grades)
                count += len(grades)
            if count == 0:
                return 0
            return total_grades / count
        else:
            print(f"Student {student_name} does not exist.")
            return None

    def highest_scoring_student(self):
        highest_avg = -1
        top_student = None
        for student in self.students:
            avg = self.calculate_average_grade(student)
            if avg is not None and avg > highest_avg:
                highest_avg = avg
                top_student = student
        return top_student, highest_avg

# Example usage:
gradebook = Gradebook()
gradebook.add_student("Alice")
gradebook.add_grade("Alice", "Math", 90)
gradebook.add_grade("Alice", "Science", 85)
gradebook.add_grade("Alice", "Math", 95)
print(f"Alice's Grades: {gradebook.get_student_grades('Alice')}")
print(f"Alice's Average Grade: {gradebook.calculate_average_grade('Alice'):.2f}")

gradebook.add_student("Bob")
gradebook.add_grade("Bob", "Math", 20)
gradebook.add_grade("Bob", "Science", 88)
print(f"Bob's Grades: {gradebook.get_student_grades('Bob')}")
print(f"Bob's Average Grade: {gradebook.calculate_average_grade('Bob'):.2f}")

top_student, top_avg = gradebook.highest_scoring_student()
print(f"Highest Scoring Student: {top_student} with an average grade of {top_avg:.2f}")
