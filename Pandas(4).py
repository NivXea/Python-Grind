#Sorting Data

//Sorting Data in 1 column
Syntax: df.sort_values(by="Column_name" , ascending=True/False , inplace=True/False) --> Here ascending=True is to sort in ascending order and False to sort in descending order

data = {
  "Name" : [ "Arun" , "Varun" , "Shreya"],
  "Age": [ 40 , 18 , 32],
  "Salary": [ 50000 , 60000 , 70000]
}

df = pd.DataFrame(data)
df.sort_values(by="Age" , ascending=False , inplace=True)
print(df)

Output:
--------------------------------
     Name  Age  Salary
0    Arun   40   50000
2  Shreya   32   70000
1   Varun   18   60000
--------------------------------





