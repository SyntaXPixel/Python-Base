A = int(input("Enter the First Number: "))
B = int(input("Enter the Second Number: "))
C = int(input("Enter the Third Number: "))

if A > B:
    if A > C:
        print("A is the largest number")
    else:
        print("C is the largest number")
else:
    if B > C:
        print("B is the largest number")
    else:
        print("C is the largest number")
