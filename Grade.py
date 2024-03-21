#Grade_book mannager 
#Assest_mannager 
#assignment of OOP Python 

class GradeBook:
    def __init__(self):
        self.students = {}

#using function and class self 

    def add_student(self, name):
        if name not in self.students:
            self.students[name] = []

    def add_grade(self, name, grade):
        if name in self.students:
            self.students[name].append(grade)
        else:
            print("Student not found.")

    def calculate_average_grade(self, name):
        if name in self.students:
            grades = self.students[name]
            if grades:
                return sum(grades) / len(grades)
            else:
                return 0
        else:
            print("Student not found.")
            return None

    def display_grade_book(self):
        print("Grade Book:")
        for name, grades in self.students.items():
            average_grade = self.calculate_average_grade(name)
            print(f"{name}: Grades - {grades}, Average Grade - {average_grade}")


# Example usage:
grade_book = GradeBook()

# Adding students
grade_book.add_student("Usman")
grade_book.add_student("Faisal")
grade_book.add_student("Noman")
grade_book.add_student("Zaeem")

# Adding grades
grade_book.add_grade("Usman", 85)
grade_book.add_grade("Usman", 90)
grade_book.add_grade("Faisal", 75)
grade_book.add_grade("Noman", 80)
grade_book.add_grade("Noman", 88)
grade_book.add_grade("Zaeem",90)
grade_book.add_grade("Zaeem",81)

# Displaying grade book of above list
grade_book.display_grade_book()
#program finish with zero error