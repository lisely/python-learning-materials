"""
分支判断-if
"""
'''
# 单分支
num1 = 5
num2 = 5
if num1 > num2:
    print("1:yes")
# 双分支
if num1 > num2:
    print("2:yes")
else:
    print("2:no")
# 多分支
if num1 > num2:
    print("3:yes")
elif num1 < num2:
    print("3:no")
else:
    print("3:这两个数是相等的。")
# 嵌套
if num2 >= num1:
    print("4:yes")
    if num1 == num2:
        print("4：他们相等。")
# 类三目运算：a if a>b else b
print("5:yes" if num1 > num2 else "5:no")
'''

"""
循环-while
"""
'''
# 打印十遍“鹅鹅鹅”
num = 0
while num < 10:
    num += 1
    print(num, ":鹅")
# 计算1-10的数值和,并输出结果
result = 0
while num > 0:
    result += num
    num -= 1
else:
    print(result)
'''
"""
循环-for
"""
'''
str = "鹅鹅鹅，曲项向天歌"
for s in str:
    print("->", s)
names = ["东方不败", "独孤求败", "天凉王破", "易烊千玺"]
for name in names:
    print(name)
'''
# 反转字符串
# 	凤凰台上凤凰游，凤去台空江自流
str = "凤凰台上凤凰游，凤去台空江自流"
result = ""
for s in str:
    result = s + result
else:
    print(result)


# break
# 计算1-10的数值和,并输出结果
# 如果中途因为打断而退出，则不会执行else中的语句
'''
num = 10
result = 0
while num > 0:
    result += num
    num -= 1
    if num == 5:
        break
else:
    print(result)
'''
# 加法计算器
'''
while True:
    # 输入
    print("请用户输入两个数值，你将得到他们的结果！")
    num1 = input("第一个值：")
    num2 = input("第二个值：")
    num1 = float(num1)
    num2 = float(num2)
    if num1 > 100 or num2 > 100:
        print("输入数据有误，请重新输入！")
        continue
    # 计算
    result = num1 + num2
    # 输出
    print("计算结果为：", result)
    # 退出流程
    is_quit = input("是否退出程序？(q:退出,其他:继续)")
    if is_quit == "q":
        break
'''
'''
# 打印1-100之间的偶数
for num in range(1, 101):
    if num % 2 == 0:
        print(num)
# 九九乘法表
for i in range(1, 10):   # 每一行
    for j in range(1, i + 1):   # 一行中的每一列
        print("%d * %d = %d" % (i, j, i*j), end='\t')
    print()
'''

# pass
num = 10
if num == 10:
    pass
else:
    pass
