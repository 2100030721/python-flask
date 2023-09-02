#program to demonstarte single inheritence
class Base:
    def abc(self):
        print("Base class")

class Derived(Base):
    def abc2(self):
        print("Derived class")

ob=Derived()
ob.abc()
ob.abc2()
