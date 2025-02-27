list = input("Enter your Numbers : ")
list = list.split(" ")
num_list = [int(n) for n in list]
length = len(num_list)

def add(num_list, length):
    if length < 0:
     return 0
    return num_list[length - 1] + add(num_list, length-1)

print(f"{add(num_list, length)}")