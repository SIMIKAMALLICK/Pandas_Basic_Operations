import pandas as pd
players1=pd.DataFrame(
    {
        'name':['Dravid','Kohli','Kambli'],
        'age': [34,32,34]
    }
)
players2=pd.DataFrame(
    {
        'name':['Dravid','Kohli','singh'],
        'height': [6.5,6.5,6.5]
    }
)
print(players1)
print(players2)
print('-'*30)
print(pd.merge(players1,players2,on='name',how='inner'))
print('-'*30)
print(pd.merge(players1,players2,on='name',how='left'))
print('-'*30)
print(pd.merge(players1,players2,on='name',how='right'))
print('-'*30)
print(pd.merge(players1,players2,on='name',how='outer'))
