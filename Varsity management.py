class Person:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

class Student(Person):
    def __init__(self, name, ID, CGPA):
        super().__init__(name, ID)
        self.CGPA = CGPA

    def calculate_tuition_fee(self, base_fee):
        if self.CGPA > 3.75:
            return base_fee * 0.75
        elif self.CGPA > 3.5:
            return base_fee * 0.8
        else:
            return base_fee

class Administrator(Person):
    def __init__(self, name, ID, department):
        super().__init__(name, ID)
        self.department = department

    def display_info(self):
        print(f"Administrator {self.name} works in {self.department} department.")

# Example usage:
student1 = Student("Alice", 123, 3.8)
print(f"Tuition fee after waiver: ${student1.calculate_tuition_fee(10000):.2f}")

admin1 = Administrator("Bob", 456, "Finance")
admin1.display_info()
