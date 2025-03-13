def add(list):
    sum=0
    for i in list:
        sum=sum+i
    return sum

list=[]
size=int(input("Enter the size of the list : "))

for j in range(size):
    num=int(input("Enter the number : "))
    list.append(num)
print("Sum of the list is : ",add(list))