num = input("Enter your Three Numbers (seperate them by space) : ")
num = num.split(" ")

if num[0] > num[1] and num[0] > num[2]:
    print(f"{num[0]} is the largest number")
elif num[1] > num[0] and num[1] > num[2]:
    print(f"{num[1]} is the largest number")
elif num[0] == num[1] and num[0] == num[2]:
    print("All numbers are equal")
else: 
    print(f"{num[2]} is the largest number")