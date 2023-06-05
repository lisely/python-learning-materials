"""
Set(集合)
"""
# 可变集合set
# 1、定义
'''
# ①s={1,2,3,4}
s1 = {"a", 1, 4, 5}
# ②s=set(iterable)
list1 = [3, 4, 7, 8]
s2 = set(list1)
print(s1)
print(s2)
# ③集合推导式
s3 = set(x + 1 for x in range(0, 20) if x % 2 == 0)
print(s3)
'''
# 2、单一集合操作
'''
s1 = {2, 5, 6, 9}
# 2-1 增
# ①add(value)：单个添加
s1.add(6)
# ②update(iterable):批量添加
list1 = ["李白", "李清照", "杜甫"]
s1.update(list1)
print(s1)
# 2-2 删
# ①remove(element)：指定删除set对象中的一个元素
s1.remove(6)       # 元素不存在则报错
# ②discard(element)：指定删除set对象中的一个元素
s1.discard(50)  # 元素不存在不会报错
print(s1)
# ③pop()：随机删除一个集合中的元素并返回
print(s1.pop())
# ④clear()：清空集合
s1.clear()
print(s1)
# 2-3 查
s3 = {8, 2, 4, 1, 20}
# ①通过 for in 进行遍历
for s in s3:
    print(s)
# ②通过迭代器进行访问
for s in iter(s3):
    print(s)
'''
# 不可变集合frozenset
# 1、定义
'''
# ①fs=frozenset(iterable)
f1 = frozenset(list1)
print(f1)
# ②集合推导式
f3 = frozenset(x + 1 for x in range(0, 20) if x % 2 == 0)
print(f3)
'''
# 3、集合之间操作
'''
s1 = set(x for x in range(1, 10))
s2 = {2, 15, 7, 9, 20, 30, 1}
# ①交集：intersection(iterable)      &
print(s1.intersection(s2))
print(s1 & s2)
# ②并集：union()   |
print(s1.union(s2))
print(s1 | s2)
# ③差集：difference()    -
print(s1.difference(s2))
print(s1 - s2)
# ④对称差集：symetric_difference   ^
print(s1.symmetric_difference(s2))
print(s1 ^ s2)
# ⑤判定：isdisjoint()：两个集合是否不相交
print(s1.isdisjoint(s2))
# ⑥判定：issuperset()：一个集合是否包含另一个集合
print(s1.issuperset(s2))
# ⑦判定：issubset()：一个集合是否包含于另一个集合
print(s1.issubset(s2))
'''
# 集合最常用的一个用法
'''
list1 = ["鸡", "狗", "牛", "蛇", "马", "羊", "猴", "龙", "蛇", "鼠", "猪", "虎", "兔", "鼠", "牛", "狗", "鸡", "马", "羊", "蛇", "猪", "猴", "龙", "鸡", "鼠", "羊", "猪", "虎", "鸡", "马", "龙", "兔"]
# print(list1)
s1 = set(list1)
print(s1)
'''
"""
Tuple(元组) 有序的不可变的元素集合
"""
# 一、定义
'''
num = (1,)              # 一个元素的写法
num2 = (1, 2, (3, 7))   # 多个元素的写法
num3 = 6, 8, 10         # 多个对象，以逗号隔开，默认为元组
list1 = ["程咬金", "黄飞鸿", "李世民"]
t1 = tuple(list1)       # 从列表转换成元组
print(t1)
'''
# 二、常用操作
'''
# 1、查
# ①tuple[index]：获取单个元素
print(t1[1])
# ②tuple[start:end:step]：获取多个元素
print(t1[0:2])
'''
# 三、其他操作
'''
# 1、获取
t2 = ("电影", "电视剧", "综艺", "音乐")
# ①count(item)：统计元组中指定元素的个数
print(t2.count("电影"))
# ②index(item)：获取元组中指定元素的索引
print(t2.index("电影"))
# ③len(tuple)：返回元组中元素的个数
print(len(t2))
# ④max(tuple)：返回元组中元素最大的值
print(max(t2))
# ⑤min(tuple)：返回元组中元素最小的值
print(min(t2))
# 2、判定 in/ not in
print(3 in t2, 3 not in t2)
# 3、拼接
print(t2 * 3, t1 + t2)
'''
"""
Dictory(字典）无序的可变的键值对集合
"""
# 一、定义
'''
# 1、方式一：{key:value,key:value……}
dic1 = {"username": "张三", "age": 18}
# 2、方式二：fromkeys(sep,value=None)
# ①类调用：dict.fromkeys("abc",123)
dic2 = dict.fromkeys("python")
dic3 = dict.fromkeys("world", 1)
print(dic3)
# ②对象调用：dicLx.fromkeys("abc",123)
dic4 = dic1.fromkeys("dic", "abc")
print(dic1, dic4)
'''
# 二、常用操作
dic1 = {}
# 1、增
# ①dic[key]=value ：当key在原字典中不存在时，即为新增操作
dic1["username"] = "姜子牙"
dic1["xinnian"] = "zzds"
# 2、改
# ②dic[key]=value：当key在原字典中存在时，即为修改
dic1["username"] = "钓鱼老头"
# ③oldDic.update(newDic)：批量修改键值对
dic2 = {"one": 1, "two": 2, "xinnian" : "cshy"}
dic1.update(dic2)
# 3、删
# ①del dic[key]
del dic1["two"]
# ②dic.pop(key[,default])：删除指定键值对，并返回对应的值
print(dic1.pop("two", "该key不存在"))   # 如果key不存在，那么直接返回给定的默认值
# ③dic.popitem()：删除当前排序后的最后一个键值对，并以元组的形式返回键值对
dic1.popitem()
# ④dic.clear()：删除字典内所有键值对
dic1.clear()
print(dic1)
# 4、查
dic3 = dict.fromkeys("abcdef", 123)
print(dic3)
# 4-1、获取单个值
# ①dic[key]
print(dic3["c"])
# ②dic.get(key[,default])
print(dic3.get("g"))
print(dic3.get("h", "啥？"))
print(dic3)
# ③dic.setdefault(key[,default])    # 如果key不存在，则新增
print(dic3.setdefault("w"))         # value=None
print(dic3.setdefault("n", "啥？"))   # value=default
print(dic3)
# 4-2、获取所有的键、值、键值对
print(dic3.values())
print(dic3.keys())
print(dic3.items())
# 4-3 遍历
for k, v in dic3.items():
    print(k, v)
# 5、计算
# len()
print(len(dic3))
# 6、判定
# in/ not in
print("a" in dic3, "a" not in dic3)

"""
模拟登录
"""
user = {
    "no1": {"username": "姜子牙", "password": "zzds"},
    "no2": {"username": "苏妲己", "password": "wbsy"},
    "no3": {"username": "申公豹", "password": "jzy"},
    "no4": {"username": "师尊", "password": "zhdap"}
}
flag_pass = ""    # 辅助变量
print("========某某系统登录========")
name = input("请输入用户名：")
password = input("请输入密码：")
for v in user.values():
    if v['username'] == name:
        flag_pass = v['password']
if flag_pass == "":
    print("用户不存在！")
elif flag_pass != password:
    print("密码错误！")
else:
    print("尊贵的VIP用户【%s】，欢迎回来！" % name)
