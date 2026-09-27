sum=0
count=0
while True:
    n=int(input("please enter the number:"))
    sum+=n
    count+=1
    if(n==0):
        break
print("Sum of number which user are add without zero:", sum)
print("the user total number are add:", count)    