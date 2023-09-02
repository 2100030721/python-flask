list = [1,2,3,4,5,6,7,8,9,10]
print('List before swapping first and last element ',list)
t=list[0]
list[0]=list[len(list)-1]
list[len(list)-1]=t
print('List after swapping first and last element ',list)
