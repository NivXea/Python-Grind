# Adding Columns
import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Ghanshyam", "Dhanshyam", "Aditi", "Jagdish", "Raj", "Simran"],
    "Age": [28, 34, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, 90, 78, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)

To add new columns there are 2 Method (To make a new column) & (Using Insert Method)
1. Making a New Column
Syntax: df["New_Column_Name"] = some_data 

df["Bonus"] = df['Salary'] * 0.1
print(df)

Output:
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        Name  Age  Salary  Performance Score   Bonus
0        Ram   28   50000                 85  5000.0
1      Shyam   34   60000                 90  6000.0
2  Ghanshyam   22   45000                 78  4500.0
3  Dhanshyam   30   52000                 92  5200.0
4      Aditi   29   49000                 88  4900.0
5    Jagdish   40   70000                 95  7000.0
6        Raj   25   48000                 80  4800.0
7     Simran   32   58000                 89  5800.0
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
2. Using insert() Method
Syntax: df.insert((location or index number) , "New_column_name" , data)
This Helps a lot in adding columns in precise locations..


df.insert( 0 , "Employee ID" , [1,2,3,4,5,6,7,8])
print(df)

Output:
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   Employee ID       Name  Age  Salary  Performance Score
0            1        Ram   28   50000                 85
1            2      Shyam   34   60000                 90
2            3  Ghanshyam   22   45000                 78
3            4  Dhanshyam   30   52000                 92
4            5      Aditi   29   49000                 88
5            6    Jagdish   40   70000                 95
6            7        Raj   25   48000                 80
7            8     Simran   32   58000                 89
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
_______________________________________________________________________________________________________________________________________________________________________________________________
#Updating Values in a DataFrame
Syntax: df.loc[rows_index , "Column_name"] = new_value

df.loc[0 , "Name"] = "AKSHAY"
print(df)

Output:
-------------------------------------------------------------------------------------------------
        Name  Age  Salary  Performance Score
0     AKSHAY   28   50000                 85
1      Shyam   34   60000                 90
2  Ghanshyam   22   45000                 78
3  Dhanshyam   30   52000                 92
4      Aditi   29   49000                 88
5    Jagdish   40   70000                 95
6        Raj   25   48000                 80
7     Simran   32   58000                 89
-------------------------------------------------------------------------------------------------
______________________________________________________________________________________________________________________________________________________________________________________________
#Removing Columns
Syntax: df.drop(columns= ["Column1_name" , "Column2_name"] , inplace= True/False) ---> inplace= True modifies original data while inplace= False returns a new dataframe

df.drop(columns= ["Performance Score" , "Age"] , inplace= True)
print(df)

Output:
-------------------------------
        Name  Salary
0        Ram   50000
1      Shyam   60000
2  Ghanshyam   45000
3  Dhanshyam   52000
4      Aditi   49000
5    Jagdish   70000
6        Raj   48000
7     Simran   58000
-------------------------------
 
















































