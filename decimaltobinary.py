decimal = int(input("Enter a decimal number: "))

binary = ""

if decimal == 0:
    binary = "0"
else:
    while decimal > 0:
        remainder = decimal % 2  
        binary = remainder  + binary
        decimal = decimal // 2 

print("The binary form of the entered decimal number is:", binary)
