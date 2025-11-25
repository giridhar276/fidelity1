
#p   y    t   h     o     n        p   r   o    g    r   a   m   m   i     n     g
#0   1    2   3     4     5   6    7   8   9    10  11  12   13  14  15    16   17
#                                                                    -3    -2    -1      
name = "python programming"
# string slicing
# string[start:stop:step]
print(name[0])  #p
print(name[1])  #y
print(name[0:4]) 
print(name[0:4:1])
print(name[0:18])   # python programming
print(name[0:18:1]) # python programming
print(name[0:18:2]) # pto rgamn
print(name[-1])  #g
print(name[-2])  #n

print(len(name))  # display length of the string
print(name)
print(name[:])
print(name[::])
print(name[::1])
print(name[::-1])  #gnimmargorp nohtyp

print(name[0:-2])
# string methods



name = "python programming"
print(name.capitalize()) 
print(name.title())
print(name.count("p"))
print(name.count("P"))
print(name.center(40))
print(name.center(40,"*"))
print(name.endswith("g"))
print(name.endswith("a"))
print(name.startswith("p"))
print(name.replace("python","java"))
print(name)   # we are not modifying actual string

print(name.isupper())   # we are validating
print(name.upper())     # displaying string in uppercase
print(name)
print(name.islower())
print(name.lower())

alist = ["python","java"]
output = ":".join(alist)   # converting list to string
print(output)

name = " python   "
print(len(name))
print(len(name.strip()))  # remove whitespaces at both ends
print(len(name.lstrip())) # only at left side
print(len(name.rstrip())) # only at right side

aname = "python:programming"
print(aname.split(":"))

#### concatenation  #### combining
first = "python"
second = "programming"
print(first + second)
print(first + second + "langauge")
print(first + " " +  second + " " +  "langauge")


# check for substring
# method1
name = "python programming"

print(name.find("pr"))  # if substring found... if returns the index of substring

print(name.find("abc"))   # if not found.... returns -1


# method2
if 'prog' in name :

    print("substring found")
    
else:
    print("not found")


if 1 < 2 :
    print("true")
    print("inside if")
    print("still inside if")
else:
    print("false")