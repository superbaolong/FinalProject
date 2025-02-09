#for
for i in range(5,10):    #range是≥开始值，小于结束值
    print(i)

for i in range(5,10,2):   #2是步长
    print(i)

sum=0
for i in range(1,101):
    sum+=i   #计算1加到100
print(sum)

#while
i=0
sum=0
while i<=100:
    sum+=i
    i+=1
print(sum)