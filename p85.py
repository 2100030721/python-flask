from csv import writer
          
def f_CSVwrite():
    
    f = open("studentDetails.csv","a")
    r = input("Enter ID:")
    b = input("Enter  name:")
    t = input("Enter SCGPA:")
    rt =input("Enter CGPA:")
    dt = writer(f)
    dt.writerow([r,b,t,rt])
    print("Record has been added.")
    f.close()
               
f_CSVwrite() 
