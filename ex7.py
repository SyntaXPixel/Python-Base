input_list = input("Enter your Numbers : ")
input_list = input_list.split(" ")
num_list = [int(n) for n in input_list]
length = len(num_list)


def add(num_list_x, length_x): 

    if length_x == 0:
     return 0
    return num_list_x[length_x-1] + add(num_list_x, (length_x-1))

print(f"{add(num_list, length)}")


# input 50 50 50 
# num_list = [50, 50, 50]
# length = 3
# def add([50, 50, 50],3):
# [50, 50, 50] = num_list_x
# length_x = 3
# return num_list_x[length_x-1] + add(num_list_x, (length_x-1))
# return ([50, 50, 50])[2] + add([50, 50, 50],2)

# [50, 50, 50] = num_list_x
# length_x = 1
# if length_x == 0:
# return num_list_x[length_x-1] + add(num_list_x, (length_x-1))
# return ([50, 50, 50])[0] + add([50, 50, 50],0)
