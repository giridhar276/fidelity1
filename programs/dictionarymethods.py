book = {"chap1":10 , "chap2":20,"chap3":30, "chap1":100}
print(book)

### add new key-value pairs
book["chap4"] = 40
book["chap5"] = 50
book["chap6"] = 40
print(book)

# display individual value
print(book["chap1"])
print(book["chap2"])
print(book["chap3"])

####################
# display keys
print(book.keys())


for key in book.keys():
    print(key)

######################
# display values
print(book.values())


for value in book.values():
    print(value)

# display key value pair
print(book.items())

for key,value in book.items():
    print(key,value)



book.pop("chap1") # chap1-100 will be removed from dictionary
print("after pop operation :",book)
book.popitem()
print("after popitem() :",book)