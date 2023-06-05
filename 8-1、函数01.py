"""
函数
"""
# 1、函数的基本使用
def abc():
    print("哇！函数！！！")

# abc()
# 2、参数
# ①单个参数
def abc2(a):
    print(a, "!!!")

abc2("python")
# ②多个参数
def abc3(a, b, c):
    print(a, b, c, "。")

abc3(1, 2, 3)       # 形参和实参一一对应
abc3(c=1, b=2, a=3)     # 函数名(参数名称1=参数1，参数名称2=参数2)，不用严格按照顺序
# ③不定长参数
def abc4(*args):   # 装包成元组
    print(args)

abc4(1)
abc4(4, 5, 6)
def abc5(**kwargs):  # 装包成字典
    print(kwargs)

abc5(a=4, b=5, c=6)
# abc5(**{'a': 4, 'b': 5, 'c': 6})
# ④缺省参数
def abc6(a=None, b=1):
    print(a, b)

abc6()
abc6(b=5)
abc6(a="鱼", b=4)
# 3、返回值
def a1():
    a = 1
    b = 2
    return a, b

str1 = abc()
str2 = a1()
print(str1, str2)
# 4、函数的使用描述
# 直接在函数体的最上面, 添加三个双引号对注释
def sum1(num1, num2):
    """
    获取两个参数的和
    :param num1: 数值1
    :param num2: 数值2
    :return: 数值和
    """
    return num1 + num2
# 5、偏函数
def qy(n, m):
    return n % m

def qy_to_2(n, m=2):
    """
    很多内容
    """
    return n % m

from functools import partial
qy_to_3 = partial(qy, m=3)    # 自动生成偏函数
print(qy_to_3(5))

# print(qy(11, 2))
# print(qy_to_2(4))
