num = int(input("Entre your Number : "))

def frac(num):
    if num == 0 or num == 1:
        return 1
    return num * frac(num-1)

print (f"Fractorial of {num} is {frac(num)}")
