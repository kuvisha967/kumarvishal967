# x=1
# # x=0
# for x in [3]:
#     pass
# print(x)

# t = ([],)
# t[0].append(5)
# print(t)

# def outer():
#     x = 5
#     def inner():
#         x = x + 1
#         return x
#     return inner()
#
# print(outer())

# a, b = 256, 256
# c, d = 257, 257
# print((a == b), (c is d))

# x = input("Enter:") // 0
# print(type(x))

# print(0 < 1 < 2 == 2 > 1)
# print(0 < 1 < 2 == 2 < 1)


# print(int(True))
# print(int(False))
# print(int(3.9))
# print(bool("False"))
# print(int(True) + int(False) + int(3.9) + bool("False"))
# print(True + False + int(3.9) + bool("False"))
#
# print(1+True+True+False)
# print(True+False)

# s = "pythonrocks"
# # t=s[::-2]
# # print(t)
# # print(t[1:4])
# print(s[::-2][1:4])

# for i in range(3):
#     for j in range(3):
#         if j == 2:
#             break
#     else:
#         print("Inner Done")
# else:
#     print("Outer Done")

# _ = [k for k in range(3)]
# print(_)
# _ = [k for k in range(3)]
# # print(k)

# for i in range(3):
#     if i % 2 == 0:
#         continue
#     else:
#         print("Done")

# x = [[[]]]
# x[0].append(1)
# print(x)

# def sqr(a):
#     b= a**2
#     return b
# # print(sqr(4))
#
# def odd_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False

# x = odd_even(12)
# # print(x)
#
# def is_vowel(char):
#     if char in 'aeiou':
#         return True
#     else:
#         return False

# y = is_vowel('vishal')
# print(y)

# def pass_check(password):
#     if len(password) >= 8 and password[0].isupper() and any(i.isdigit() for i in password):
#         print('password is eligible')
#     else:
#         print('password is too short')
#     return password

# pass_check('Vishal@12096')

# print(dir(str))
# print(dir(tuple))

# x="python python c c java python"
# print(x.split())
# print(" ".join(x.split()))
# v='  vishal'
# print(v.strip())
# s = "banana"
# print(s.strip("an"))
# t = (1, 2, 3)
# print(id(t), id(t[:]))

# n = 5
# for i in range(n):
#     for j in range(i, n):
#         print("*", end=" ")
#         if i + j == n - 1:
#             break
#     print()

# a = {1, 2}
# b = {2, 3}
# # print(a ^ b, a & b)
#
# d = {True: "A", 1: "B", 1.0: "C"}
# print(d, len(d))
#
# print(d.items())
# print(d.keys())
# print(d.values())

# d = {}
# d[(1,2)] = "tuple"
# # d[[1,2]] = "list"
# print(d)
#
# x = {}
# x[x] = 1
# print(x)

# a = {()}
# b = {tuple()}
# print(a == b, len(a | b))


# def sqr(n):
#     return n**n
# print(sqr(2))

# names = ["  vishal","annie  "]
# row = tuple(map(str.strip,names))
# # print(row)
#
# words= ["apple","ant","vishal","annie"]
# res= list(filter(lambda x: x[0] == 'a', words))
# print(res)


# employees = [
#     {"name": "Akash", "age": 32, "salary": 50000},
#     {"name": "Meena", "age": 25, "salary": 40000},
#     {"name": "Rahul", "age": 35, "salary": 60000}
# ]
#
# result = reduce(
#     lambda a, b: a + b,
#     map(
#         lambda x: x["salary"] * 0.9,     # tax deduction
#         filter(lambda e: e["age"] > 30, employees)
#     )
# )
#
# print(result)

# def f(x,y=[]):
#     y.append(x)
#     return y
# print(f(1,[]),f(2,[]),f(3,[]))

# x = 10
# def g(y): return y + x

# def outer():
#     x = 5
#     def inner():
#         return x + 1
#     return inner
#
# f = outer()
# print(f.__closure__[0].cell_contents)

# def deco(f):
#     def wrapper(x):
#         return f(x) * 2
#     return wrapper
#
# @deco
# def f(x): return x + 1
#
# print(f(3))

# nums = [0, 1, 2, 3, 4]
# print(list(filter(None, nums)))

# for i in range(5):
#     print("*",end="")
# print()
# for i in range(5):
#     print("*",end="")
# print()
# for i in range(5):
#     print("*",end="")

# s="swwiss"
# for i in s:
#     if s.count(i) == 1:
#         print(i)
#         break
# print(0/1)


# n=int(input("enter_num:"))
# c= n**3
# print(c)

# def grt(n):
#     if n > 50:
#         print("Massive")
#     else:
#         print("smaller")
#     return n
# grt(51)


lst= [[1, 2, [3]], [4, 5], [6, [7, 8]]]
# li = []
# for i in lst:
#     # print(f'this is my i:{i}')
#     for j in i:
#         # print(f'this is my j:{j}')
#         if isinstance(j, list):
#             for k in j:
#                 li.append(k)
#         else:
#             li.append(j)
# print(li)
# import numpy as np
# n = np.array(lst)
# print(n.flatten())

# def is_even(*args):
#     for i in args:
#         if i % 2 == 0:
#             print("even")
#         else:
#             print("odd")
#     return args
#
# is_even(5,3,65,67,7,8)

# is_even = lambda x: "even" if x%2==0 else "odd"
# print(is_even(7))

# def ad(*args):
#     for i in args:
#         s = i+i
#         print(s)
#     return args
# ad(1,2,3)

# def mul(x,y):
#     return x*y
# print(mul(2,3))
#
# mult = lambda x,y: x*y
# print(mult(2,3))

# def power(n):
#     return lambda x: x**n
# sqr = power(2)
# cube = power(3)
# print(sqr(5))
# print(cube(5))

# li = [3, 6, 600,40001, 9, 2]
# n= len(li)
# # print(n)
# for i in range(n):
#     for j in range(n-i-1):
#         if li[j]>li[j+1]:
#             li[j],li[j+1] = li[j+1],li[j]
# print(li[-2])

# li = [1,2,2,2,3,3,4,5,5,6,7,7]
# d= list(set(li))
# print(d)

# s='vishall'
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)

# def chr_cnt(s):
#     d = {}
#     for i in s:
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1
#     return d
# print(chr_cnt('vishall'))
#
# s='vishall'
# r = list(map(chr_cnt,s))
# print(r)

# num1=153
# numbe=str(num1)
# num = len(numbe)
# row=0
# for i in numbe:
#     row = row + int(i)**num
# if row == num1:
#     print(f'{numbe} is armstrong')
# else:
#     print(f'{numbe} is not armstrong')

# data = ['1','2','3','4']
# print(type(data[0]))
# l = []
# for i in data:
#     if i != str:
#         l.append(int(i))
# print(l)

# l = list(map(int,data))
# print(l)

# print(dir(dict()))

# class discount_sys:
#     def __init__(self, prd_name, price):
#         self.prd_name = prd_name
#         self.price= price

#     def discount_cal(self):
#         discount_amount = self.price*(10/100)
#         final_price = self.price - discount_amount
#         return discount_amount,final_price
#     def display_info(self):
#         print("product name:", self.prd_name)
#         print("price:", self.price)
#         print("Discounted Price, Final_price", self.discount_cal())
# c=discount_sys("fan",1000)
# # c.display_info()

# class A: pass
# class B: pass
# class C(A,B): pass
# print(C.__mro__)


# class Calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#
#     def add(self):
#         return(self.a+self.b)
#
#     def mul(self):
#         return(self.a*self.b)
#
# ad=Calculator(1,2)
# print(f'addition of a+b is: {ad.add()}')
# print(f'multiplication of a*b is: {ad.mul()}')


# class Employee:
#     def __init__(self,name,emp_id,salary):
#         self.name=name
#         self.emp_id=emp_id
#         self.salary=salary
#     def get_details(self):
#         return f'Name: {self.name}, Emp ID: {self.emp_id}, Salary: {self.salary}'
#
#     def get_salary(self):
#         return self.salary
#
#     class Full_time_employee(Employee):
#         def __init__(self):
#             return self.salary + 5000

# class Product:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#
#     def get_base_price(self):
#         return self.price
#
# class Order(Product):
#     def __init__(self,name,price,full_size):
#         super().__init__(name,price)
#         self.full_size = full_size
#
#
#     def get_price_with_gst(self):
#         # d= self.price + self.full_size * 0.18
#         # return d
#         if self.price > 0:
#             d= self.price + self.full_size * 0.15
#         else:
#             raise ValueError('price cannot be zero')
#         return d
#
#
#         # raise ZeroDivisionError("Cannot divide by zero")
# try:
#     p=Order("fan", 1000,10)
#     print(p.get_price_with_gst())
# except ValueError as e:
#     print(e)
# finally:
#     print('Task completed')


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display_person(self):
#         return self.name
#
# class Employee(Person):
#     def __init__(self, name, age, salary):
#         super().__init__(name, age)
#         self.salary = salary
#
#     def getSalary(self):
#         return self.salary
#
# class Manager(Employee):
#     def __init__(self, name, age, salary, Manager_name):
#         super().__init__(name, age, salary)
#         self.Manager_name = Manager_name
#
#     def getManagerName(self):
#         return self.Manager_name

# try:
#     li=[1,2,3,4,5,6,7,8,9]
#     print(li[0])
# except Exception as e:
#     print(f'Error: {e}')
# finally:
#     print('execution completed!')

# user_name = ["vishal","Annie"]
# try:
#     i = input("Enter User: ")
#     if i in user_name:
#         raise Exception("Username already exists")
#     else:
#         user_name.append(i)
#         print(f"{i} has been added to the list")
# except Exception as e:
#     print(e)
# finally:
#     print(user_name)

######## Hi Akash, Can you please explain with industry level code example, how to use Polymorphism and Abstraction and if possible which type of Inheritance we can use?
# class Product:
#     def __init__(self, product_name, product_type, product_price):
#         self.product_name = product_name
#         self.product_type = product_type
#         self.product_price = product_price
#
#     def product_details(self):
#         if self.product_type == 'Electronic':
#             if self.product_name == 'Mobile':
#                 discount = float(self.product_price) * (3/100)
#                 prd_discounted_price = self.product_price - discount
#             elif self.product_name == 'Laptop':
#                 discount = float(self.product_price) * (5/100)
#                 prd_discounted_price = self.product_price - discount
#             elif self.product_name == 'Tablet':
#                 discount = float(self.product_price) * (4/100)
#                 prd_discounted_price = self.product_price - discount
#                 # gst_percent = discounted_price * (12/100)
#                 # gst_price = discounted_price + gst_percent
#         elif self.product_type == 'Electrical':
#             if self.product_name == 'blub':
#                 discount = float(self.product_price) * (2/100)
#                 prd_discounted_price = self.product_price - discount
#             elif self.product_name == 'Fan':
#                 discount = float(self.product_price) * (3/100)
#                 prd_discounted_price = self.product_price - discount
#                 # gst_percent = discounted_price * (18 / 100)
#                 # gst_price = discounted_price + gst_percent
#         return (f'Product_Discount_price: {prd_discounted_price}')
#
# class Customer(Product):
#         def __init__(self, product_name, product_type, product_price,customer_id, customer_name, customer_card):
#             super().__init__(product_name, product_type, product_price)
#             self.customer_id = customer_id
#             self.customer_name = customer_name
#             self.customer_card = customer_card
#
#         def customer_details(self):
#             if self.customer_card == 'visa':
#                 card_discount = prd_discounted_price * (3/100)
#                 discount_price = prd_discounted_price - card_discount
#             return discount_price
#
#
# e=Product('Mobile', 'Electronic', 10000)
# e1=Product('Tablet', 'Electronic', 12000)
# d=Product('blub', 'Electrical', 540)
# d1=Product('Fan', 'Electrical', 90000)
#
# print(e.product_details())
# print(e1.product_details())
# print(d.product_details())
# print(d1.product_details())
#
# try:
#     a=Customer('Mobile', 'Electronic', 10000, customer_id='0001', customer_name='ANIL', customer_card='visa')
#     print(a.customer_details())
# except Exception as e:
#     print(e)


class Product:
    def __init__(self, product_name, product_type, product_price):
        if product_price <= 0:
            raise ValueError("Product price must be positive")

        self.product_name = product_name
        self.product_type = product_type
        self.product_price = product_price
        self.discounted_price = None

    def product_details(self):
        try:
            if self.product_type == 'Electronic':
                if self.product_name == 'Mobile':
                    discount = self.product_price*0.03

                elif self.product_name == 'Laptop':
                    discount = self.product_price*0.05

                elif self.product_name == 'Tablet':
                    discount = self.product_price*0.04
                else:
                    raise ValueError("Invalid electronic product")

            elif self.product_type == 'Electrical':
                if self.product_name == 'Bulb':
                    discount = self.product_price*0.02

                elif self.product_name == 'Fan':
                    discount = self.product_price*0.03
                else:
                    raise ValueError("Invalid electrical product")
            else:
                raise ValueError("Invalid product type")

            self.discounted_price = self.product_price - discount
            return (f'di: {self.discounted_price}')

        except Exception as e:
            return f"Error: {e}"


class Customer(Product):
    def __init__(self, product_name, product_type, product_price,
              customer_id, customer_name, customer_card):

        super().__init__(product_name, product_type, product_price)
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_card = customer_card
        self.final_price_with_gst = None

    def customer_details(self):
        try:
            if self.discounted_price is None:
                self.product_details()

            if self.customer_card.lower() == 'visa':
                card_discount = self.discounted_price * 0.03
                final_price_without_gst = self.discounted_price - card_discount
            else:
                final_price_without_gst = self.discounted_price

            gst_cal = final_price_without_gst * 0.18
            self.final_price_with_gst = final_price_without_gst + gst_cal

            return final_price_without_gst, self.final_price_with_gst
        except Exception as e:
            return f"Error: {e}"

#
# b = Customer('Bulb','Electrical',110,'001','ANIL','VISA')
# print(b.customer_details())



# import numpy as np
# r=np.array([1,2,3,4,5])
# print(type(r))

# l = [1,2,3]
# print(l*2)
# r=np.array(l)
# print(r*2)

# li = np.array([5,10,15,20])
# print(li)
# print(r.shape)
# print(type(li))
# print(li.reshape(2,2))

import numpy as np

# myarr = np.array([1,2,3,4,6,5,7],dtype= int)
# print(myarr.shape)
# print(myarr.ndim)

# listarray = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(listarray)

# a = np.array([1, 2, 3])
# b = np.array([1.0, 2.0, 3.0])
# print(a.dtype, b.dtype)

# a = np.arange(8)
# print(a)
# b = a.reshape(2, -1, 2)
# print(b)
# print(b.shape)
# print(b.)

# a = np.array([[1,2],[3,4]])
# b = a.ravel()
# print(b)
# b[0] = 99
# print(b)
# print(a)

# l= list(range(10))
# print(l)

# array_3d = np.array([
#     [[1, 2, 3], [4, 5, 6], [7, 8, 9]],      # First layer
#     [[10, 11, 12], [13, 14, 15], [16, 17, 18]],  # Second layer
#     [[19, 20, 21], [22, 23, 24], [25, 26, 27]]   # Third layer
# ])
# print(array_3d.shape)

# a = np.arange(6)
# mask = a % 2 == 0
# a[mask] = -1
# print(a)

#
# a = np.array([10,20,30,40])
# idx = np.array([3,1,2,0])
# # print(a[idx])
#
# a = np.arange(12).reshape(3,4)
# print(f'{a} ######')
# print(a[1:, ::-1])

# array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
#
# reshaped1 = array.reshape((2, 2, -1))
# print(reshaped1)
# # converting it to 2-D array
# reshaped2 = array.reshape((4, -1))
#
# print(reshaped2)


import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df = pd.read_csv('titanic.csv')
# print(df.head())

df1 = pd.read_excel('titanic.xlsx')
# print(df.head())

# print(df1.describe())
# print(df1.info())

df2 = ((df['Sex'] == 'female') & (df['Survived'] == 1))
print(df2.head())

# df2 = ((df['PassengerId'] == 'female') & (df['Survived'] == 1))
df['Sex'].value_counts()
