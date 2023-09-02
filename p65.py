class Base:
    def abc(self):
        print("Hello")

class Derived(Base):
    def abc(self):
        print("Good Evening")

ob=Derived()
ob.abc()
