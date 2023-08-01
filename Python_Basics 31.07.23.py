# Write a program that takes a number as input and checks whether it is even or odd.
# number=int(input("Enter a number:"))
# if(number%2!=0): #check for odd
#     print(f"{number} is odd")
# else: # check for even
#     print(f"{number} is even")


# loop

# for
for i in range(1,11):   # range(start,end+1)
    print(f"1999 x {i} = {1999* i }")
# while
i=1
while (i<16 or i%2==0):
    print(i)
    i+=1


# Write a program to print the first 10 numbers of the Fibonacci sequence.
# What is fibonacci number?: https://en.wikipedia.org/wiki/Fibonacci_sequence

# using for loop to print 10 numbers in fibonacci
f1=0 #first number in fibonacci
f2=1 #second number in fibonacci
next=0 # next number in fibonacci
print("First 10 numbers in fibonacci")
# printing two fibonacci 
print(f1) 
print(f2)
for i in range(8):
    next=f1+f2 # as next fibonacci number is the sum of previous two numbers
    print(next)
    f1=f2
    f2=next