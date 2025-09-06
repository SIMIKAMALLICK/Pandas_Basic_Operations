list=[
    "Welcome to python\n",
    "Lets learn list\n",
    "Lets learn pandas\n",
    "Lets learn numpy\n"
]

w=open('simika1.txt','w')
w.writelines(list)      #it will write all contents of the list to the file

w.close()