
info = {
"id": "0001",
"type": "donut",
"name": "Cake",
"image":
{
"url": "images/0001.jpg",
"width": 200,
"height": 200
},
"thumbnail":
{
"url": "images/thumbnails/0001.jpg",
"width": 32,
"height": 32
}
}

val = 10 
print(isinstance(val,int))
print(isinstance(val,list))
print(isinstance(val,dict))
alist = [10,20,30]
print(isinstance(alist,list))
print(isinstance(alist,int))
print(type(alist))
print(type(val))


for key,value in info.items():
    if isinstance(value,str):
        print(key.ljust(15),":",value)
    elif isinstance(value,dict):
        for skey,svalue in value.items():
            finalkey = key + skey
            print(finalkey.ljust(15),":",svalue)
