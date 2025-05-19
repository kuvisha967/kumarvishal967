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




