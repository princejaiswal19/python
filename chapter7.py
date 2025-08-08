# loops in python 
# only two types of loops 1.while loop 2.for loop
# a=int(input("Enter the digit of which you want table:"))
# i=1
# while i<11:
#     # concatanate string
#     print(str(a) + "X"+str(i)+"="+str(i*a))
#     print(f"{a}X{i}={a*i}")
#     i=i+1

# code to check whether number is prime or not
# a=int(input("Enter the number:"))
# prime=False

# # i=2
# for i in range(2,a-1):
#     if(a%i==0):
#         prime=True
#         break
#     i=i+1
# if(prime):
#     print("Not prime")
# else:
#     print("prime")

# wap to find the sum of first n natural numbers

# a=int(input("Enter the number:"))
# sum=1
# i=1
# while(i<=a):
#     sum=sum*i
#     i=i+1

# print(sum)

# n=4
# for i in range(4):
#     print("*"*i)

# printing pattern 

n=3
for i in range(1,3):
    print(" "*(n-i-1), end="")
    print("*"*(2*i+1), end="")
    print(" "*(n-i-1))
