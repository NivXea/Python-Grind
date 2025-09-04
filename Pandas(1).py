import pandas as pd
__________________________________________________________________________________________________________________________________________________________________________________________
// Reading Different types of data with Pandas //
#CSV DATA
csv = pd.read_csv("file.csv" , encoding="unt-8"/"latin1")

#EXCEL DATA
exl = pd.read_excel("file.xlsx")

#JSON DATA
json = pd.read_json("File.json")

#Creating Your Own DATAFRAME
data = {
  "Name":['AKSHAY' , "AMAN" , "MANAN"],
  "Age":[17 , 18 , 16],
  "City":["NathuPura" , "Amrit Vihar" , "Ib"]
}

df = pd.DataFrame(data)
print(df) #This Will create A good view of data inside
_________________________________________________________________________________________________________________________________________________________________________________________
// Converting DATA //
Just use: 
df.to_csv("Name.csv" , index=False)
df.to_excel("Name.xlsx" , index=False)  #The files will be saved in the folder with their respective names and no unnecessary index is saved
df.to_json("Name.json" , index=False)

________________________________________________________________________________________________________________________________________________________________________________________
// Reading First and last Rows of any DataFrame using pandas
import pandas as pd

df = pd.read_json("sample_data.json")
print("5 Rows of DataFrame")
print(df.head(5)) #df.head(n) prints first n rows and df.tail(n) prints last n rows of DataFrame... 
print("\n")
_________________________________________________________________________________________________________________________________________________________________________________________
// Info of A DataFrame //

#df.info() is a method which tells about no. of rows and column, Dtype(int64 , float64, object) , Memory usage , Non Null(means value is not missing).. 

  
data = {
  "Name":['AKSHAY' , "AMAN" , "MANAN"],
  "Age":[17 , 18 , 16],
  "City":["NathuPura" , "Amrit Vihar" , "Ib"]
}

df = pd.DataFrame(data)
print(df.info())

THIS WILL BE THE OUTPUT
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
RangeIndex: 3 entries, 0 to 2        
Data columns (total 3 columns):      
 #   Column  Non-Null Count  Dtype   
---  ------  --------------  -----   
 0   Name    3 non-null      object  
 1   Age     3 non-null      int64
 2   City    3 non-null      object
dtypes: int64(1), object(2)
memory usage: 200.0+ bytes
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
________________________________________________________________________________________________________________________________________________________________________________________
import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Ghanshyam", "Dhanshyam", "Aditi", "Jagdish", "Raj", "Simran"],
    "Age": [28, 34, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, 90, 78, 92, 88, 95, 80, 89]
}


df = pd.DataFrame(data)
print("Sample DataFrame:")
print(df)
print("\n")

print("DataFrame Description:")
print(df.describe())

OUTPUT WILL BE:
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
             Age        Salary  Performance Score
count   8.000000      8.000000           8.000000 #Count of all non missing values
mean   30.000000  54000.000000          87.125000 #Mean of All non Missing Values
std     5.529144   8194.074514           5.817154 #Std deviation 
min    22.000000  45000.000000          78.000000 #min value in that list
25%    27.250000  48750.000000          83.750000 #25%ile of data 
50%    29.500000  51000.000000          88.500000
75%    32.500000  58500.000000          90.500000
max    40.000000  70000.000000          95.000000 #Max value in that list
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
________________________________________________________________________________________________________________________________________________________________________________________
// Shape and Columns //
data = {
    "Name": ["Ram", "Shyam", "Ghanshyam", "Dhanshyam", "Aditi", "Jagdish", "Raj", "Simran"],
    "Age": [28, 34, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, 90, 78, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)

print("Sample DataFrame:")
print(df)
print(f"Shape: {df.shape}")  # Prints the shape of the DataFrame (rows, columns) ---> Shape: (8, 4)
print(f"Columns: {df.columns}")  # Prints the list of column names ---> Columns: Index(['Name', 'Age', 'Salary', 'Performance Score'], dtype='object')
_________________________________________________________________________________________________________________________________________________________________________________________
// Selecting And Filtering Data //

SYNTAX:
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
SELECTION
single_column = df['Column name']
multiple_column = df['column1' , 'column2']

FILTERING
single_condition = df[df['column'] > 30000]
multiple_condition = df[(df['column1'] > 30000) & (df['column2'] > 90)]
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
data = {
    "Name": ["Ram", "Shyam", "Ghanshyam", "Dhanshyam", "Aditi", "Jagdish", "Raj", "Simran"],
    "Age": [28, 34, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, 90, 78, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)

#Selecting a single column
print("Selecting a single column (Name):")
name = df["Name"]
print(name) #Returns a Series

#Selecting multiple columns
print("\nSelecting multiple columns (Name and Salary):")
name_salary = df[["Name", "Salary"]]    
print(name_salary) #Returns a DataFrame

#Filtering rows based on 1 single condition
higher_salary = df[df["Salary"] > 50000]
print("\nFiltering rows where Salary > 50000:")
print(higher_salary)

#Filtering rows based on multiple conditions
high_performers = df[(df["Salary"] > 50000) & (df["Performance Score"] > 92)] #& is AND and | is OR 
print("\nFiltering rows where Salary > 50000 and Performance Score > 92:")
print(high_performers)

_________________________________________________________________________________________________________________________________________________________________________________________
