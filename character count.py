str = input("Enter the String: ")
count = 0
char = input("Enter the character whose occurrences you want to count: ")
for x in str:
    if x == char:
        count +=1
    else:
        pass

print(f"'{char}' appears {count} times in your string")
