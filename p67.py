class Student:
     def __init__(self,id,name,cgpa):
         self.id=id
         self.name=name
         self.cgpa=cgpa
s1=Student(101,"abc",9.1)
print(getattr(s1,'cgpa'))
setattr(s1,'cgpa',9.3)
print(getattr(s1,'cgpa'))
delattr(s1,'id')
print(hasattr(s1,'id'))
