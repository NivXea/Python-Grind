import pandas as pd

Original Data:
data = {
    "Name": ["Ram", "Shyam", "Ghanshyam", "Dhanshyam", "Aditi", "Jagdish", "Raj", "Simran"],
    "Age": [28, 34, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, 90, 78, 92, 88, 95, 80, 89]
}
______________________________________________________________________________________________________________________________________________________________________________________________
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

NOTE: Removing Rows and Columns is too risky so
___________________________________________________________________________________________________________________________________________________________________________________________
#Filling Missing Values with Any Default Value
Syntax: df.fillna(default value , inplace= True/False)

df.fillna(0 , inplace= True)
print(df)

Output:
---------------------------------------------------------------------------
        Name   Age   Salary  Performance Score
0        Ram  28.0  50000.0               85.0
1          0   0.0      0.0                0.0
2  Ghanshyam  22.0  45000.0               78.0
3  Dhanshyam  30.0  52000.0               92.0
4      Aditi  29.0  49000.0               88.0
5    Jagdish  40.0  70000.0               95.0
6        Raj  25.0  48000.0               80.0
7     Simran  32.0  58000.0               89.0
---------------------------------------------------------------------------

NOTE: 0 is not good so fill the missing values with mean of available values

df['Salary'].fillna(df['Salary'].mean() , inplace= True)
print(df)

Output:
---------------------------------------------------------------------------------------------------------------------
        Name        Age        Salary  Performance Score
0        Ram  28.000000  50000.000000          85.000000
1       None  29.428571  53142.857143          86.714286
2  Ghanshyam  22.000000  45000.000000          78.000000
3  Dhanshyam  30.000000  52000.000000          92.000000
4      Aditi  29.000000  49000.000000          88.000000
5    Jagdish  40.000000  70000.000000          95.000000
6        Raj  25.000000  48000.000000          80.000000
7     Simran  32.000000  58000.000000          89.000000
----------------------------------------------------------------------------------------------------------------------
____________________________________________________________________________________________________________________________________________________________________________________________
#InterPolate Method
-> Sometimes to maintain data integrity and flow, pandas interpolate method fills the missing values via estimating it to its near surrounding data values

Syntax: df.interpolate(method= "linear"/"polynomial"/"time" , axis= 0 , inplace= True)

data = {
    "Time": [1 , 2 ,3 ,4 ,5],
    "Value": [10 , None ,30 ,None , 50]
}
df = pd.DataFrame(data)
print("Before Interpolation")
print(df)
print("After Interpolation")
df['Value'] = df['Value'].interpolate(method="linear", axis=0)
print(df)

Output:
------------------------------------------------------------------------------
   Time  Value
0     1   10.0
1     2    NaN
2     3   30.0
3     4    NaN
4     5   50.0
After Interpolation
   Time  Value
0     1   10.0
1     2   20.0
2     3   30.0
3     4   40.0
4     5   50.0
-------------------------------------------------------------------------------
NOTE: This Can be Used in Timer Based Data or When Working with Numerical Data set where a pattern is followed

__________________________________________________________________________________________________________________________________________________________________________________________


