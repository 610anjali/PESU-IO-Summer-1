#5. Write a Python program to check if a string is numeric.

print("Enter a string:")
line=input()
if line.isnumeric(): #can also use line.isdigit()
    print("It is numeric")
else:
    print("It is not numeric")
