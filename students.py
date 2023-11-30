# define the student class
class Student:
# define the student class
  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade
# method to display the student information
  def display_info(self):
    print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")
# example usage:
# create a instance and display the student information
student1 = Student("Mishma", 20, "A+++")
student1.display_info()







