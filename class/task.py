# employee mangement syestem with attendance and payroll system


# task description
from datetime import datetime


class Person:
    def __init__(self,dob,name):
        self.dob = dob
        self.name=name

    def get_age(self):
        birth_date=datetime.strptime(self.dob,"%Y-%m-%d")
        today = datetime.today()
        age=today.year - birth_date.year-((today.month,today.day)<(birth_date.month,birth_date.day))
        print(f"{self.name} is {age} year olds.")
obj=Person('1992-07-5','ania')


class Employee(Person):
     def __init__(self, dob, name,employee_id,department,salary):
      super().__init__(dob,name)
      self.employee_id =employee_id
      self.department=department
      self.salary=salary


     def showDeatils(self):
      print(f"Name: {self.name}")
      print(f"DOB: {self.dob}")
      print(f"Employee ID: {self.employee_id}")
      print(f"Department: {self.department}")
      print(f"Salary: {self.salary}")
      
obj2=Employee('1222-01-8','laiba',1,'cs',293992)
obj2.get_age()
obj2.showDeatils()



class Attendence:
   def __init__(self,date):
      self.data=date
      
      
    
          
