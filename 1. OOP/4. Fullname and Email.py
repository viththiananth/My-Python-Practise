class Employee:
    def __init__(self,firstname,lastname):
        self.firstname=firstname.lower().capitalize()
        self.lastname=lastname.lower().capitalize()
        self.fullname=self.firstname+" "+self.lastname
        self.email=self.firstname.lower()+"."+self.lastname.lower()+"@company.com"


emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")

print(emp_1.fullname)
print(emp_2.email)
print(emp_3.firstname)