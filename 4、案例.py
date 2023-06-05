# 如果一张纸的厚度是0.08mm，那么对折多少次之后能达到珠穆朗玛峰的高度（8848.13m）？
'''
height = 0.08 / 1000
count = 0
while True:
    height *= 2
    count += 1
    if height > 8848.13:
        print("只需要折{0}次就可以达到珠峰的高度了。".format(count))
        break
'''
# 今有雉（鸡）兔同笼，上有三十五头，下有九十四足，问雉兔各几何”
# 鸡x  兔y
'''
for x in range(1, 36):
    y = 35 - x
    if 2 * x + 4 * y == 94:
        print("鸡有{0}只，兔有{1}只。".format(x, y))
        break
'''
# 水仙花数判断
'''
while True:
    print("=====水仙花数验证=====")
    num = input("请输入你要验证的数字（三位）:")  # 输入
    num = int(num)
    if not (100 <= num <= 999):     # 验证是否是三位数
        print("请输入三位数！")
        continue
    # 验证是否是水仙花数 num=个位数的3次方(c)+十位数的3次方(b)+百位数的3次方(a)
    a = num // 100
    b = num % 100 // 10
    c = num % 10
    result = ((a ** 3 + b ** 3 + c ** 3) == num)
    if result:
        print("{0}是水仙花数。".format(num))
    else:
        print("{0}不是水仙花数。".format(num))
    is_quit = input("是否继续？(q:退出，其他:继续)")
    if is_quit == "q":
        break
'''
# 猜数字游戏
'''
import random

num = random.randint(1, 100)
count = 0  # 计次
print("=====猜数字游戏=====")
while True:
    result = input("请输入你猜的数值(范围1-100，q:退出):")
    if result == "q":
        break
    count += 1
    result = int(result)
    if result == num:
        print("恭喜你，猜对啦，数值就是{0},一共用了{1}次。".format(result, count))
        break
    elif result > num:
        print("你猜的数字偏大。")
    else:
        print("你猜的数字偏小。")
'''
# import random
# num = random.randint(1, 100)
# print(num)
"""
掷骰子游戏
"""
import random

print("欢迎来到掷骰子游戏！")
name_a = input("请输入玩家A的姓名：")
name_b = input("请输入玩家B的姓名：")
while True:
    input("请玩家【%s】掷骰子（任意键投掷）。" % name_a)
    num_a = random.randint(1, 6)
    print("玩家【%s】投掷的点数为->%d" % (name_a, num_a))
    print()
    input("请玩家【%s】掷骰子（任意键投掷）。" % name_b)
    num_b = random.randint(1, 6)
    print("玩家【%s】投掷的点数为->%d" % (name_b, num_b))
    print()
    if num_a > num_b:
        print("=====玩家【%s】获胜=====" % name_a)
    elif num_a < num_b:
        print("=====玩家【%s】获胜=====" % name_b)
    else:
        print("=====平局=====")
    is_quit = input("是否退出？(q:退出，其他:继续)")
    if is_quit == "q":
        break
