num=[1,2,6,4,5,1]    #定义一个num列表（类似C语言的数组）
print(num[0])
print(sorted(num))        #直接帮你排好序
print(min(num))           #min,max你懂的
print(max(num))

ganye=["甘烨",2004,4,10]  #列表可以存储不同数据类型，灰常方便
print(ganye[0])
print(ganye[1])

num.append(100)      #调用append方法，将100存到列表里
print(num)

num.remove(1)   #remove方法，去掉数组元素，但是如果有两个一样的，他只会去掉第一个
print(num)

num[1]="我是天帝"    #直接修改第二个元素
print(num)