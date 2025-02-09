class Student():    #定义一个学生类
    def __init__(self,name,age):  #学生的姓名、年龄
        self.name = name
        self.age = age
        self.grades = {"语文":0,"数学":0,"英语":0}    #字典存储每科的成绩

    def set_grade(self,course,grade):   #设置成绩
        self.grades[course] = grade

    def print_grade(self):        #打印成绩
        print(self.grades)

student1=Student("甘烨",20)
student1.set_grade("英语",50)   #英语设置成50分
student1.print_grade()    #打印
student1.set_grade("数学",100)      #数学一百
print(student1.grades)    #打印