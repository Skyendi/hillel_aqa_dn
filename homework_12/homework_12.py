class Student:
    def __init__(self, first_name, second_name, age, average_grade):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.average_grade = average_grade

    def update_grade(self, new_grade):
        self.average_grade = new_grade

    def show_info(self):
        print(f"Name - {self.first_name}")
        print(f"second_name - {self.second_name}")
        print(f"age - {self.age}")
        print(f"average_grade - {self.average_grade}")


