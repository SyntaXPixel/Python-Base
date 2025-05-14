input_list = input("Enter your Numbers : ")
input_list = input_list.split(" ")
num_list = [int(n) for n in input_list]

num_list.sort()
print(num_list)
