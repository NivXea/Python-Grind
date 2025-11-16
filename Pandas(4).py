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
Syntax: df_merged = pd.merge(df1 , df2 , on="Column_name" , how="inner/outer/left/right") --> On="Column Name" is the name of common column where u wanna merge

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
df_merged = pd.merge(df1 , df2 , on="Customer ID" , how="outer" )








