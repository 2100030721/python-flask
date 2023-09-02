import csv

fh=open("studentDetails.csv","r")
re=csv.reader(fh)
s=[ ]
r=int(input("Enter roll number to Delete....."))
found=False
for row in re:
    if row[0]==str(r):
        found=True
    else:
        s.append(row)
fh.close()
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
fh.close()
