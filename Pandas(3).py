import pandas as pd

Original Data:
data = {
    "Name": ["Ram", "Shyam", "Ghanshyam", "Dhanshyam", "Aditi", "Jagdish", "Raj", "Simran"],
    "Age": [28, 34, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, 90, 78, 92, 88, 95, 80, 89]
}
________________________________________________________________________________________________________________________________________________________________________________________________
#Detecting Missing Values
data = {
    "Name": ["Ram", None, "Ghanshyam", "Dhanshyam", "Aditi", "Jagdish", "Raj", "Simran"],
    "Age": [28, None, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, None, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, None, 78, 92, 88, 95, 80, 89]
}

Synatx: df.isnull() --> Return a boolean value (True if Data is Missing else Returns False)

df = pd.DataFrame(data)
print(df.isnull())

Output:
--------------------------------------------------------------------------------------
    Name    Age  Salary  Performance Score
0  False  False   False              False
1   True   True    True               True
2  False  False   False              False
3  False  False   False              False
4  False  False   False              False
5  False  False   False              False
6  False  False   False              False
7  False  False   False              False
------------------------------------------------------------------------------------
and to find total number of missing values-
Syntax: df.isnull().sum()

print(df.isnull().sum())
Output:
--------------------------------
Name                 1
Age                  1
Salary               1
Performance Score    1
dtype: int64
-------------------------------
_____________________________________________________________________________________________________________________________________________________________________________________________
#Removing Rows and Columns with those missing Values
Syntax: df.dropna(axis = 0/1 , inplace= True/False) --> axis= 0 (remove rows) & axis= 1 (remove columns)

df.dropna(axis=0 , inplace= True)
print(df)

Output:
-----------------------------------------------------------------
        Name   Age   Salary  Performance Score
0        Ram  28.0  50000.0               85.0
2  Ghanshyam  22.0  45000.0               78.0
3  Dhanshyam  30.0  52000.0               92.0
4      Aditi  29.0  49000.0               88.0
5    Jagdish  40.0  70000.0               95.0
6        Raj  25.0  48000.0               80.0
7     Simran  32.0  58000.0               89.0
-----------------------------------------------------------------

df.dropna(axis= 1 , inplace= True)
print(df)

Output:
-----------------------------------------------------------------
Empty DataFrame
Columns: []
Index: [0, 1, 2, 3, 4, 5, 6, 7]
-----------------------------------------------------------------





























