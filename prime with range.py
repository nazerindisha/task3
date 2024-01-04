start=int(input("enter a number :"))
end=int(input("enter the last number:"))
for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
            if num%2==0:
              break
        else:
            print(num)    