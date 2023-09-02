class Student:
     def __init__(self,id,name,cgpa):
         self.id=id
         self.name=name
         self.cgpa=cgpa
s1=Student(101,"abc",9.1)
print(getattr(s1,'cgpa'))
