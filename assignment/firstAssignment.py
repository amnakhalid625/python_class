class User:
    def __init__(self,name, email, gender, user_id):
        self.name=name
        self.email=email
        self.gender=gender
        self.user_id=user_id
        
        
class Student(User):
    def __init__(self,name,email,gender,user_id,roll_no, semester,enrolled_course,grades):
        super().__init__(name,email,gender,user_id)
        self.roll_no=roll_no
        self.semester=semester
        self.enrolled_course=enrolled_course
        self.grades=grades
    
    def enroll(self,course):
        pass

    def view_grades(self):
        pass
    def generate_report(self):
        print(f"Student Report: {self.name} (Roll No: {self.roll_no})")
    
     

class Teacher(User): 
    def __init__(self,name, email, gender, user_id,employee_id, department, assigned_courses_list):
        
         super().__init__(name,email,gender,user_id)
         self.employee_id=employee_id
         self.department=department
         self.assigned_courses_list=assigned_courses_list
         
        
        
    def assign_grade(self,student, course, grade):
        pass
    def generate_report(self):
        print(f"Teacher Report: {self.name} (Employee ID: {self.employee_id})")

        
        
class Course:
    def __init__(self,course_code,title,credit_hours, teacher,student_list):
          self.course_code=course_code
          self.title=title
          self.credit_hours=credit_hours
          self.teacher=teacher
          self.student_list=student_list
          
          
def print_report(user):
        user.generate_report()
        
student=Student('ali','ali@gmail.com','male',12,160,2,['cs'], {'CS101': 'A'})
teacher =Teacher("Mam Amna", "amna@gmail.com", "Female", 2, "T001", "CS", [])


#    def register_sstu


# polymorphism in action

print_report(student)
print_report(teacher)


#  Create a Department class that contains teachers, students, and courses (use composition here)
class Department:
     def __init__(self):
       self.teachers =[]
       self.students =[]
       self.courses =[]


# Create department
obj=Department()

teacher1 = Teacher("Mam Amna", "amna@gmail.com", "Female", 2, "T001", "CS", [])
obj.teachers.append(teacher1)


student1=Student('ali','ali@gmail.com','male',12,160,2,['cs'], {'CS101': 'A'})
obj.students.append(student1)

course1=Course('cs101','cs',3,teacher1,[student1])
obj.courses.append(course1)


class University:
    def __init__(self):
        self.departments = []
obj2=University()


obj2.departments.append(obj)





