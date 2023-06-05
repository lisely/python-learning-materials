import time

# 1、获取时间戳
print(time.time())
my_time = 1603866897.8261285
# 2、获取时间元组
print(time.localtime(my_time))
print(time.localtime())
# 3、格式化时间
# ①ctime(seconds=None)：时间戳 -> 可读时间
print(time.ctime(), time.ctime(my_time))
# ②asctime(p_tuple=None)：时间元组 -> 可读时间
my_localtime = time.localtime(my_time)
print(time.asctime(), time.asctime(my_localtime))

# 4、格式化日期
# ①strftime(format, p_tuple=None)：接收时间元组，并返回以可读字符串表示的当地时间
print(time.strftime("%Y-%m-%d %H:%M:%S", my_localtime))
# ②strptime(string, format)：根据指定的格式把一个时间字符串解析为时间元组
str1 = "2020-10-28"
print(time.strptime(str1, "%Y-%m-%d"))
# ③mktime(t)：把结构化的时间转为时间戳
print(time.mktime(time.strptime(str1, "%Y-%m-%d")))
print(time.mktime(my_localtime))
# 5、休眠
t0 = time.time()
# time.sleep(3)
t1 = time.time()
print(t1 - t0)

import calendar

# 1、获取某月日历
print(calendar.month(2020, 10))
# 2、获取某年日历
print(calendar.prcal(2020))

import datetime

# 1、获取当天日期
print(datetime.datetime.now())
print(datetime.datetime.today())
# 2、单独获取当前的年月日时分秒
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)
# 3、计算n天之后的日期
# timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
result = datetime.datetime.today() + datetime.timedelta(days=7)
print(result)
# 4、获取两个时间的时间差
first = datetime.datetime(2020, 1, 1)
end = datetime.datetime(2020, 10, 1)
result = end - first
print(result, result.total_seconds())

# 把当前时间以图示格式显示
print(time.strftime("【%Y-%m-%d】%H:%M:%S", time.localtime()))

# 输入两个数值，等待1秒后显示结果。
# num1 = int(input("第一个数值："))
# num2 = int(input("第二个数值："))
# time.sleep(1)
# print(num1 + num2)

# 获取2020年9月的日历
print(calendar.month(2020, 9))

# 计算10天后的日期
result = datetime.datetime.now() + datetime.timedelta(days=10)
print(result)



