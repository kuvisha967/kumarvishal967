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


nums = [1,2,2,3,3,3]
k = 2

num2 = []
# numss= nums.count(2)
# print(numss)


for i in nums:
    if nums.count(i) == k:
        num2.append(i)
print(num2)