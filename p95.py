def isArms(x):
    a=x
    sum=0
    digit=0
    while a!=0:
        digit+=1
        a//=10
    a=x
    while a!=0:
        n=a%10
        sum=sum+(pow(n,digit))
        a//=10
    if sum==x:
        print("Armstrong")
    else:
        print("Not Armstrong")
isArms(int(input()))

