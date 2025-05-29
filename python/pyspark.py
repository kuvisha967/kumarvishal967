# name = ''
# while name != 'your name':
#     print('Please type your name.')
#     name = input()
# print('Thank you!')

# def calculate():
#     result = float(input("Enter the first number: "))
#     next_number = float(input("Enter the next number: "))
#
#     while True:
#         operators =input()
#         if operator == "+":
#             result += next_number
#         elif operator == "-":
#             result -= next_number
#         elif operator == "*":
#             result *= next_number
#         elif operator == "/":
#             if next_number != 0:
#                 result /= next_number
#             else:
#                 print("Error: Division by zero is not allowed.")
#                 continue
#         else:
#             print("Invalid operator. Try again.")
#             continue
#
#         # Show the intermediate result
#         print(f"Intermediate result: {result}")
#
#     return result


# # Run the calculation
# final_result = calculate()
# print("Final result:", final_result)


# li=[12,89,56,55,20,15]
# def mul(li):
#     for i in li:
#         if i%3==0 and i%5==0:
#             pass
#     return(i)
# print(mmul(li))
#
# var= list(filter(lambda i: i%3==0 and i%5==0,li))
# print(var)

# st="153"
# len_st= len(st)
# arm=0
# for i in st:
#     arm+=int(i)**len_st
# # print(arm)
# if arm==int(st):
#     print(f'yes ({arm}) is a armstrong num')
# else:
#     print(f'No ({arm}) is not an armstrong num')
#

# def arm(st):
#     len_st= len(st)
#     arms=0
#     for i in st:
#         arms+=int(i)**len_st
#     # print(arms)
#     if arms == int(st):
#         print("yes it is a armstrong num")
#     else:
#         print("No it is not an armstrong num")
# #     return arms
#     return arms == int(st)
# arm(str(input("")))



# def arm(num):
#     num_st= str(num)
#     len_num= len(num_st)
#     sum=0
#     for i in num_st:
#         arms=int(i)**len_num
#         sum= sum+arms
#     return sum == num
# # arm(str(input("")))
# for i in range(100,10001):
#     if arm(i):
#         print(i)

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)