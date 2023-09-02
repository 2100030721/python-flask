try:
    a=input()
    b=input()
    c=a/b
except:
    print("An Exception Occured - ZeroDivision")
else:
    print("Exception not occured")
finally:
    print("Succesfull")
