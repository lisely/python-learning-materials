# 快捷键ctrl+/
# print("hello world")

# 注释
# 单行注释 #
# 多行注释
'''
这是
多行
注释
'''
"""
这是
多行
注释
"""
# 注释嵌套
# ''' ''' """"""
'''
#
""""""
'''
"""
#
''''''
"""

"""
变量
定义变量
"""
'''
# 方式1   变量名 = 值
a = 2
print(a)
# 方式2   变量名1， 变量名2 = 值1， 值2
c, d = 4, 5
print(c, d)
# 方式3   变量名1 = 变量名2 = 值 多个变量赋同一个值
e = f = 6
print(e, f)
'''

"""
数据类型
查看数据类型 type()
"""
'''
a = 6
b = "abc"
print(type(a), type(b))
# 类型转换
c = "123"
c = int(c)
print(type(c))
'''

"""
算数运算符
+  -  *  /  //(整除)  **(幂运算)  %
"""
'''
a, b = 3, 2
print(a + b, a - b, a * b)
print(a / b, a // b)
print(a ** b)   # a的b次方
print(a % b)    # 商1 余1
'''

"""
赋值运算符
=  +=   -=  *=  /=  //=     %=  **=
"""
'''
a, b = 2, 3
a += b  # a = a + b
print(a)  # 5
a -= b  # a = a - b
print(a)  # 2
a *= b
print(a)  # 6
a **= b  # a = a ** b
print(a)
'''

"""
比较运算符
<   >   !>  >=  <=  ==
"""
'''
a = 2
b = 3
#       False True   True     True   False
print(a > b, a < b, a != b, a <= b, a >= b)
# 链式比较
c = 5
print(a < b <c, a < c <b)
'''

"""
逻辑运算符
not and or
"""
'''
print(not True, not False)
print(True and True, True and False, False and False)
print(True or False, True or True, False or False)
print(5 and 3, 0 and 3)
'''

"""
身份运算符
is  is not
"""
'''
a = 30000
b = 30000
print(id(a), id(b), a is b, a is not b)
'''

"""
成员运算符
in      not in
"""
'''
a = 3
b =[1, 2, 5, 6]
print(a in b, a not in b)
'''

"""
输入
input("提示信息")
"""
'''
# a = input("请输入您的姓名：")
# print(a)
a = input("请输入年龄：")
a = int(a)
print(a + 1)
'''

"""
输出
print(self，*args, sep=' ', end='\n', file=None)
"""
'''
print(1, 7, 8, sep="-")
print(1, end=",")
print(2)
f = open("test.txt", "w", encoding="utf-8")
print("这是要放进文件里的话。", file=f)
'''

"""
格式化输出
%
format
"""
'''
# %
a = 18
print("张三的年龄是", a, "岁。")
# 一个参数
print("张三的年龄是%d岁。" % a)
# 多个参数
b = 20
print("我们要输出数字%d和%d。" % (a, b))
c = 2
print("输出%d。" % c)
# 占位符 %[(name)][flags][width][.precision]typecode
print("输出%.2d。" % c)       # [.precision]
print("输出%010d。" % c)       # [flags][width]
print("输出%+10d。" % c)       # 正数前加+，负数前加-
print("输出%-10d。" % c)    # - 左对齐
print("我们要输出数字%(no1)d和%(no2)d。" % {"no2": b, "no1": a})
'''

# format
'''
a = 3
print("我们要输出的数字是{0}。".format(a))
b = 4
print("我们要输出的数字是{0}和{1}。".format(a, b))
# {[name][:][[fill]align][sign][#][0][width][,][.precision][type]}
c, d = 2020, 9
print("今天是{year}年{month}月。".format(month=d, year=c))  # [name]
print("现在的时间是下午{:02}点{:02}分。".format(a, b))     # [fill][width]
print("我们要输出的数字是{:0<10}。".format(a))    # align
print("我们要输出的数字是{:0>10}。".format(a))    # align
print("我们要输出的数字是{:0^10}。".format(a))    # align
pi = 3.1415926
print("我们要输出的数字是{:.2}。".format(pi))     # .precision
print("我们要输出的数字是{:.2f}。".format(pi))     # .precision [type]
print("我们要输出的数字是{szpi:*^+#010.2f}。".format(szpi=pi))    # 全部
'''
# 对齐问题
str1 = "{:5}{:02}"
print(str1.format("zs", 18))
print(str1.format("zwj", 23))
print(str1.format("dfbb", 20))
# chr(12288)中文空格
str2 = "{1:{0}<5}{2:02}"
str3 = "{1:{0}<5}\t{2:02}"
print(str3.format(chr(12288), "张三", 18))
print(str3.format(chr(12288), "张无忌", 23))
print(str3.format(chr(12288), "东方不败", 20))

a = 'python'
b = 5.20123
print("{:*^20}".format(a))
print("{:*^+20.2f}".format(b))





