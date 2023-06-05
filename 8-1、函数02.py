# 1、高阶函数
def px(a):
    return -a

list1 = [4, 7, 3, 51, 20, 13]
# list.sort(list1, reverse=False)
list.sort(list1, key=px)
print(list1)


# 2、返回函数
def getFunc(flag):
    # 函数内部再定义几个函数
    def sum(a, b, c):
        return a + b + c
    def cj(a, b, c):
        return  a * b * c
    # 根据不同的flag返回不同的函数
    if flag == "+":
        return sum
    elif flag == "*":
        return cj


result = getFunc("*")
print(result(5, 4, 3))
# 3、匿名函数
# lambda 参数1，参数2，……：表达式
sum1 = (lambda x, y: x + y)(3, 4)
print(sum1)
sum2 = lambda x, y: x + y
print(sum2(4, 6))

# 4、闭包
def outer(x):
    def inner(y):
        nonlocal x
        x += y
        return x
    return inner

out = outer(3)
print(out(4))   # 7
print(out(2))   # 9

# 5、装饰器
# 简单装饰器
'''
def check(Func):
    def inner():
        print("验证登录……")
        Func()
    return inner

def line(Func):
    def inner():
        print("-"*30)
        Func()
    return inner

@line
@check
def fss():
    print("发说说！")
# fss = check(fss)   # 等价于@check

fss()
'''
# 对有参函数进行装饰   ①②③参数保持一致
'''
def zsq(Func):
    def inner(a, b):    # ②
        print("-"*30)
        Func(a, b)      # ③
    return inner
@zsq
def sum(num1, num2):  # ①
    print(num1 + num2)

sum(4, 5)
'''
'''
def zsq(Func):
    def inner(*args):    # ②
        print("-"*30)
        Func(*args)      # ③
    return inner

@zsq
def sum(num1, num2):  # ①
    print(num1 + num2)

@zsq
def sum2(num1, num2, num3):  # ①
    print(num1 + num2 + num3)

sum(4, 15)
sum2(2, 3, 4)
'''
# 对有返回值的函数进行装饰
def zsq(Func):
    def inner(*args):    # ②
        print("-"*30)
        result = Func(*args)      # ③
        return result       # 返回值
    return inner

@zsq
def sum(num1, num2):  # ①
    return num1 + num2

print(sum(3, 4))
# 带有参数的装饰器
def getzsq(char):
    def zsq(Func):
        def inner(*args):  # ②
            print(char * 30)
            result = Func(*args)  # ③
            return result  # 返回值

        return inner
    return zsq

@getzsq("=")
def sum(num1, num2):  # ①
    return num1 + num2

@getzsq("*")
def sum2(num1, num2, num3):  # ①
    return num1 + num2 + num3

print(sum(3, 4))
print(sum2(3, 4, 1))