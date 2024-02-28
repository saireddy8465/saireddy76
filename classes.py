class Student:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
    def StudentWork(self):
        if(self.department=="CSE"):
            print("He works on software")
        else:
            print("He works on Hardwork")
a=Student('sai',22,'CSE')
a.StudentWork()
print(a.name)
print(a.age)
print(a.department)
b=Student('raju',21,'ECE')
b.StudentWork()
print(b.name)
print(b.age)
print(b.department)

        
   
