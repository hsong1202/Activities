
myList = [23, 45, 12, 10, 25]

#find the sum of the numbers using a while loop

listLength = len(myList)

i = 0
sum = 0
while (i < listLength):
    sum = sum + myList[i]
    i = i+1
print(sum)

print(23 + 45 + 12 +10 +25)

numbers = [12, 3, 56, 67,89,90]
x = 0
for num in numbers:
    print(f"this is {x} iteration")
    print(f"this is the value of {x} in numbers[num]")
    x = x + 1
    print(f"this is the value after the iteration:", x)
# else:
#     print(x)

