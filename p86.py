import csv
 
fh=open("studentDetails.csv","r")
re=csv.reader(fh)
s=[ ]
r=input("Enter roll number to Update.....")
found=False
for row in re:
    if row[0]==str(r):
        found=True
        marks=input("ENTER Name to change...")
        row[1]=marks
    s.append(row)
fh.close( )
if found==False:
    print("Student does not exists..")
else:
    fh=open("studentDetails.csv","w+",newline='')
    wr=csv.writer(fh)
    wr.writerows(s)
    fh.seek(0)
    re=csv.reader(fh)
    for row in re:
        print(row)
fh.close( )
