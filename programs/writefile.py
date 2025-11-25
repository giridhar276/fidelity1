## regular way # traditional way
fobj = open("customers.txt","w")
fobj.write("tcs\n")
fobj.write("cts\n")

fobj.writelines(["infy\t","oracle\t","microsoft\n"])
for val in range(1,10):
    fobj.write( str(val )+ "\n")
fobj.close()

# pythonic way # modern way
# context manger
# if any line begins using with keyword .. it is called as context manager
# Advantage: file gets closed automatically when it comes out of indentation
with open("customers.txt","w") as fobj:
    fobj.write("tcs\n")
    fobj.write("cts\n")
    print(fobj.closed) # file is not closed hence False
print(fobj.closed) # True 