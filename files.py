
myfile='nums.txt'
sum=0
with open(myfile) as f:
   # print(f)
    for i in f:
        i=i.strip()
        sum=sum+int(i)
print(sum)
