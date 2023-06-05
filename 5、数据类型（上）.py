"""
一、Numbers(数值类型)
"""
'''
# 1、int-进制
num1 = 12      # 十进制： 0-9
num2 = 0o12     # 八进制：0o+数值(0-7)
num3 = 0b10     # 二进制： 0b+数值(0-1)
num4 = 0xf    # 十六进制： 0x+数值(0-9 or a-f)
print(num1, num2, num3, num4)
# 2、随机数
import random
# ①choice(seq):从一个序列中，随机挑选一个数值
nums = [3, 60, 50, 23, 17]
print(random.choice(nums))
# ②randint(x,y):范围之内的随机整数[x,y]
nums2 = random.randint(1, 20)
print(nums2)
'''
"""
二、Bool(布尔类型)
"""
# True False
"""
三、String(字符串)
"""
# 形式

# # 非原始字符串
# str1 = "abciufiogop" \
#        "hkhnlkhkf"
# str2 = '''auyrfgyho
# foiuhoiphj'''
# # r 转为原始字符串
# str3 = r"ab\nkc"
# print(str3)
# # \ 转义符
# print("\"")

# 字符串的一般操作
# 字符串拼接
'''
#  方式一 str1+str2
print("python" + "world")
#  方式二 str1str2
print("python""world")
#  方式三 “xxx%sxxx"%(a+b)
print("%s" % ("python" + "world"))
#  方式四 str*数值
print("=" * 60)
'''
# 字符串切片
'''
str1 = "凤凰台上凤凰游，凤去台空江自流"
print(str1[2])
# str[start:end:step]   范围：[start:end)
print(str1[4:7])
print(str1[0:len(str1):1])
print(str1[::2])
print(str1[::-1])  # 负号反向
print(str1[::-2])
'''
# 字符串函数操作
# 1、查找计算
'''
# ①len(str):计算字符串的字符个数
str1 = "python"
print(len(str1))
# ②find(sub,start=0,end=len(str))：查找子串索引位置
print(str1.find("th"))
print(str1.find("thg"))     # 找不到则返回-1
# ③rfind(sub,start=0,end=len(str))：查找子串索引位置， 从右往左
str2 = "l love python"
print(str2.find("o"), str2.rfind("o"))
# ④index(sub,start=0,end=len(str))：获取子串索引位置
print(str2.index("o"))
# print(str2.index("o1"))     # 找不到则报错
# ⑤rindex(sub,start=0,end=len(str))：获取子串索引位置，从右往左
print(str2.rindex("o", 1, 10))
# ⑥count(sub,start=0,end=len(str))：计算某个子字符串出现的次数
print(str2.count("o"))
print(str2.count("z"))      # 没有则返回0
print(str2.count("o", 1, 6))
'''
# 2、转换
'''
# ①replace(old,new[,count])：替换，使用新字符串替换原字符串中的旧字符串
str1 = "凤凰台上凤凰游"
str2 = str1.replace("凤凰", "孔雀")  # 不修改原字符串
str3 = str1.replace("凤凰", "孔雀", 1)
print(str1, str2, str3)
# ②capitalize()：将字符串首字母变为大写
# ③title()：将字符串中的每个单词的首字母变为大写
# ④lower()：将字符串每一个字符都变为小写
# ⑤upper()：将字符串每一个字符都变为大写
str4 = "l lovE python"
print(str4.capitalize(), str4.title(), str4.lower(), str4.upper(), sep='\n')
'''
# 3、填充压缩
'''
# ①ljust(width,fillchar)：根据指定字符，将原字符串填充足够指定长度,原字符串在左
# ②rjust(width,fillchar)：根据指定字符，将原字符串填充足够指定长度,原字符串在右
# ③center(width,fillchar)：根据指定字符，将原字符串填充足够指定长度,原字符串居中
str1 = "-oWo-"
print(str1.ljust(15, "*"), str1.rjust(15, "*"), str1.center(15, "*"), sep='\n')
# ④lstrip(chars)：移除原字符串左边指定字符（默认为空白字符）
# ⑤rstrip(chars)：移除原字符串右边指定字符（默认为空白字符）
# 空格、\n\t都属于空白字符
str2 = " \n\tT-T----"
print(str2, str2.lstrip(), str2.rstrip("-"), sep='\n')
'''
# 4、分割拼接
'''
# ①split(sep,maxsplit)：将一个大的字符串分割成几个子字符串
str1 = "姓名，性别，年龄，学号"
list1 = str1.split("，")
print(str1, list1, list1[0])
list2 = str1.split("，", 2)
print(str1, list2)
# ②partition(sep)：根据指定的分隔符，返回（分隔符左侧的内容，分隔符，分隔符右侧的内容）
# ③rpartition(sep)：根据指定的分隔符，返回（分隔符左侧的内容，分隔符，分隔符右侧的内容） 从右往左找分隔符
# 返回类型为元组类型
print(str1.partition("，"), str1.rpartition("，"), sep='\n')
print(str1.partition("-"), str1.rpartition("-"), sep='\n')
# ④splitlines(keepends)：按照换行符（\r,\n),将字符串拆成多个元素，保存到列表中
str2 = "天行健，君子以自强不息；\n地势坤，君子以厚德载物；"
print(str2.splitlines())
print(str2.splitlines(True))
# ⑤join(iterable)：根据指定字符串，将给定的可迭代对象进行拼接，得到拼接后的字符串
str3 = "天行健，君子以自强不息"
list2 = ["1", "4", "39", "abc"]
print("-".join(str3))
print("*".join(list2))
'''
# 5、判定
'''
# ①isalpha()：判断字符串中是否所有的字符都是字母
# ②isdigit()：判断字符串中是否所有的字符都是数字
# ③isalnum()：判断字符串中是否所有的字符都是数字或者字母
# ④isspace()：判断字符串中是否所有的字符都是空白符
print("abc".isalpha(), "123".isdigit(), "123abc".isalnum(), "\n\t\r ".isspace())
# ⑤startswith(prefix,start=0,end=len(str))：判断字符串是否以某个前缀开始
# ⑥endswith(suffix,start=0,end=len(str))：判断字符串是否以某个后缀结束
str1 = "天行健，君子以自强不息；\n地势坤，君子以厚德载物；"
print(str1.startswith("天"), str1.endswith("载物；"))
# ⑦in / not in :判定一个字符串，是否被/不被另一个字符串包含
str2 = "abcdefg"
print("a" in str2, "h" not in str2)
'''
"""
str1 = '''A Donkey once found a Lion’s skin which the hunters had left out in the sun to dry. He put it on and went towards his native village. All fled at his approach, both men and animals, and he was a proud Donkey that day. In his delight he lifted up his voice and brayed, but then every one knew him, and his owner came up and gave him a sound cudgeling for the fright he had caused. And shortly afterwards a Fox came up to him and said:” Ah, I knew you by your voice.”
Fine clothes may disguise, but silly words will disclose a fool.'''
# 文中出现几次空格？
print(str1.count(" "))
# Fox第一次出现的位置是？
print(str1.find('Fox'))
# 把文中出现的Donkey全部替换为DONKEY
str2 = str1.replace("Donkey", "DONKEY")
print(str2)
# 把全文按照“换行符”进行分割
str3 = str1.splitlines()
print(str3)
# 输出全文并把“Fine clothes may disguise, but silly words will disclose a fool.”全部转为大写
# print(str3[0], str3[1].upper(), sep="\n")
str4 = str3[0] + '\n' + str3[1].upper()
print(str4)
# 文中出现了几次and？
str5 = str1.lower()
print(str5.count("and"), str1.count("and"))
# 把全文按照“,”进行分割
print(str1.split(','))
"""
"""
四、List(列表)
"""
# 1、定义
'''
# 方式一 [元素1,元素2,……]
list1 = [1, 2, "a", "world"]
# 方式二
# 列表推导式:[表达式  for  num in nums]
nums = [1, 5, 7, 10, 2]
list2 = [num for num in nums]
print(nums, list2)
list3 = [num + 1 for num in nums]
print(nums, list3)
# 列表推导式:[表达式  for  num in nums if 条件]
list4 = [num for num in nums if num % 2 == 0]
print(nums, list4)
list5 = [num + 1 for num in nums if num % 2 == 0]
print(nums, list5)
# 列表生成式 range(start,stop[,step])
list6 = range(1, 10)
# for i in list6:
#     print(i)
print(list6)
'''
# 2、常用操作
# 2-1 增
'''
# ①append(object)：在列表的最后追加一个新元素
nums = [num for num in range(1, 4)]
nums.append(7)
print(nums)
# ②insert(index,object)：在列表中的指定为位置处插入一个新元素
nums.insert(3, 45)
print(nums)
# ③extend(iterable)：在列表中，扩展一个可迭代序列
list1 = [8, 9, 20]
nums.extend(list1)
print(nums)
'''
# 2-2 删
'''
nums = [num for num in range(1, 9)]
# ①del 指定元素：删除一个指定元素
print(nums)
del nums[1]
# del nums
print(nums)
# ②pop(index=-1)：移除并返回列表中指定索引对应的元素，默认-1，对应列表最后一个元素
print(nums.pop())
print(nums)
print(nums.pop(4))
print(nums)
# ③remove(object)：移除列表中指定元素
nums.remove(5)
print(nums)
'''
# 2-3 改
'''
# names[index]=value
nums = [num for num in range(1, 9)]
print(nums)
nums[3] = 14
print(nums)
'''
# 2-4 查
'''
# ①items[index]：获取单个元素
print(nums[3])
# ②index(value[,start,end])：获取元素索引
print(nums.index(5))   # 4
nums[4] = 14
print(nums)
# ③count(object)：获取指定元素个数
print(nums.count(14))
# ④items[start:end:step]：获取多个元素
print(nums[1:6], nums[1:6:2])
# 遍历
# 方式一 ：for item in list：根据元素进行遍历
for num in nums:
    print(num)
# 方式二：for index in range(len(list)):根据索引进行遍历
for i in range(len(nums)):
    print(nums[i])
# 方式三：for index,value in enumerate(nums):遍历枚举对象
# enumerate(sequence,[start=0])
for i, num in enumerate(nums):
    print(i, num)
# 方式四：通过迭代器进行
# 可迭代对象
from collections.abc import Iterable
print(isinstance(nums, Iterable))  # True
# 迭代器
from collections.abc import Iterator
print(isinstance(nums, Iterator))   # False
Iter = iter(nums)   # iter(Iterable)：把可迭代对象转为迭代器
print(isinstance(Iter, Iterator))   # True
print("="*40)
# for num in Iter:
#     print(num)
for num in Iter:
    # print(num)
    print(next(Iter))
# print(next(Iter)) # 迭代结束后继续获取会报错
'''
# 3、其他操作
# ①in / not in
list1 = [4, 6, 7, 123, 5, 0]
print(4 in list1, 8 not in list1)
# ②排序一：sorted(iterable,key=None,reverse=False)
list2 = sorted(list1)
list3 = sorted(list1, reverse=True)   # 降序
def px(a):
    return -a
list4 = sorted(list1, key=px)         # 通过key实现降序
print(list1, list2, list3, list4)
# ③排序二：list1.sort(key=None,reverse=False)
# list1.sort()       # 原列表改变
# list1.sort(reverse=True)         # 降序
list1.sort(key=px)      # 通过key实现降序
print(list1)
# ④乱序：random.shuffle(list)   导入random模块
import random
random.shuffle(list1)
print(list1)
# ⑤比较：直接比较
num1 = [4, 4, 0]
num2 = [3, 4, 5, 6]
print(num2 > num1)
# ⑥反转一：l.reverse()  会改变原列表
list1.reverse()
print(list1)
# ⑦反转二：切片l[::-1]
print(list1[::-1], list1)

str1 = "馒头、披萨、西红柿、方便面、莲藕、柚子、冰激凌、饼干、酸菜鱼、石榴、燕窝、荷包蛋、菊花茶、火龙果、棒棒糖"
no_1 = [s for s in str1.split("、")]
count = 1
print(no_1[count + 1])
