#program to demonstarte multiple inheritence
class Base1:
    def abc1(self):
        print("Base1 class")
class Base2:
    def abc2(self):
        print("Base2 class")
class Base3:
    def abc3(self):
        print("Base3 class")

class Derived(Base1,Base2,Base3):
    def abc4(self):
        print("Derived class")


ob=Derived()
ob.abc1()
ob.abc2()
ob.abc3()
ob.abc4()
