# var=input("1.what is your name\na.kumar    b.vishal\nc.vishal kumar    d.none\n:")
# if var=="vishal kumar":
#     print("correct answer:",var)
# else:
#     print("wrong answer")
# print("game over!\nThanks for playing")


# li=[2,3,4,5,6,10,11,12,15,16]
# even_li=[]
# odd_li=[]
# for val in li:
#     if val%2==0:
#         even_li.append(val)
#     else:
#         odd_li.append(val)
#
# print(even_li)
# print(odd_li)

# mix_li=[2,5.5,'cjf','vishal']
# #mix_li=input()
# str_li=[]
# even_li=[]
# float_li=[]
# for val in mix_li:
#     if type(val)== str:
#         str_li.append(val)
#     elif val%2==0:
#         even_li.append(val)
#     elif type(val)== str:
#         float_li.append(val)
# print(str_li)
# print(even_li)
# print(float_li)

# li=[10,20,30,40,50]
# sum=0
# for i in li:
#     sum+=i
# print(sum)

# import time
# name=input("Enter your name:")
# hour= int(input("Enter time:"))
# # hour= int(time.strftime('%H'))
# if(hour>0 and hour<12):
#     print("good morning!:",name)
# elif(hour>=12 and hour<17):
#     print("good afternoon!:",name)
# elif(hour>=17 and hour<22):
#     print("good evening!:",name)
# elif(hour>=22 and hour<=24):
#     print("good night!:",name)

# if n%2!=0:
#     print("Weird")
# if n%2==0:
#     if n>=2 and n<=5:
#         print("Not Weird")
#     elif n>=6 and n<=20:
#         print("Weird")
#     elif n>20:
#         print("Not Weird")

# for i in range(1,6):
#     print('*'*(i))
# for i in range(3,6,2):
#     print('*'*i)

# for i in range(1):
#     print('    *')
# for i in range(1):
#     print('   *'+' *')
# for i in range(1):
#     print('  *'+' *'+' *')
# for i in range(1):
#     print(' *'+' *'+' *'+' *')
# for i in range(1):
#     print('*'+' *'+' *'+' *'+' *')

# for i in range(1,6):
#     print(' *'*i)
# for i in range(1,6):
#     print(' *'*(6-i))

# for i in range(1,6):
#     for j in range(6-i):
#         print(" ",end="")
#     for j in range(i):
#         print('*',end=" ")
#     print()

# for i in range(1,6):
#     print(' '*(5-i),' *'*i)
#
# li = [67,56,21,89,43,12,44,32,18,62]
# # # [12, 18, 21, 32, 43, 44, 56, 62, 67, 89]
# #
# n=len(li)
# for i in range(n):
#     for j in range(n-1):
#         if li[j]>li[j+1]:
#             li[j],li[j+1]=li[j+1],li[j]
# print(li)

# num=25
# sum=0
# while num<=35:
#     # print(num)
#     sum=sum+num
#     num=num+1
# print(sum)


# li= [['qwerty',12,'89'],[78.90,67,'rt','Vamshi'],['ty,90']]     #output = ['qwerty', '89', 'rt', 'Vamshi', 'ty,90']
#
# str_li=[]
# st=""
# for i in li:
#     for j in i:
#         if type(j) is str:
#             str_li.append(j)
#             for i in str(str_li):
#                 st= i+st
# # print(str_li[::-1])
# print(st)

# usr=input('')
# usr1=0
# for i in usr:
#     usr1=usr1+1
# print(usr1)

# usr=input('Enter str:')
# cnt=0
# vwl='aeiou'
# for i in usr:
#     if i in vwl:
#         cnt=cnt+1
# print(cnt)
# islower isupper isnumeric isalpha
# st='Ok, Hello, 123,Yes,89 @,rt&^7vh$%^4354'
# lower=''
# upper=''
# num=''
# special_chr=''
# # print(dir(str))
# for i in st:
#     if i.islower():
#         lower=lower+i
#     elif i.isupper():
#         upper=upper+i
#     elif i.isdigit():
#         num=num+i
#     else:
#         special_chr=special_chr+i
# print(lower)
# print(upper)
# print(num)
# print(special_chr)

# n = list(map(int, input().split()))
# print(n) #give input 2 3 44 22 1

# def solve(a,b):
#     add=a+b
#     sub=a-b
#     return add , sub
#
# print(solve(3,2))


# def add(*args):
#     operators =input()
#     Sum = 0
#     for i in args:
#         if operators == "+":
#             Sum=Sum+i
#     return(Sum)
# print(add(10,34))

# st1='listen'
# st2='silent'

# print(type(st1))
# print(dir(str))
# print(st1[::-1])
# if st1==st2[::-1]:
#     print('is palindrome')
# else:
#     print('not a palindrome')
# print(st1.count('i'))

# if len(st1)==len(st2):
#     print('anagram')
# else:
#     print('not a anagram')

# st='i love india'
# # st= ["i","love","india"]
# # st_j= " ".join(st)
# st1={}
# for i in st:
#     if i in st1:
#         st1[i]+=1
#     else:
#         st1[i]=1
# print(st1)


# st1='listen'
# st2='silent'
#
# if len(st1)==len(st2):
#     print('Length is matching, we can go head to check for the count of accurance of elements')
#     st1_1={}
#     st2_2={}
#     for i in st1:
#         if i in st1_1:
#             st1_1[i]+=1
#         else:
#             st1_1[i]=1
#     print(st1_1)
#     for i in st2:
#         if i in st2_2:
#             st2_2[i]+=1
#         else:
#             st2_2[i]=1
#     print(st2_2)
#     if st1_1 == st2_2:
#         print('Every thing is matching hence it is a Anagram')
#     else:
#         print('not an anagram, because each element of a string is not matching yet length is matching')
# else:
#     print('not an anagram, because length is not matching')

# st="udnag"
# rev_st=""
# for i in st:
#     rev_st=i+rev_st
#     # print(rev_st)
# print(rev_st)


# st="I am good wala bad boy"
# sp=st.split()
# # print(sp)
# cnt_st=0
# max_st=""
# for i in sp:
#     if len(i)>cnt_st:
#         # cnt_st= cnt_st+len(i)
#         max_st = i
#         cnt_st= len(i)
#
#         print(cnt_st,i)
# print(cnt_st,max_st)
# for i in cnt_st:
#     max_st= len(i)
#     print(max_st)

# gt= lambda a,b,c: max(a, b, c)
#
#
# num1, num2, num3= 5, 12, 8
# rt=gt(num1, num2, num3)
# print(rt)
# lst=[]
# var= lambda a: for i in range(1,20): if a%2==0
# print(var)
# var= [i for i

# palim= [i for i in range(1, 1001) if str(i)== str(i)[::-1] and len(str(i))== 3]
# print(len(palim))
# print(palim)

# st="gandu"
# rev_st=""
# for i in st:
#     rev_st= i+rev_st
# print(rev_st)
# li=[1997,2000,2010,2012,2016,2022,2023,2024]
# def leap_year(li):
#     for i in li:
#         if i%4==0:
#             print("it's a leap year:",i)
#         else:
#             print("not a leap year:",i)
#     return li
#
# print(leap_year([1997,2000,2010,2012,2016,2022,2023,2024]))

# leap_yr= [i for i in li if i%4==0]
# print(leap_yr)

# leap_yr= list(filter(lambda i: i%4==0,li))
# print(leap_yr)

# var= open('Sample_1.csv', 'r')
# # print(var.readlines())
# # print(var.read())
# # print(var.readline())
# data = var.readlines()
# print(data)
# # print(type(data))
# for i in data:
#     print(i.capitalize())

# cnt_acr={}
# for i in data:
#     if i in cnt_acr:
#         cnt_acr[i]+=1
#     else:
#         cnt_acr[i]=1
# print(cnt_acr)
#
# splt_data= data.split()
# cnt_acrr={}
# for i in splt_data:
#     if i in cnt_acrr:
#         cnt_acrr[i]+=1
#     else:
#         cnt_acrr[i]=1
# print(cnt_acrr)

# class information:
#     def __init__(self):
#         pass
#     def


# fruit = ["apple","banna","kiwi"]
# new_li = []
#
# for i in fruit:
#     if 'a' in i:
#         new_li.append(i)
# st_fruit = " ".join(new_li)
# cnt_li = {}
# for i in st_fruit:
#     if i in cnt_li:
#         cnt_li[i]+=1
#     else:
#         cnt_li[i] = 1
#
# print(new_li)
# print(st_fruit)
# print(cnt_li)


arr = {34,20,23,70}
arr_l = list(arr)

arr_l.sort(reverse=True)

larg_sum= arr_l[0] +arr_l[1]

reslt= {larg_sum}

print(reslt)
