def swapFileData():

    fileA=input("enter your first file path")
    fileB=input("enter your second file path")
    with open(fileA,'r') as a:
        data_a=a.read()
    with open(fileB,'r') as b:
        data_b=b.read()
    with open(fileA,'w') as a:
        a.write(data_b)
    with open(fileB,'w') as b:
        b.write(data_a)

swapFileData()