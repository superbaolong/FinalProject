#元组，圆括号。类似列表，但是不可变,也就是不可以append remove啥的
a=(1,2,3)
print(a[0])

#字典，花括号,可变，但是元素类型不能变
b={1:'甘烨',2:'天帝'}
print(b[1])
b[3]="神仙"
print(b[3])
b[10086]="联通客服"
print(b[10086])

print(b.keys())    #键
print(b.values())   #值
print(b.items())    #键值对