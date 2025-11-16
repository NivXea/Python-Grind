#Sorting Data

//Sorting Data in Columns
Syntax: df.sort_values(by=["Column_name" , etc..] , ascending=[True/False , True/False , etc..] , inplace=True/False) --> Here ascending=True is to sort in ascending order and 
False to sort in descending order

data = {
  "Name" : [ "Arun" , "Varun" , "Shreya"],
  "Age": [ 40 , 18 , 32],
  "Salary": [ 50000 , 60000 , 70000]
}

df = pd.DataFrame(data)
df.sort_values(by=["Age" , "Salary"] , ascending=[False , True] , inplace=True)
print(df)

Output:
--------------------------------
     Name  Age  Salary
0    Arun   40   50000
2  Shreya   32   70000
1   Varun   18   60000
--------------------------------
__________________________________________________________________________________________________________________________________________________________________________________________
#Grouping 
Syntax: grouped = df.groupby(["column1" , "column2" , ..])

__________________________________________________________________________________________________________________________________________________________________________________________
#Common Methods
1. mean()
2. min()
3. max()
4. std() --> standard deviation of values
5. count() --> count of all none NAN values

__________________________________________________________________________________________________________________________________________________________________________________________
#Merging and Joining
Syntax: df_merged = pd.merge(df1 , df2 , on="Column_name" , how="inner/outer/left/right") 
On="Column Name" is the name of common column where u wanna merge

#Customer DF
df1 = pd.DataFrame({
    "Customer ID" : [1,2,3,],
    "Name": ["Akshay" , "Aman" , "Arceus"]
})
#Order DF
df2 = pd.DataFrame({
    "Customer ID" : [1 , 3 , 5],
    "Order Amt": [250 , 450 , 440]
})
#Merging Both DF's

1. Inner --> Jinki Keys(Customer ID) match hogi sirf wahi return honge)
df_merged = pd.merge(df1 , df2 , on="Customer ID" , how="inner" )

Output:
-----------------------------------------------
   Customer ID    Name  Order Amt
0            1  Akshay        250
1            3  Arceus        450
-----------------------------------------------

2. Outer --> Union of Sets ki Tarah
df_merged = pd.merge(df1 , df2 , on="Customer ID" , how="outer" )

Output:
----------------------------------------
   Customer ID    Name  Order Amt
0            1  Akshay      250.0
1            2    Aman        NaN
2            3  Arceus      450.0
3            5     NaN      440.0
----------------------------------------

3. Left --> df1 ki Customer ID's ka info aayega
df_merged = pd.merge(df1 , df2 , on="Customer ID" , how="left" )

Output:
----------------------------------------------
   Customer ID    Name  Order Amt
0            1  Akshay      250.0
1            2    Aman        NaN
2            3  Arceus      450.0
----------------------------------------------


4. Right --> df2 ki Customer ID's Ka Info Aayega
df_merged = pd.merge(df1 , df2 , on="Customer ID" , how="right" )

Output:
----------------------------------------------
   Customer ID    Name  Order Amt
0            1  Akshay        250
1            3  Arceus        450
2            5     NaN        440
-----------------------------------------------

5. Cross --. If df1 has m rows and df2 has n rows then crossed df will have m*n rows
df_merged = pd.merge(df1 , df2  , how="cross" )

Output:
--------------------------------------------------------
   Customer ID_x    Name  Customer ID_y  Order Amt
0              1  Akshay              1        250
1              1  Akshay              3        450
2              1  Akshay              5        440
3              2    Aman              1        250
4              2    Aman              3        450
5              2    Aman              5        440
6              3  Arceus              1        250
7              3  Arceus              3        450
8              3  Arceus              5        440
---------------------------------------------------------
____________________________________________________________________________________________________________________________________________________________________________________________
#Concatenation
Syntax: df.concat([df1 , df2, ...] , axis= 0/1 , ignore_index= True)
[df1 , df2 , ...] is the list of DF's which has to be concatenated.
axis = 0/1 is to concatenate Vertically(Row-wise)/Horizonatlly(Column-wise) --> axis = 0 is by default

Ex:
#Region 1
df1 = pd.DataFrame({
    "Name" : ["Shreya" , "Shub"],
    "Age": [21 , 34]
})
#Region 2
df2 = pd.DataFrame({
    "Name": ["Akshay" , "Aman"],
    "Age" : [ 17 , 18]
})
#Concatenated DF
df3 = pd.concat([df1,df2] , axis= 0 , ignore_index= True)

Output:
--------------------------------------------------
     Name  Age
0  Shreya   21
1    Shub   34
2  Akshay   17
3    Aman   18
--------------------------------------------------

and if axis= 1:
Output:
---------------------------------------------------------
        0   1       2   3
0  Shreya  21  Akshay  17
1    Shub  34    Aman  18
---------------------------------------------------------
_____________________________________________________________________________________________________________________________________________________________________________________________
