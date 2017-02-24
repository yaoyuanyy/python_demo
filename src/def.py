def fin(num):
    """ this is a fin """
    a, b = 0, 1
    while a < num:
        print(a, end="|")
        a, b = b, a + b
    print()


fin(10)


def fin2(num):
    """ this is a fin """
    a, b = 0, 1
    result = []
    while a < num:
        result.append(a)
        a, b = b, a + b
    return result


f = fin2(10)
print(f)


def isOk(prompt, reties=4, compliant="yes or no ,please!"):
    while True:
        ok = input(prompt)
        if ok in ('y', 'e', 'yes'):
            return True
        if ok in ('n', 'no'):
            return False
        reties = reties - 1
        if reties < 0:
            raise OSError('error')
        print(compliant)


# print(isOk('do you ready? Go!'))

def change(arg1, *args):
    print(arg1, end="循环")
    print(type(args))
    for a in args:
        print(a)


change(10, 100, 101, 102)

total = 0;  # 这是一个全局变量


# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2;  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total


# 调用sum函数
sum(10, 20)
total2 = sum(10, 200)

print("函数外是全局变量 : ", total)
print("函数外是全局变量 : ", total2)
