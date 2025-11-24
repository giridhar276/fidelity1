
alist = [34,67,16,81,83,36,68,34,34]
print(len(alist))
print(alist.count(34))
alist.append(74)   # alist.append(value)
print("After appending:",alist)
alist.extend([85,53,59])
print("After extending:",alist)
alist.insert(1,95)
print("After inserting :",alist)
alist.pop(1)   # alist.pop(index) - value at the index is removed
print("After pop operation :",alist)
alist.remove(34) # list.remove(value) - value gets removed directly
print("AFter removing :",alist)
alist.reverse()
print("After reversing :",alist)
alist.sort()
print("sorting in ascending order:",alist)
alist.sort(reverse=True)
print("sorting in descending order:",alist)

#### always validate
if 340 in alist:
    alist.remove(340)
    print("value removed")
else:
    print("value not found")




alist = [34,67,16,81,83,36,68,34,34]
### display all the numbers from 1 to 10
# range(start,stop,step)
for i in range(1,11): # excluding 11
    print(i)
# display odd numbers
for i in range(1,11,2):
    print(i)
## display even numbers
for i in range(2,11,2):
    print(i)

## reading each element in list
for value in alist:
    print(value)
# reading each character from the string
name = "python"
for char in name:
    print(char)

name = "python"
for i in range(0,len(name)):   # range(0,6)
    print(name[i])