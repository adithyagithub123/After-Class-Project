number = int(input("Enter any number which u want to enter to find the number of digits in it : "))

digits = 0

while number != 0:
    number = number // 10 
    digits += 1      

print("The number of digits is:", digits)