import os
import sys
try:
    filename = "languages111.txt"
    if os.path.isfile(filename):
        with open(filename,"r") as fobj:
            for line in fobj:
                print(line.strip())
    else:
        print(filename," is not found")
except Exception as e:
        print(e)
        print("file not found")
        print(sys.exc_info())


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
