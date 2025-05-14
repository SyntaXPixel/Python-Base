input1=input("Enter your Set1 Values : ")
set1=set(map(int,input1.split()))

input2=input("Enter your Set2 Values : ")
set2=set(map(int,input2.split()))

intersection= set1 & set2

print(f"Intersection of Set1 and Set2 {intersection}")
