class Student():    #定义一个学生类
    def __init__(self,name,age):  #学生的姓名、年龄
        self.name = name
        self.age = age
        self.grades = {"语文":0,"数学":0,"英语":0}    #字典存储每科的成绩

    def set_grade(self,course,grade):   #设置成绩
        self.grades[course] = grade

    def print_grade(self):        #打印成绩
        print(self.grades)

class BigStudent(Student):     #大学生继承父类的初始化、设置成绩等
    def delete_grade(self,course):
        self.grades[course] =0

gy=BigStudent("甘烨",20)
gy.set_grade("语文",60)
gy.set_grade("英语",80)   #设置成绩是调用的父类用法
print(gy.grades)
gy.delete_grade("语文")     #删除成绩用的是子类用法
print(gy.grades)
