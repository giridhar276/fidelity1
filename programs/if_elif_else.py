####### simple if
lang = input("Enter any language :")
if lang in "python programming":
    print("you are leanring python")

######## if-else
lang = input("Enter any language :")

if lang  == "python":
    print("you are leanring python")
else:
    print("you are learning java")


####### if-elif-elif-else
lang = input("Enter any language :")
if lang in "python programming":
    print("you are leanring python")
elif lang in "java programming":
    print("you are learning java")
elif lang in "unix shell scripting":
    print("you are learning unix")
else:
    print("you are learning gen ai")