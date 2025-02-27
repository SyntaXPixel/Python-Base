A = int(input("Enter the First Number: "))
B = int(input("Enter the Second Number: "))
C = int(input("Enter the Third Number: "))

if A > B and A > C:
    print("A is the largest number")
elif B > A and B > C:
    print("B is the largest number")
elif A == B and A == C:
    print("All numbers are equal")
else :
    print("C is the largest number")
