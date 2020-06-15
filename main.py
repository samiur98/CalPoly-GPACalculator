from typing import List


class Course:
    # Class that contains information about a particular course.
    def __init__(self):
        self.name: str = ""
        self.grade: float = 0.0
        self.units: int = 0

    # Getters and Setters

    def get_name(self) -> str:
        return self.name

    def get_grade(self) -> float:
        return self.grade

    def get_units(self) -> int:
        return self.units

    def set_name(self, name: str) -> None:
        self.name = name

    def set_grade(self, grade: float) -> None:
        self.grade = grade

    def set_units(self, units: int) -> None:
        self.units = units

    # Redefining __str__

    def __str__(self):
        result: str = ""
        result = result + "Name: "
        result = result + self.name
        result = result + "\n"
        result = result + "Grade: "
        result = result + str(self.grade)
        result = result + "\n"
        result = result + "Units: "
        result = result + str(self.units)
        return result


def main() -> None:
    # Main method that runs the program.
    print_welcome_message()
    course_list: List[Course] = []
    cmd: str = ""
    while cmd is not "Q":
        cmd = input()
        if cmd is "A":
            course: Course = a_command()
            course_list.append(course)
        elif cmd is "U":
            u_command(course_list)
        elif cmd is "D":
            d_command(course_list)
        elif cmd is "C":
            c_command(course_list)
        elif cmd is "P":
            p_command(course_list)
        elif cmd is "Q":
            print("Thank-you, Good bye and Good Luck!")
        else:
            print("Invalid Command\n")
            print_commands_message()


def print_welcome_message() -> None:
    # Prints the welcome message for the user.

    print("Welcome to the CalPoly SLO GPA Calculator")
    print("This is a simple tool that lets you calculate your GPA,"
          " based on the classes you have taken and the letter grade you have"
          " received in those classes")
    print("This can be a useful tool to predict what grade/s you should aim"
          " for when taking a class")
    print("\n")
    print_commands_message()


def print_commands_message() -> None:
    # Prints a list of available commands for the user.

    print("Please enter one of the following commands:")
    print("A - Add course")
    print("U - Update course")
    print("D - Delete course")
    print("C - Calculate GPA")
    print("P - Print Entered Courses")
    print("Q - Quit")


def print_grades_message() -> None:
    # Prints a list of available letter grade options
    print("Please enter one of the following letter grades: A, A-, "
          "B+, B, B-, C+, C, C-, D+, D, D-, F")


def grade_prompt() -> float:
    # Prompts user for grade and returns the corresponding float value.
    while True:
        print_grades_message()
        grade: str = input()
        if grade == "A":
            return 4.0
        elif grade == "A-":
            return 3.7
        elif grade == "B+":
            return 3.3
        elif grade == "B":
            return 3.0
        elif grade == "B-":
            return 2.7
        elif grade == "C+":
            return 2.3
        elif grade == "C":
            return 2.0
        elif grade == "C-":
            return 1.7
        elif grade == "D+":
            return 1.3
        elif grade == "D":
            return 1.0
        elif grade == "D-":
            return 0.7
        elif grade == "F":
            return 0.0
        else:
            print("Invalid Option")


def revert_grade(grade: float) -> str:
    # Converts float grade value to string letter grade representation.
    if grade >= 4.0:
        return "A"
    elif grade >= 3.7:
        return "A-"
    elif grade >= 3.3:
        return "B+"
    elif grade >= 3.0:
        return "B"
    elif grade >= 2.7:
        return "B-"
    elif grade >= 2.3:
        return "C+"
    elif grade >= 2.0:
        return "C"
    elif grade >= 1.7:
        return "C-"
    elif grade >= 1.3:
        return "D+"
    elif grade >= 1.0:
        return "D"
    elif grade >= 0.7:
        return "D-"
    else:
        return "F"


def a_command() -> Course:
    # Handles adding a new course.
    course: Course = Course()
    name: str = input("Please Enter the Name of the Course: ")
    units: int = 0
    while True:
        try:
            units = int(input("Please Enter the Units of the Course: "))
            break
        except ValueError:
            print("Please enter a valid integer")
    print("Please enter a letter grade from the following options: ")
    grade: float = grade_prompt()
    course.set_name(name)
    course.set_units(units)
    course.set_grade(grade)
    print(name + " was added.")
    return course


def u_command(course_list: List[Course]) -> None:
    # Handles updating an existing course.
    course_name: str = input("Please enter the course name: ")
    success: bool = False
    for course in course_list:
        if course.get_name() == course_name:
            success = True
            print("Do you wish to update the units of the course?")
            unit_option: str = input("Enter Y for YES and N for NO: ")
            if unit_option == "Y":
                while True:
                    try:
                        new_unit: int = int(input("New Value for Units: "))
                        course.set_units(new_unit)
                        break
                    except ValueError:
                        print("Please enter a valid float value")
            print("Do you wish to update the grade of the course?")
            grade_option: str = input("Enter Y for YES and N for No: ")
            if grade_option == "Y":
                new_grade: float = grade_prompt()
                course.set_grade(new_grade)
    if success:
        print(course_name + " has been updated")
    else:
        print(course_name + " could not be found and updated")


def d_command(course_list: List[Course]) -> None:
    # Handles deleting an existing course.
    success: bool = False
    course_name: str = input("Please enter the course name to be deleted: ")
    for course in course_list:
        if course.get_name() == course_name:
            success = True
            course_list.remove(course)
            break
    if success:
        print(course_name + " has been successfully deleted")
    else:
        print(course_name + " could not be found and deleted")


def c_command(course_list: List[Course]) -> None:
    # Calculates and outputs GPA
    if len(course_list) == 0:
        print("No courses added, GPA could not be calculated.")
    else:
        total_grades: float = 0.0
        total_units: float = 0.0
        for course in course_list:
            total_grades = total_grades + (course.get_grade() * float(course.get_units()))
            total_units = total_units + float(course.get_units())
        gpa: float = total_grades/total_units
        print("Your Cumulative GPA: " + str(gpa))



def p_command(course_list: List[Course]) -> None:
    # Prints the courses that have been added along with info about the courses
    i: int = 1
    if len(course_list) == 0:
        print("No Courses added.")
    else:
        for course in course_list:
            entry: str = "#" + str(i)
            entry = entry + " Name: " + course.get_name()
            entry = entry + " Units: " + str(course.get_units())
            entry = entry + " Grade: " + revert_grade(course.get_grade())
            print(entry)
            i = i + 1


if __name__ == "__main__":
    main()

