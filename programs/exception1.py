
try:
    with open("languages111111111111.txt","r") as fobj:
        for line in fobj:
            print(line.strip())
except Exception as err:
        print(err)
        print("file not found")


try:
    with open("languages111111111111.txt","r") as fobj:
        for line in fobj:
            print(line.strip())
except ValueError as err:
    print(err)
except TypeError as err:
    print(err)
except (IndexError,KeyError) as err:
    print(err)
except Exception as err:
    print(err)
