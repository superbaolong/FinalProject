print("今天可以打游戏吗？")
mood_index=int(input("对象今天心情指数："))
if mood_index>=60:
    print("今天应该可以打游戏")      #条件语句啥也不想写可以写个pass
    print("哈哈哈(^∇^)")
elif(mood_index>40):
    print("小心翼翼地打")
else:
    print("还是算了。")
    print("(ಥ_ಥ)")

