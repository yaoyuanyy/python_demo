def fun1(str):
    print("这是必须参数函数")
    print(str)
fun1("this is a must param")

def fun2(name, age):
    print("这是关键字参数函数")
    print("名字：", name)
    print("年龄：", age)
fun2(age=1, name="yy")

def fun3(name, age=10):
    print("这是默认参数")
    print("名字：", name)
    print("年龄：", age)
fun3("yyy")


def fun4(arg1, *args2):
    print("这是不定长参数")
    print("输出: ", )
    print(arg1)
    for var in args2:
        print("不定长参数：", var)
    return

# fun4 函数
fun4(10)
fun4(70, 60, 50)

# 匿名函数
fun5 = lambda arg1, arg2: arg1 + arg2
print(fun5(1, 2))
