#4. Write a Python program to calculate the sum of the digits in an integer.

print("Enter an integer number:")
num=int(input())
summ=0
while num>0:
    summ=summ+num%10
    num=num//10
print("Sum is ",summ)
