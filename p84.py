import csv

with open('studentDetails.csv',mode='r') as f:
    det=csv.reader(f)

    for i in det:
        print(i)
