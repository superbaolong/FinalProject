#加函数
def sum(a,b):
    return a+b
#max函数
def max(a,b):
    return a if a > b else b

print(sum(1,2),max(2,8))

#写一个BMI计算的函数
def calculate(height,weight):
    BMI=weight/(height*height)
    if BMI < 18.5:
        print("您偏瘦")
    elif BMI<=25:
        print("您体型正常")
    elif BMI<=30:
        print("您体型偏重")
    else:
        print("你太特么胖了")
    return BMI

height=float(input("您的身高是（单位m）："))
weight=float(input("您的体重是（单位kg）"))
your_bmi = calculate(height,weight)
print("您的BMI是：",your_bmi)