
#list
alist = [10,20,30]
alist[0] = 100
print("after changes :", alist)


# tuple
atup = (10,20,30)
#atup[0] = 1000
print("After changes :",atup)


# typecasting- converting from one object to another object
atup = (10,20,30)
alist = list(atup) # step1: converting to list
alist.append(40)   # step2: making changes
atup = tuple(alist)# step3: reconverting back to tuple
print("After changes :",atup)

# list of lists
empdb = [["rita",'1-1-1','US'],['sita','2-2-2','UK']]

# list of tuples
empdb = [("rita",'1-1-1','US'),('sita','2-2-2','UK')]