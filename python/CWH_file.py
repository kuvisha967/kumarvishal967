#for loop
# colour=['Red','Orange','Green','Yellow']
# for i in colour:
#     print(i)
#     for j in i:
#         print(j)

# for i in range(1,9,2):
#     print(i)
#     if i==5:
#         break
# print('loop skip 5')

# li=[78,56,21,34,79,10]
# n=len(li)
# print(dir(list))
# sorted(li) #wrong
# print(li[-2])#wrong
# li.sort()
# print(li[-2])
# for i in range(n):
#     for j in range(0,n-i-1):#(0,10-1-1)
#         if li[j]>li[j+1]:
#             li[j],li[j+1]=li[j+1],li[j]
# print(li)
# print(li[-3])

# def sec_lrg(n):
#     for i in range(len(n)):
#         for j in range(len(n)-1):
#             if li[j]>li[j+1]:
#                 li[j], li[j + 1] = li[j + 1], li[j]
#     return n
# li=[1,3,5,2,10,25,23,15,9,8,12,14]
# n=len(li)
# print(sec_lrg(li)[-2])

# x = "awesome"
#
# def myfunc():
#     global x
#     x = "fantastic"
#     print("Python is " + x)
#
# myfunc()
#
# print("Python is " + x)

# txt = "hello WorlD "
# x = txt.capitalize()
# x = x.replace('H','J')
# print(x)


# #If
# x = 9
# #, what is a correct syntax to print 'The price is 9.00 dollars'?
#
# print(f'The price is {x:.2f} dollars')
# print(f'The price is {x:2} dollars')
# # print(f'The price is {x:format(x)} dollars')

# age = 36
# txt = f"My name is John, and I am {age}"
# print(txt)

# print(f'the price of this is {3+4} rupees')
# print(bool(2))

# fruits = ["apple", "banana", "cherry"]
# fruits.insert(1,"lemon")
# print(fruits)


# mylist = ['apple', 'banana', 'cherry']
# i = 0
# while (i >
#     len(mylist)):
#     print(mylist[i])
#     i = i + 1


# fruits = ['apple', 'banana', 'cherry']
# newlist = ['apple' for x in fruits]
# print(newlist)

# a= "banana"
# for x in a:
#   print(x, end="")


# txt = "The best things in life are free!"
# print("free" in txt)
#
# b = "Hello, World!"
# print(b[-5:-1])

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["watermelon"]
# print(thislist)
#
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i], end= " ")

# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1

# fruit = ["apple","banana","kiwi","cherry","mango"]
# new_fruit = []

# for i in fruit:
#     if "a" in i:
#        new_fruit.append(i)
# print(new_fruit)

# new_fruit = [i for i in fruit if "a" in i]
# print(new_fruit)

# new_fruit = [i.capitalize() for i in fruit]
# print(new_fruit)

# list = [i for i in range(10) if i > 5]
# print(list)


# def myfunc(n):
#   return abs(n - 50)
#
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
#
# list3 = list1 + list2
# print(list3)

# x = ("apple","orange","banana")
# y = list(x)
# y[0] = "kiwi"
# x = tuple(y)
# print(x)

# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y
#
# print(thistuple)

# fruits = ("apple", "banana", "cherry")
#
# (green, yellow, red) = fruits
#
# print(green)
# print(yellow)
# print(red)
# print(fruits)
# print(green, yellow, red)


# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
#
# (green, yellow, *red) = fruits
#
# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "banana", "mango", "papaya", "pineapple", "cherry", "kiwi")
#
# (green, yellow , *tropic, red, algay) = fruits
#
# print(green)
# print(yellow)
# print(tropic)
# print(red)
# print(algay)


# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#   print(x)
#
#
# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
#   print(thistuple[i])

# thisset = {"apple", "banana", "cherry", "apple"}
#
# print(thisset)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
#
# set3 = set1.union(set2)
# print(set3)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}
#
# myset = set1.union(set2, set3, set4)
# print(myset)

# x = {"a", "b", "c"}
# y = (1, 2, 3, 3)
# z = x.union(y)
# print(z)

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
#
# x = car.keys()
# y = car.values()
# z = car.items()
#
# print(x) #before the change
# print(y)
# print(z)
#
# car["color"] = "white"
#
# print(x) #after the change
# print(y)
# print(z) riya

# str1 = "logical"
# str2 = ""
# for i in range(len(str1)):
#     if i%2 == 0:
#         str2 = str2 + str1[i].upper()
#     else:
#         str2 = str2 + str1[i].lower()
#
# print(str2)

# str1 = "logical"
# str2 = list(str1)
# print(str2)
# for i in range(len(str2)):
#     if i%2==0:
#         str2[i] = str2[i].upper()
#
# str3= ''.join(str2)
# print(str3)

# nums = [1, 3, 2, 3]
# nums.sort()
#
# print(nums)
#
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] == nums[j]:
#             print(True)

# s = "racecar"
# t = "carrace"
# print(sorted(s))
# print(sorted(t))
# s1={}
# t1={}
#
# for i in s:
#     if i in s1:
#         s1[i] += 1
#     else:
#         s1[i]=1
# print(s1)
#
# for i in t:
#     if i in t1:
#         t1[i] += 1
#     else:
#         t1[i] = 1
# print(t1)
#
#
# if len(s)==len(t):
#     if s1 == t1:
#         print(f'it is an anagram')


# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#     for y in fruits:
#         print(x,y)

# for x,y in zip(adj,fruits):
#     print(x,y)


# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result
#
# print("Recursion Example Results:")
# tri_recursion(6)


# # st= 'vishal'
# st = ["i","love","india"]
# rv_st = ''
# for i in st:
#     rv_st = i + rv_st
# print(rv_st)

# li = [24,56,72,63,10,12,9]
# # li.sort()
# # print(f'second largest: {li[-2]}')
#
# max1 = max2 = float('-inf')
# for i in li:
#     if i> max1:
#         max2 = max1
#         max1 = i
#     elif i > max2 and i != max1:
#         max2 = i
# print(max2)

class Product:
    def __init__(self, product_type, product_name, product_price):
        self.product_name = product_name
        self.product_type = product_type
        self.product_price = product_price
        self.discounted_price = None

        if self.product_price <= 0:
            raise ValueError("The price of the product must be positive")

    def product_details(self):
        try:
            if self.product_type == 'Electronic':
                if self.product_name == 'Mobile':
                    discount = self.product_price * 0.02
                elif self.product_name == 'Laptop':
                    discount = self.product_price * 0.05
                elif self.product_name == 'Tablet':
                    discount = self.product_price * 0.03
                else:
                    raise ValueError("The product name is not supported")
            elif self.product_type == 'Electrical':
                if self.product_name == 'Fan':
                    discount = self.product_price * 0.02
                elif self.product_name == 'Light':
                    discount = self.product_price * 0.025
                else:
                    raise ValueError("The product name is not supported")
            else:
                raise ValueError("The product type is not supported")

            self.discounted_price = self.product_price - discount
            return (f'Product_price: {self.product_price} and dicount_amount: {discount} and Discounted_price: {self.discounted_price}')

        except Exception as e:
            print(f'Erorr_Occured: {e}')

        finally:
            print('*****||Product Section||*****')

class Customer(Product):
    def __init__(self, product_type, product_name, product_price, customer_name, customer_card):
        super().__init__(product_type, product_name, product_price)
        self.customer_name = customer_name
        self.customer_card = customer_card


    def customer_details(self):
        try:
            if self.discounted_price is None:
                self.product_details()

            if self.customer_card.lower() == 'visa':
                card_discount = self.discounted_price * 0.04

            elif self.customer_card.lower() == 'rupay':
                card_discount = self.discounted_price * 0.05
            else:
                raise ValueError("The customer card is not supported")

            price_without_gst = self.discounted_price - card_discount
            gst_cal = price_without_gst * 0.18
            self.price_with_gst = price_without_gst + gst_cal

            return (f'Product_price: {self.product_price} and Discounted_price: {self.discounted_price}',
                    f'Price_without_gst: {price_without_gst} and gst_amount: {gst_cal} and price_with_gst: {self.price_with_gst}')

        except Exception as e:
            print(f'Erorr_Occured: {e}')

        finally:
            print('*****||Customer Section||*****')





# p = Product('Electronic','Mobile',12697)
# print(p.product_details())

c = Customer('Electrical', 'Fan', 243, 'vishal', 'visa')
print(c.customer_details())
