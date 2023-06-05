"""
文件
"""
# 1、文件的使用流程
'''
# 打开
f = open("./test1.txt", "w", encoding='utf-8')
# 写入
f.write("测试内容！")
print(f.writable(), f.readable())
# 关闭
f.close()
'''

# 2、读取
'''
f = open("./test1.txt", "r", encoding='utf-8')
# ①f.read([num])
# print(f.read())
print(f.read(10))
# for r in f:
#     print(f.read(10))   # 推荐
# f.seek(偏移量,[0,1,2])
print(f.tell())
f.seek(9, 0)
print(f.tell())
print(f.read(10))
# ②f.readline([limit])
# print(f.readline())
# print(f.readline(10))
# ③f.readlines()
# print(f.readlines())
print(f.closed, f.name, f.mode)
f.close()
print(f.closed, f.name, f.mode)
'''

# 补充：f.flush() 立即清空缓冲区的数据内容到磁盘文件
'''
f = open("test.txt", "w", encoding="utf-8")
f.write("33333")
f.flush()
input("请输入任意字符！")
f.close()
'''

# 文件的相关操作
import os
# 1 获取目录内容列表:os.listdir()
path1 = r"E:\教学\2020下\Python\素材\test"
file_list = os.listdir(path1)
print(file_list)
# 2 获取当前目录:os.getcwd()
print(os.getcwd())
# 3 改变默认目录:os.chdir("目标目录")
os.chdir(path1)
print(os.getcwd())
# 4 创建文件夹
# ①os.mkdir(path[, mode])  # 不能递归的创建
# os.mkdir("./a")
# ②os.makedirs(path[, mode]) # 可以递归创建文件夹
# os.makedirs("./f/e/s")
# 5 重命名
# ①os.rename("old","new") 修改单级目录/文件名称
# os.rename("./a", "./e")
# ②os.renames("old","new") 修改多级目录/文件名称
# os.renames("./f/e/s", "./f/f/f")
# 6 删除
# ①删除文件：os.remove(path)
# os.remove("./将进酒.txt")
# ②删除文件夹：os.removedirs(path) # 要删除的文件夹必须为空
# os.removedirs("./b")

# 补充
# os.path.join(*path)连接两个或更多的路径名组件
str1 = r"d:\a"
str2 = "b"
str3 = "c"
# print(str1 + "/" + str2 + "/" + str3)
print(os.path.join(str1, str2, str3))
# os.path.exists(path)来检测文件/文件夹是否存在
print(os.path.exists("桃花庵歌.txt"))
print(os.path.exists("ss.txt"))
# os.path.splitext(path)分离文件名与扩展名,返回元组(文件名,扩展名)
print(os.path.splitext("桃花庵歌.txt"))
# os.path.isdir(path) 检测是否是文件夹
print(os.path.isdir("桃花庵歌.txt"))
# os.path.isfile(path) 检测是否是文件
print(os.path.isfile("桃花庵歌.txt"))
