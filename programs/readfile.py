# method1 - reading the file line by line
with open("languages.txt","r") as fobj:
    for line in fobj:
        print(line.strip())

# method2 - reading using fobj.readlines()  returns list
with open("languages.txt","r") as fobj:
    print(fobj.readlines())


# method3 - using fobj.read()  returns single string
# not suggested on larger files
with open("languages.txt","r") as fobj:
    print(fobj.read())

# method4 - using csv library  - Advantage: each line will be converted to list
import csv 
with open("languages.txt","r") as fobj:
    reader = csv.reader(fobj)
    for line in reader:
        print(line)


import json 
with open("languages.json","r") as fobj:
    data = json.load(fobj)





# method5 - using pandas library
# pip install pandas
import pandas as pd

df = pd.read_csv("languages.txt", header=None)
print(df.head(2))
