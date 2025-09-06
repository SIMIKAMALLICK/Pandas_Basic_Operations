import pandas as pd

empdata=[
    (10,'Simika',30000,'Kolkata'),
    (20,'Anubhav',40000,'Pune'),
    (30,'Shruti',50000,'Bangalore'),
    (40,'Monalisa',60000,'Goa'),
    (50,'Ishika',70000,'Kashmir')
]

df=pd.DataFrame(empdata,columns=['id','name','salary','city'])
print(df)

# loc()=> locate() data using columns labels

print('-'*30)
df1=df.loc[:,['name','salary']]
print(df1)

# iloc()=> locate() data using columns index
print('-'*30)
df2=df.iloc[:3,[0,2,3]]
print(df2)