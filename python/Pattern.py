# n = int(input("Enter a number: "))
# rev = 0
#
# while n > 0:
#     digit = n % 10         # extract last digit
#     rev = rev * 10 + digit # build reversed number
#     n //= 10               # remove last digit
#
# print("Reversed number:", rev)


# for i in range(5):
#     print("*",end = "")

# for i in range(2):
#     print("*",end="")
# print()
# for i in range(3):
#     print("*",end="")
# print()

# n = int(input("enter:"))
# m = int(input("enter:"))
# for i in range(n):
#     for j in range(m):
#         print("*",end="")
#     print()

# n= 5
# for i in range(n+1):
#     for j in range(i):
#         print(str(i)+"*",end=" ")
#     print()
#
# print("Vishal Kumar   >")
#
# for i in range(n+1):
#     for j in range(i,n):
#         print(str(n-i) + "*",end=" ")
#     print()

# n= 5
# for i in range(n):
#     print(" " * (n-i) +"*"*(2*i-1))
#     # print()
#
# print(" Vishal")
#
# for i in range(n-1,0,-1):
#     print(" " * (n-i) +"*"*(2*i-1))

#
# n=int(input("enter_num:"))
# # m=int(input("enter_num"))
# for i in range(n):
#     for j in range(n):
#         print("*",end="")
#     print()

# def row_col(n):
#     for i in range(n):
#         for j in range(n):
#             print("*",end="")
#         print()
#     return(n)
# row_col(5)


# def row_col(n):
#     for i in range(n+1):
#         for j in range(i):
#             print("*",end="")
#         print()
#     return(n)
# row_col(5)

# def row_col(n):
#     for i in range(n+1):
#         for j in range(n-i):
#             print("*",end="")
#         print()
#     return(n)
# row_col(5)
