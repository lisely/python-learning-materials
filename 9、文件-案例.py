from ee import Role
"""
1、文件复制
"""
'''
path_a = r"E:\教学\2020下\Python\素材\复制文件\道德经.txt"
path_b = r"E:\教学\2020下\Python\素材\复制文件\new\道德经.txt"
# 1、读取源文件a
f_a = open(path_a, "rb")
# 方式一：一次性读取全部内容
# content = f_a.read()
# 方式二：分批读取
f_b = open(path_b, "wb")
while True:
    content = f_a.read(1024)   # 每次最多读取1024个字节长度
    if len(content) == 0:   # 当读取内容为空时退出
        break
    # 2、写入文件b
    f_b.write(content)    # 边读取文件a时，边把内容写入文件b
f_a.close()
f_b.close()
'''

"""
2、文件分类，并生成文件清单
"""
# '''
import os
import shutil


def getlist(file, path):
    for filename in os.listdir(path):
        print(filename)
        if os.path.isdir(filename):
            file.write(filename + "\n")
            getlist(file, filename)  # 如果是文件夹则递归调用函数，继续遍历
        else:
            file.write("\t" + filename + "\n")   # 如果是文件就直接写入


path = r"E:\教学\2020下\Python\素材\文件分类"
os.chdir(path)  # 切换目标路径问工作路径
# 1、遍历目标文件夹
for filename in os.listdir("./"):
    # print(filename)
    # 2、获取文件后缀
    index = filename.rfind(".")
    dirname = filename[index + 1::]
    # 3、根据后缀名生成相应文件夹
    if not os.path.exists(dirname):  # 判断文件夹是否存在
        os.mkdir(dirname)
    # 4、移动文件到对应文件夹下
    shutil.move(filename, dirname)
# 5、生成文件清单
# ①生成新清单文件
file = open("文件分类清单.txt", "w", encoding="utf-8")
# ②写入数据
getlist(file, path)
# ③关闭文件
file.close()
# '''

"""
3、批量修改文件名
"""
'''
import os

def delstr(dir_path, del_str):
    for filename in os.listdir(dir_path):  # 遍历文件夹
        file_path = os.path.join(dir_path, filename)  # 补全文件路径
        # 如果是文件夹，则递归
        if os.path.isdir(file_path):
            delstr(file_path, del_str)
        # 如果是文件，则直接重命名
        else:
            new_name = filename.replace(del_str, "")
            new_path = os.path.join(dir_path, new_name)
            os.rename(file_path, new_path)
            print(filename, "---->", new_name)


dir_path = r"E:\教学\2020下\Python\素材\重命名"
del_str = "【更多资源请添加公众号：1131231】"
delstr(dir_path, del_str)
print("执行完毕!")
'''

"""
4、合并文件
"""
import os


dir_path = r"E:\教学\2020下\Python\素材\文件合并"
os.chdir(dir_path)
file = open(dir_path + ".txt", "w", encoding="utf-8")  # 新文件
for filename in os.listdir("./"):
    f = open(filename, "r", encoding="utf-8")  # 打开源文件
    for content in f:
        file.write(content)
    file.write("\n\n")
    f.close()
file.close()
print("合并完成！")



