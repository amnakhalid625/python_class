class User:
    def __init__(self, name, email, gender, user_id):
        self.name = name
        self.email = email
        self.gender = gender
        self.user_id = user_id

    def generate_report(self):
        raise NotImplementedError("Subclasses must implement generate_report")


class Student(User):
    def __init__(self, name, email, gender, user_id, roll_no, semester, enrolled_course, grades):
        super().__init__(name, email, gender, user_id)
        self.roll_no = roll_no
        self.semester = semester
        self.enrolled_course = enrolled_course
        self.grades = grades

    def enroll(self, course):
        pass

    def view_grades(self):
        pass

    def generate_report(self):
        print(f"Student Report: {self.name} (Roll No: {self.roll_no})")


class Teacher(User):
    def __init__(self, name, email, gender, user_id, employee_id, department, assigned_courses_list):
        super().__init__(name, email, gender, user_id)
        self.employee_id = employee_id
        self.department = department
        self.assigned_courses_list = assigned_courses_list

    def assign_grade(self, student, course, grade):
        pass

    def generate_report(self):
        print(f"Teacher Report: {self.name} (Employee ID: {self.employee_id})")


class Course:
    def __init__(self, course_code, title, credit_hours, teacher, student_list):
        self.course_code = course_code
        self.title = title
        self.credit_hours = credit_hours
        self.teacher = teacher
        self.student_list = student_list

    def show_summary(self):
        print(f"\n Course Title: {self.title}")
        print(f" Course Code: {self.course_code}")
        print(f"Credit Hours: {self.credit_hours}")
        print(f"Teacher: {self.teacher.name} ({self.teacher.email})")
        print("Enrolled Students:")
        if self.student_list:
            for student in self.student_list:
                print(f" - {student.name} (Roll No: {student.roll_no})")
        else:
            print(" No students enrolled yet.")


def print_report(user):
    user.generate_report()


class Department:
    def __init__(self):
        self.teachers = []
        self.students = []
        self.courses = []


class University:
    def __init__(self):
        self.departments = []

    def register_student(self, department, student):
        if student not in department.students:
            department.students.append(student)

    def hire_teacher(self, teacher, department):
        if teacher not in department.teachers:
            department.teachers.append(teacher)

    def add_department(self, department):
        if department not in self.departments:
            self.departments.append(department)

    def enroll_student_in_course(self, student, course):
        if student not in course.student_list:
            course.student_list.append(student)
        if course.title not in student.enrolled_course:
            student.enrolled_course.append(course.title)


# Sample Data

# Teachers
teacher1 = Teacher("Mam Amna", "amna@gmail.com", "Female", 2, "T001", "CS", [])
teacher2 = Teacher("Sir Asim", "asim@gmail.com", "Male", 3, "T002", "IT", [])

# Students
student1 = Student("Ali", "ali@gmail.com", "Male", 12, 160, 2, [], {})
student2 = Student("Sara", "sara@gmail.com", "Female", 13, 161, 2, [], {})
student3 = Student("Zain","zain@gmail.com", "Male", 14, 162, 2, [], {})

# Courses
course1 = Course("CS101", "Intro to CS", 3, teacher1, [student1])
course2 = Course("CS102", "Data Structures", 3, teacher1, [student2])
course3 = Course("IT201", "Networking", 3, teacher2, [student3])

# Departments
dept1 = Department()
dept2 = Department()

# Add data to departments

# Department 1
dept1.teachers.append(teacher1)
dept1.students.extend([student1, student2])
dept1.courses.extend([course1, course2])

# Department 2
dept2.teachers.append(teacher2)
dept2.students.append(student3)
dept2.courses.append(course3)

# University
univ = University()
univ.add_department(dept1)
univ.add_department(dept2)

# Polymorphism Test
all_people = [student1, student2, student3, teacher1, teacher2]
for person in all_people:
    print_report(person)

# Show course summaries
for course in dept1.courses + dept2.courses:
    course.show_summary()


