input_list = input("Enter your Numbers : ")
input_list = input_list.split(" ")
num_list = [int(n) for n in input_list]


def add(num_list): 

    sum=0
    for i in num_list:
        sum += i
    return sum

print(f"{add(num_list)}")