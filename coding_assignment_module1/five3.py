#3. Write a python program for binary search to search a number in the list of given numbers. If the number isn't present, give the appropriate message. Both the list and the number to be searched is given by the user. Learn more about binary search from geeksforgeek if required.

print("Enter a list of numbers separated by space:")
inp=input()
list=inp.split()
print("Enter the number to be searched:")
num=int(input())
nl=[int(i) for i in list]
nl.sort()
print("Sorted list is ",nl)
low=0
high=len(list)-1
found=False
loc=-1
while high >= low and not found :
    mid=(low+high)//2
    if nl[mid]>num:
        high=mid-1
    elif nl[mid]==num:
        loc=mid
        found=True
    else:
        low=mid+1
if loc>=0:
    print(num,"is located at",loc,"in the sorted list")
else:
    print(num,"is not present in the list")
