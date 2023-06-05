# python关于时间的计算，time模块

## 一. 时间的几种格式：

### 一.时间戳（timestamp）

- 1970年1月1日0点开始，到现在的秒数（以格林尼治时间为准）。

```python
#数据类型为'float',浮点数,小数
import time
print("时间戳")
print("当前时间")
print(time.time())
print(typr(time,time()))

>>> 时间戳
	当前时间
	1648866142.4326322
	<class 'float'>
```

### 二.时间元组（Time tuple(time obj)）

- 这是把年月日时分秒周日……作为一个元组。

```python
#数据类型为'time.struct_time',元组
import time
print('时间元组')
print('当前时间')
print(time.localtime())
print(type(time.localtime()))
print('年是0位：' + str(time.localtime()[0]))
print('月是1位：' + str(time.localtime()[1]))
print('日是2位：' + str(time.localtime()[2]))
print('时是3位：' + str(time.localtime()[3]))
print('分是4位：' + str(time.localtime()[4]))
print('秒是5位：' + str(time.localtime()[5]))
print('周几是6位：' + str(time.localtime()[6]))
print('第几天是7位：' + str(time.localtime()[7]))
print('夏令时是8位，但是没用：' + str(time.localtime()[8]))
print('-----')
print('年是0位：' + str(time.localtime().tm_year))
print('月是1位：' + str(time.localtime().tm_mon))
print('日是2位：' + str(time.localtime().tm_mday))
print('时是3位：' + str(time.localtime().tm_hour))
print('分是4位：' + str(time.localtime().tm_min))
print('秒是5位：' + str(time.localtime().tm_sec))
print('周几是6位：' + str(time.localtime().tm_wday))
print('第几天是7位：' + str(time.localtime().tm_yday))
print('夏令时是8位，但是没用：' + str(time.localtime().tm_isdst))

>>> 时间元组
	当前时间
	time.struct_time(tm_year=2022, tm_mon=4, tm_mday=2, tm_hour=10, tm_min=28, tm_sec=44, tm_wday=5, tm_yday=92, tm_isdst=0)
	<class 'time.struct_time'>
	年是0位：2022
	月是1位：4
	日是2位：2
	时是3位：10
	分是4位：28
	秒是5位：44
	周几是6位：5
	第几天是7位：92
	夏令时是8位，但是没用：0
	-----
	年是0位：2022
	月是1位：4
	日是2位：2
	时是3位：10
	分是4位：28
	秒是5位：44
	周几是6位：5
	第几天是7位：92
	夏令时是8位，但是没用：0
```

### 三.时间格式（Datetime obj）

- 最准确的时间格式，还带毫秒

```python
#数据类型'datetime.datetime'
import datetime
print("时间格式")
print("当前时间")
print(datetime.datetime.now())
print(type(datetime.datetime.now()))

>>> 时间格式
	当前时间
	2022-04-02 10:33:53.726242
	<class 'datetime.datetime'>
```

### 四.时间字符串（string）

- 就是字符串而已

```python
#数据类型为'str',字符串
import time
print("字符串格式")
print("当前时间")
now = time.strftime("%Y%m%d%H%M%S")
print(now)

>>> 字符串格式
	当前时间
	20220402104033
```

```python
#这些备注表示的是now中输入的意思
# % y 两位数的年份表示（00 - 99）
# % Y 四位数的年份表示（000 - 9999）
# % m 月份（01 - 12）
# % d 月内中的一天（0 - 31）
# % H 24小时制小时数（0 - 23）
# % I 12小时制小时数（01 - 12）
# % M 分钟数（00 = 59）
# % S 秒（00 - 59）
# % a 本地简化星期名称
# % A 本地完整星期名称
# % b 本地简化的月份名称
# % B 本地完整的月份名称
# % c 本地相应的日期表示和时间表示
# % j 年内的一天（001 - 366）
# % p 本地A.M.或P.M.的等价符
# % U 一年中的星期数（00 - 53）星期天为星期的开始
# % w 星期（0 - 6），星期天为星期的开始
# % W 一年中的星期数（00 - 53）星期一为星期的开始
# % x 本地相应的日期表示
# % X 本地相应的时间表示
# % Z 当前时区的名称
# % % % 号本身
```



## 二. 关于time模块和datetime模块的比较

```python
# time模块，是以时间戳为基础的。
# datetime模块，是以时间格式为基础的。
# 时间字符串，就是一个字符串，不方便进行计算，首先弃用。
# 时间戳，是个浮点数，也不方便进行计算，也弃用。
# 时间元组，是个元组，不能直接存入数据库，还是弃用。
# 时间格式，这是最基本的格式，优先选用。
```



## 三. 如何让时间格式，字符串，时间戳相互转换

```python
# 首先讲定制时间
# 指定时间
# 其实看下图，左右是时间格式，上面是字符串，下面是时间戳
```

![](C:\Users\29678\Desktop\learn\ptyhon笔记\python关于时间的计算，time模块\time模块的相互转换-16488981125321.png)

### 一.  指定时间

- 想指定时间，就需要从字符串或时间戳转换过去，时间戳还要计算，我们一般用字符串转换为时间格式。

```python
import datetime
print('指定时间')
print('datetime指定时间，datetime格式，图上datetime.datetime.strptime(str,format)')
# 可以设置7个参数来指定时间
S_datetime = datetime.datetime(2019, 10, 29, 21, 39, 2, 21111)
print(S_datetime)

>>> 指定时间
	datetime指定时间，datetime格式，图上datetime.datetime.strptime(str,format)
	2019-10-29 21:39:02.021111
```

```python
# 可以精简为3个参数
import time,datetime
S_datetime = datetime.datetime(2019, 10, 28)
print(S_datetime)
print(type(S_datetime))
print('time指定时间，time时间格式（元组）,图上time.strptime(str,format)')
S_time = time.strptime('2019102921392', '%Y%m%d%H%M%S')
print(S_time)
S_time = time.strptime('20191029', '%Y%m%d')
print(S_time)

>>> 2019-10-28 00:00:00
	<class 'datetime.datetime'>
	time指定时间，time时间格式（元组）,图上time.strptime(str,format)
	time.struct_time(tm_year=2019, tm_mon=10, tm_mday=29, tm_hour=21, tm_min=39, tm_sec=2, tm_wday=1, tm_yday=302, tm_isdst=-1)
	time.struct_time(tm_year=2019, tm_mon=10, tm_mday=29, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=302, tm_isdst=-1)
```

```python
# 甚至可以精简到2个参数
import time,datetime
S_time = time.strptime("201910","%Y%m")
print(S_time)
S_time = time.strptime('2019年10月29日21时39分2秒', '%Y年%m月%d日%H时%M分%S秒')
print(S_time)
print(type(S_time))

>>> time.struct_time(tm_year=2019, tm_mon=10, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=274, tm_isdst=-1)
	time.struct_time(tm_year=2019, tm_mon=10, tm_mday=29, tm_hour=21, tm_min=39, tm_sec=2, tm_wday=1, tm_yday=302, tm_isdst=-1)
	<class 'time.struct_time'>
```

### 二. 想将指定的时间再转换回去

- 再转换回去，需要datetime转换为字符串，图上的dt_obj.strftime()

```python
import time,datetime
S_datetime = datetime.datetime(2019, 10, 29, 21, 39, 2, 21111)
S_time = time.strptime('2019102921392', '%Y%m%d%H%M%S')
print('时间格式转换为字符串')
print('datetime时间格式转换为字符串,图上dt_obj.strftime()')
print(S_datetime)
print(type(S_datetime))
D_str = S_datetime.strftime('%Y-%m-%d %H:%M:%S %f')
print(D_str)
D_str = S_datetime.strftime('%Y%m%d%H%M%S%f')
print(D_str)
print(type(D_str))
print('time时间格式转换为字符串,图上time.strftime(format,t_tp)')
print(S_time)
print(type(S_time))
T_str = time.strftime('%Y%m%d%H%M%S', S_time)
print(T_str)
T_str = time.strftime('%Y-%m-%d %H:%M:%S', S_time)
print(T_str)

>>> 时间格式转换为字符串
	datetime时间格式转换为字符串,图上dt_obj.strftime()
	2019-10-29 21:39:02.021111
	<class 'datetime.datetime'>
	2019-10-29 21:39:02 021111
	20191029213902021111
	<class 'str'>
	time时间格式转换为字符串,图上time.strftime(format,t_tp)
	time.struct_time(tm_year=2019, tm_mon=10, tm_mday=29, tm_hour=21, tm_min=39, tm_sec=2, tm_wday=1, tm_yday=302, tm_isdst=-1)
	<class 'time.struct_time'>
	20191029213902
	2019-10-29 21:39:02
```

