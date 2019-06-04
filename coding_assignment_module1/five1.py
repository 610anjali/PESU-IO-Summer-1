#1. Write a Python program which accepts a sequence of comma-separated numbers from the user and generate a list and a tuple with those numbers. 

print("Enter a sequence of comma-separated numbers:")
inp=input()
list=inp.split(",")
tup=tuple(list)
print("The sequence is ",inp)
print("The sequence as a list is ",list)
print("The sequence as a tuple is ",tup)
