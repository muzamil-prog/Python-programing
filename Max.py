print("find largest number in list")
list=[10, 20, 30, 50, 70]
larger=list[0]
for i in list:
    if(larger<i):
        larger=i
        print(larger)