import pandas as pd

df = pd.read_csv('C:/Users/Personal/Desktop/SF_Sample_Data_Files/emp_data/emp_sal_prep.csv')
# print(df)

print(df.shape)
rows, columns = df.shape
print(columns)

df.head()
# prints first few samples
df.head(5)
# prints first 5 rows
df.tail()
# prints last few samples
print(df[2:5])
# print from rows 2 to 5 which does not include row 5.
# rows in df starts from 0 so above code returns 3rd record to 5th record in a given table
print(df[:])
print(type(df['GENDER']))
# <class 'pandas.core.series.Series'>
print(type(df))
# <class 'pandas.core.frame.DataFrame'>
print(df[['NAME', 'GENDER']])
print(df['SALARY'].mean())
print(df.describe())
# above code prints statics of any columns with numerics in df

# conditionally selecting data
print(df[df.SALARY > df.SALARY.mean()])
# we can also the below syntax if the column name has spaces
print(df[df.SALARY > df['SALARY'].mean()])

# print name and department of the employee with highest salary
print(df[['NAME', 'DEPARTMENT']][df.SALARY == df['SALARY'].max()])

# Reading Files
# CSV or Excel
# Header related functions

# Skip Header
# df = pd.read_csv("file_name/path", skiprows = 1) skips the first row
# header = 1 will also do the same, as index starts from 0 header will be 1 when you want to skip first row
# header = None is when you want no header from your input file
# but when you choose none the column name s would be numerics 0,1,2,3 to name them we can use
# df  = pd.read_csv("file_name/path", header = None, name ="cl1_name", "cl2_name")

# Read limited records from a file
# df  = pd.read_csv("file_name/path", nrows=3)

# Basics of cleaning data
# Replacing given values with NaN
