# import pandas as pd
#
# data = {"Name":["Vishal","Anamika","Ankush","Riya","Unu"],
#         "Age":[28,25,21,25,"NA"],
#         "Ocupation":["IT","Digital","Study","Study",""]}
# df = pd.DataFrame(data)
# # print(df)
# # df1 = df.fillna("null")
# df1 = df.dropna()
# # print(df1)
#
# for i in df.columns:
#         if df[i].dtype == 'object':
#                 df[i] = df[i].fillna(df[i].mode()[0])
#         else:
#                 df[i] = df[i].fillna(df[i].median())
# # print(df)
#
# # df.to_csv(r'E:\python\fm.csv', index=False)
# # n_df = pd.read_csv("fm.csv")
# # print(n_df)
#
# age_col = df['Age']
# # print(age_col)
# # print(df.index)
#
# df_set_indx = df.set_index('Name')
# # print(df_set_indx)
# df_reset = df.reset_index()
# # print(df_reset)
#
# secnd_row = df.iloc[0]
# # print(secnd_row)
#
# subset = df.loc[0:2, ['Name','Age']]
# # print(subset)
#
# # filtr = df[df['Age']>21]
# # print(filtr)
#
# flrt_at = df.at[2,'Ocupation']
# # print(flrt_at)
#
#
#
# import pandas as pd
#
# # df = pd.read_csv("Employee.csv", usecols = ['Education','JoiningYear'])
# # df = pd.read_csv("Employee.csv",nrows=3)
# # print(df)
#
# df = pd.read_csv("Employee.csv")
# # print(df.iloc[0:2,[2]])
# # print(df.count())
# # print(df.head())
# # print(df.tail())
# rs= df.query("JoiningYear==2013")
# # print(rs)

import pandas as pd

# df = pd.read_csv(r'/FileStore/tables/cleaned_student_admission_record_dirty.parquet')
# print(df.head())
# print(df.count())

#checking for null
# null_chk = df.isnull().sum()
# print(null_chk)

# droping missing value
# df_cln = df.dropna()
# print(clean_df)

# filling missing value
# df_cln = df.fillna('0')
# print(df_cln)

import pyarrow
# prqt_df = df_cln.to_parquet(r'E:\dataset\cleaned_student_admission_record_dirty.parquet', engine = "pyarrow", index=False)


# df1 = pd.read_parquet(r'F:\dataset\cleaned_student_admission_record_dirty.parquet', engine = "pyarrow")

# print(df1.head())
# print(df1.count())

# /FileStore/tables/student_admission_record_dirty.csv
# /FileStore/tables/student_admission_record_dirty-1.csv

import pandas as pd

df = pd.read_csv(r'F:\dataset\student_admission_record_dirty.csv')

# print(df.head())

# print(df.isnull().sum())
# print(df.isna().sum())
print(df.notnull().sum())

# print(df.columns)
#
# for col in df.columns:
#     if df[col].dtype == 'object':
#         df[col]

cln_df = df.dropna(axis=0, how='any')
print(cln_df.notnull().sum())

print(len(df) - len(cln_df))
# print(len(cln_df) - len(df))

df1 = cln_df.to_parquet(r'D:\cleaned_emp_data.parquet', engine='pyarrow',index=False)
df2=pd.read_parquet(r'D:\cleaned_emp_data.parquet', engine='pyarrow')
print(df2.head())
print(df2.count())