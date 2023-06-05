# 1、输入：输入身高、体重、年龄、性别
person_height = float(input("请输入身高(m):"))
person_weight = float(input("请输入体重(kg):"))
person_age = int(input("请输入年龄:"))
person_gender = int(input("请输入性别(男-1，女-0):"))
# 2、计算
#   BMI=体重(kg)/(身高*身高)(米）
#   体脂率=1.2*BMI+0.23*年龄-5.4-10.8*性别(男：1，女：0）
BMI = person_weight / (person_height * person_height)
person_tzl = 1.2 * BMI + 0.23 * person_age - 5.4 - 10.8 * person_gender
person_tzl /= 100
# 判断范围
min_num = 0.15 + 0.1 * (1 - person_gender)
max_num = 0.18 + 0.1 * (1 - person_gender)
result = min_num <= person_tzl <= max_num  # 结果True/False
# 3、输出
print("当前用户的体脂率为%.2f" % person_tzl, result)