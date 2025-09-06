import pandas as pd

empdata={
    "id":[1,2,3,4,5],
    "name":['Simika','Anubhav','Shruti','Monalisa','Ishika'],
    "salary":[30000,40000,50000,60000,70000],
    "city":["Kolkata","Bangalore","Pune","Goa","Kashmir"]
}

df1=pd.DataFrame(empdata)
print(df1)

for index, row in df1.iterrows():
    print("{} has the salary of {}".format(row['name'], row['salary']))
