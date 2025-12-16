####string method
# # count the char
# char_st = "apple"
# char_cnt = {}
#
# for i in char_st:
#     if i in char_cnt:
#         char_cnt[i]+=1
#     else:
#         char_cnt[i] = 1
#
# print(char_cnt)
#
# # in built method
# cr= char_st.count("a")
# print(cr)


# # reverse a str
#
# st= "PYnative"
# st1 = ""
# # slicing method
# print(st[::-1])
#
# for i in st:
#     st1 = i+st1
#
# print(st1)


# # find last occurance
# str1 = "Emma is a data scientist who knows Python. Emma works at google."
# substring = "Emma"
#
# st1_1 = str1.rfind(substring)
# print(st1_1)
#
# # if substring in str1:
# #     print(True)
# # else:
# #     print(False)

# # Check if a String is a Palindrome
# str1 = "hannah"
#
# # if str1 == str1[::-1]:
# #     print("String is a palindrome.")
# # else:
# #     print("not a palindrome")
#
# str2 = ""
#
# for i in str1:
#     str2 = i + str2
#     if str1 == str2:
#         print("String is a palindrome.")

# # Capitalize Every Next Letter
# str1 = "logical"
# str2 = ""
# for i in range(len(str1)):
#     if i%2 == 0:
#         str2 += str1[i].upper()
#     else:
#         str2 += str1[i].lower()
# print(str2)

# str1 = "logical"
# str2 = list(str1)
#
# for i in range(len(str2)):
#     if i%2 == 0:
#         str2[i]= str2[i].upper()
#     else:
#         str2[i]= str2[i].lower()
# f_str = ''.join(str2)
# print(f_str)


# remove white spaces
# str1 = "        a b c d      "
# st2=[]
# l_str1= list(str1)
# print(l_str1)
#
# for i in l_str1:
#     if i != " ":
#         st2.append(i)
# st = ''.join(st2)
# print(st)


# st2=""
# for i in str1:
#     if not i.isspace():
#         st2 += i
# print(st2)


# inbuild
# str2 = str1.strip()
# str3 = str1.replace(" ","")
# print(str2)
# print(str3)

# Replace All Occurrences of a Substring

# str1 = "Hello world, welcome to the world of Python."
# old_substring = "world"
# new_substring = "universe"
#
# str2= str1.replace(old_substring,new_substring)
# print(str2)


# # Find the First Non-Repeated Character
# str1 = "swiss"
#
# for i in str1:
#     if str1.count(i) == 1:
#         print("First Non-Repeated Character:",i)
#         break
# else:
#     print("not found any")


# # Check if Two Strings Are Rotations of Each Other
# str1 = "abcd"
# str2 = "dabs"
#
# if len(str1) != len(str2):
#     print(False)
#
# for i in range(len(str1)):
#     s = str1[i:] + str1[:i]
#     if s == str2:
#         print(True)

# # Remove Consecutive Duplicates
# str1 = "aaabbccdaa"
#
# s = list(str1)
# str2 = []
#
# for i in range(len(s)):
#     if i == 0 or s[i] != s[i-1]:
#         str2.append(s[i])
# print(str2)
# f_str = ''.join(str2)
# print(f_str)
#
#
# str1 = "aaabbccdaa"
#
# str2 = ""
#
# for i in range(len(str1)):
#     if i== 0 or str1[i] != str1[i-1]:
#         str2 += str1[i]
# print(str2)


## group anagram
# strs = ["act","pots","tops","cat","stop","hat"]
# d_str = {}
#
# for i in strs:
#     srt_s = ''.join(sorted(i))
#     print(f'str_s:{srt_s}')
#     if srt_s in d_str:
#         d_str[srt_s].append(i)
#         print(i)
#     else:
#         d_str[srt_s] = [i]
#
# print(d_str)
# print(list(d_str.values()))


# # Find the Longest Common Substring
# str1 = "abcdef"
# str2 = "zcdemf"
# # Expected Output: 'cd'
# n= len(str2)
# m= len(str1)
#
# dp = [[0] * (n + 1) for _ in range(m + 1)]
#
# max_len = 0
# end_index = 0  # end index of substring in str1
#
# for i in range(1, m + 1):
#     for j in range(1, n + 1):
#         if str1[i - 1] == str2[j - 1]:
#             dp[i][j] = dp[i - 1][j - 1] + 1
#             if dp[i][j] > max_len:
#                 max_len = dp[i][j]
#                 end_index = i
#         else:
#             dp[i][j] = 0
#
# # extract the substring
# print(str1[end_index - max_len:end_index])



nums = [1,2,2,3,3,3]
k = 2

num2 = []
# numss= nums.count(2)
# print(numss)


# for i in nums:
#     if nums.count(i) == k:
#         num2.append(i)
# print(num2)

count = {}
for i in nums:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
    # count[i] = 1 + count.get(i, 0)
# print(count)
# buk = [[] for _ in range(len(nums)+1)]

cnt = {}
for i in nums:
    if i in cnt:
        cnt[i]=+i
    else:
        cnt[i] = 1
# print(cnt)

# f = open("Sample_1.csv","r")
# f1= f.readlines()
# print(f1)
#
# for i in f1:
#     for j in i:
#         if j == "I":
#             continue
# print("i can read file")
# f.close()
# f = open("Sample_1.csv","w")
# f2= f.write("I Love my mom")
# print(f2)
#
#
# import MyModule as m
# m.wish("vishal")


st = ['vishal','anamika','vishal']
# li = list(st)
# print(li)
# print(st[::-1])
st1 = ""
st2={}

for i in (st):
    st1 = i+st1
# print(st1)

for i in st:
    if i in st2:
        st2[i] += 1
    else:
        st2[i] = 1

# print(st2)

# li = [1,2,2,3,4]
# # seen = set(li)
# # print(seen)
# s = set()
# for i in li:
#     s.add(i)
# print(s)


# def is_febo(num):
#     a,b = 0,1
#     while b<num:
#         a,b = b,a+b
#     return num == a or num == b
# print(is_febo(13))

def febo(n):
    a,b = 0,1
    for i in range(n):
        print(a, end=" ")
        a,b = b,a+b
    return a
febo(12)

# lst= [[1, 2, [3]], [4, 5], [6, [7, 8]]]
#
# e_lst= []
# # for i in lst:
# #     for j in i:
# #         e_lst.append(j)
# #
# # print(e_lst)
#
# for i in lst:
#     if isinstance(i, list):
#         e_lst.extend(lst(i))
#     else:
#         e_lst.append(i)
# print(e_lst)

