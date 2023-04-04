import datetime

class Student:
    def __init__(self, student_num, first_name, last_name, dob, sex, country):
        self.__student_num = student_num
        self.__first_name = first_name
        self.__last_name = last_name
        self.__dob = dob
        self.__sex = sex
        self.__country = country
    
    # Getter methods
    def get_student_num(self):
        return self.__student_num

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_dob(self):
        return self.__dob

    def get_sex(self):
        return self.__sex

    def get_country(self):
        return self.__country

    # Setter methods
    def set_student_num(self, student_num):
        self.__student_num = student_num

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_dob(self, dob):
        self.__dob = dob

    def set_sex(self, sex):
        self.__sex = sex

    def set_country(self, country):
        self.__country = country

    # Method to calculate age
    def age(self):
        today = datetime.date.today()
        return today.year - self.__dob.year - ((today.month, today.day) < (self.__dob.month, self.__dob.day))

def write_to_file(students):
    with open("students.txt", "w") as f:
        for student in students:
            f.write(f"{student.get_student_num()}|{student.get_first_name()}|{student.get_last_name()}|{student.get_dob()}|{student.get_sex()}|{student.get_country()}\n")

def read_from_file():
    students = []
    with open("students.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            parts = line.split("|")
            student_num = int(parts[0])
            first_name = parts[1]
            last_name = parts[2]
            dob = datetime.datetime.strptime(parts[3].strip(), "%Y-%m-%d").date()
            sex = parts[4]
            country = parts[5].strip()
            student = Student(student_num, first_name, last_name, dob, sex, country)
            students.append(student)
    return students

def add_student(students):
    if len(students) >= 100:
        print("The student array is full.")
        return
    student_num = int(input("Enter student number: "))
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    dob = datetime.datetime.strptime(input("Enter date of birth (YYYY-MM-DD): "), "%Y-%m-%d").date()
    sex = input("Enter sex: ")
    country = input("Enter country of birth: ")
    student = Student(student_num, first_name, last_name, dob, sex, country)
    students.append(student)
    print("Student added.")

def find_student(students):
    student_num = int(input("Enter student number: "))
    for student in students:
        if student.get_student_num() == student_num:
            age = student.age()
            print(f"Student number: {student.get_student_num()}")
            print(f"First name: {student.get_first_name()}")
            print(f"Last name: {student.get_last_name()}")
            print(f"Date of birth: {student.get_dob()}")
            print(f"Sex: {student.get_sex()}")
            print(f"Country of birth: {student.get_country()}")
            print(f"Age: {age}")
            return
    print("Student not found.")

def show_all_students(students):
    for student in students:
        age = student.age()
        print(f"Student number: {student.get_student_num()}")
        print(f"First name: {student.get_first_name()}")
        print(f"Last name: {student.get_last_name()}")
        print(f"Date of birth: {student.get_dob()}")
        print(f"Sex: {student.get_sex()}")
        print(f"Country of birth: {student.get_country()}")
        print(f"Age: {age}")
        print()

def show_students_by_year(students):
    year = int(input("Enter year: "))
    for student in students:
        if student.get_dob().year == year:
            age = student.age()
            print(f"Student number: {student.get_student_num()}")
            print(f"First name: {student.get_first_name()}")
            print(f"Last name: {student.get_last_name()}")
            print(f"Date of birth: {student.get_dob()}")
            print(f"Sex: {student.get_sex()}")
            print(f"Country of birth: {student.get_country()}")
            print(f"Age: {age}")
            print()
        else:
            print("No students found.")

def modify_student_record(students):
    student_num = int(input("Enter student number: "))
    for student in students:
        if student.get_student_num() == student_num:
            field = input("Enter field to modify (student number, first name, last name, dob, sex, country): ")
            if field == "student number":
                new_value = int(input("Enter new student number: "))
                student.set_student_num(new_value)
                print("***successfully saved***")
            elif field == "first name":
                new_value = input("Enter new first name: ")
                student.set_first_name(new_value)
                print("***successfully saved***")
            elif field == "last name":
                new_value = input("Enter new last name: ")
                student.set_last_name(new_value)
                print("***successfully saved***")
            elif field == "dob":
                new_value = datetime.datetime.strptime(input("Enter new date of birth (YYYY-MM-DD): "), "%Y-%m-%d").date()
                student.set_dob(new_value)
                print("***successfully saved***")
            elif field == "sex":
                new_value = input("Enter new sex: ")
                student.set_sex(new_value)
                print("***successfully saved***")
            elif field == "country":
                new_value = input("Enter new country of birth: ")
                student.set_country(new_value)
                print("***successfully saved***")
            else:
                print("Invalid field.")
                return
            print("Record modified.")
            return
    print("Student not found.")

def delete_student(students):
    student_num = int(input("Enter student number: "))
    for student in students:
        if student.get_student_num() == student_num:
            students.remove(student)
            print("Student deleted.")
            return
    print("Student not found.")

students = []
while True:
    print("1. Write contents of student array to file")
    print("2. Read student data from file and populate student array")
    print("3. Add a new student")
    print("4. Find a student by student number")
    print("5. Show all students")
    print("6. Show all students born in a given year")
    print("7. Modify a student record")
    print("8. Delete a student")
    print("9. Quit")
    choice = input("Enter choice: ")
    if choice == "1":
        write_to_file(students)
    elif choice == "2":
        students = read_from_file()
    elif choice == "3":
        add_student(students)
    elif choice == "4":
        find_student(students)
    elif choice == "5":
        show_all_students(students)
    elif choice == "6":
        show_students_by_year(students)
    elif choice == "7":
        modify_student_record(students)
    elif choice == "8":
        delete_student(students)
    elif choice == "9":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")

