f=open('info.txt','r')
print(f.read(10))  #number of charecters can be read


print('-'*40)
print(f.readlines(2))

for i in f:
    print(i)

f.close()