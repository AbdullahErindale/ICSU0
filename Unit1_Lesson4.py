num = input("Please input a whole number that isn't zero: ") 
num = int(num) 
num2 = input("Say another number: ") 
num2 = int(num2)
num3 = num / num2
print("When", num, "is divided by", num2, end=" ")
print("the result is: %.0f"% num3)
