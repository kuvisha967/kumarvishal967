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


fruits = ['apple', 'banana', 'cherry']
newlist = ['apple' for x in fruits]
print(newlist)
