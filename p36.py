#program to demonstrate print 1 to 100 prime numbers
 # range function is not count last number (Ending number)
 # only 1 to 100 is counted
 
for i in range(2,101): 
    for j in range(2,101):
        if i%j == 0:
            break
    if i == j:
        print(i,end=",")
