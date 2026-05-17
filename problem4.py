import os

# current directory ka path
path = "/new folder"

# directory ke contents lena
contents = os.listdir(path)

# contents print karna
print("Directory contents are:")

for item in contents:
    print(item)