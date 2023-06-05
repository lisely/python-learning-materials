# python的基础语法

## print()函数

- 主要功能是：打印内容

- 无引号用法

  ```python
  x = 2
  y = x * 2
  print(y)
  #无引号：让计算机读懂括号里的内容，并打印最终结果
  >>> 4
  ```

- 单双引号的用法(`""`) (`''`)

  - 使用单双引号的缘由：让计算机无需理解，原样复述引号中的内容。
  - 为什么会有单双引号一起用：

  ```python
  #""或'' : 在print()函数内不仅能使用单引号，还能使用双引号，两者的效果没什么区别，都能让你打印出一行文本。
  #【注意：双引号是英文输入法下的双引号，而不是两个单引号！】
  print('你好')
  print("你好")
  >>>你好
     你好
  ```

- 三引号的用法("' '")

  ```python
  print('''你好
  你真好''')
  >>>你好
     你真好
  ```

## 转义字符

![转义字符总结](C:\Users\29678\Desktop\learn\ptyhon笔记\python的基础语法\转义字符总结.png)

## 变量的命名规范

- 只能是一个词
- 只能包含字母、数字和下划线
- 不能以数字开头
- 尽量描述包含的数据内容
- 不要使用pyhton函数名或关键字

## 数据类型

- `str` 字符串

  ```python
  字符串就是用引号括起来的文本
  
  字符串就是由一个个字符串起来的组合，字符可以是一个数字、一个字母、一个文字，甚至是一个符号。字符串可以表达现实世界里的词、语句、表达式等
  ```

- `int` 整数

  ```python
  整数就是普通的整数数字
  ```

- `float` 浮点数

  ```python
  浮点数就是带有小数点的数
  运算结果会有误差
  ```

## 四则运算

- `+` 加

- `-` 减

- `*` 乘

- `/` 除

- `%`  被整除后多出的余数为输出结果

- `//`  被整除后得出的整数为输出结果

- `**`  幂函数

  ```python
  x = 5
  y = 2
  a = x + 1
  b = x - 1
  c = x * y
  d = x / y
  e = x % 2
  f = x // 2
  g = x ** y
  print(a,b,c,d,e,f,g)
  
  >>> 6 4 10 2.5 1 2 25
  ```

## 字符数拼接（数据拼接）

- 方法

  用 `+` 将数据进行拼接

- 方法

  数据整合

  ```python
  x = 3 
  x = str(x)
  print("今年我" + x + "岁了！")
  
  >>>今年我3岁了！
  ```

## 数据类型查询

- `type()`函数

  - 作用

    查询数据类型

  ```python
  x = 3 
  print(type(x))
  
  #输出结果告诉我们这是整数型
  >>> <class'int'>
  ```

## 数据转换

![](C:\Users\29678\Desktop\learn\ptyhon笔记\python的基础语法\数据转换.jpg)



## 条件判断`if..elif..else..`

- 单向判断`if` 

  ```python
  if xxx:				#条件
      print(xxx)		#自动缩进，做点什么
  ```

  ```python
  #实例：
  x = 6
  if x >= 6:
       print("你拥有了毁灭宇宙的力量")
  
  >>> 你拥有了毁灭宇宙的力量
  ```



- 双向判断`if...else...` 

  ```python
  if xxx:				#条件
      print(xxx)		#做点什么
  else:				#当if条件不满足时
      print(xxx)		#做点其他的什么
  ```

  ```python
  #实例：
  x = 3
  if x >=6:
      print("你拥有了毁灭宇宙的力量")
  else:
      print("带着卡魔拉去沃弥尔星寻找灵魂宝石")
  ```

- 多向判断`if...elif...else...`

  ```python
  if xxx:				#条件1
      print(xxx)		#做点什么
  elif xxx:			#条件2
      print(xxx)		#做点什么
  elif xxx:			#条件3
      print(xxx)		#做点什么
  else:				#当if和elif的条件都不满足时
      print(xxx)		#做点其他的什么
  ```

  ```python
  #实例：
  x = 5
  if x >= 6:
      print("你拥有了毁灭宇宙的力量")
  elif 0 < x <= 5:
      print("绯红女巫需要亲手毁掉幻视额头上的心灵宝石")
  else:
      print("需要惊奇队长逆转未来")
  ```

  ## if嵌套

  ![](C:\Users\29678\Desktop\learn\ptyhon笔记\python的基础语法\if嵌套.png)

```python
#实例:
historyscore=26
if historyscore>=60:
    print('你已经及格')
    
    if historyscore>=80:
        print('你很优秀')
    else:
        print('你只是一般般')
        
else:
    print('不及格')
    
    if historyscore<30:
        print('学渣')
    else:
        print('还能抢救一下')
        
print('程序结束')
```

## `input()`函数

- 使用

  ```python
  有问有答，有来有往；
  需要在终端处输入信息
  ```

- 赋值

  ```python
  函数好用，赋值第一
  input()函数的结果必须赋值
  ```

- 数据类型

  ```python
  返回类型必为 str
  不管你在终端输入的时整数还是字符串，输出值必为字符串
  ```

- 结果的强制转换

  ```python
  想要整数，源头转换
  输入值需要是整数时，input()函数结果需要强制转换
  ```

```python
实例1:
print("那么，您的选择是什么？ 1 接受，还是 2 放弃呢？")

choice = int(input('请输入您的选择：'))

if choice == 1:
    print('霍格沃茨欢迎您的到来。')
else:
    print('您可是被梅林选中的孩子，我们不接受这个选项。')

>>>那么，您的选择是什么？ 1 接受，还是 2 放弃呢？
   请输入您的选择：1
   霍格沃茨欢迎您的到来。
```

```python
实例2:
money = int(input('你一个月工资多少钱？\n'))

if money >= 10000:
     print('土豪我们做朋友吧！')
elif 5000<money<10000:
    print('我们都是搬砖族。。。')
else:
    print('我负责赚钱养家，你负责貌美如花～')

>>>你一个月工资多少钱？
   20
   我负责赚钱养家，你负责貌美如花～
```

## 列表`list`

- 列表元素组成

  ```python
  student = ['小明','小红','小刚']
  ```

  ![](C:\Users\29678\Desktop\learn\ptyhon笔记\python的基础语法\列表元素组成.png)

- 每个元素都有自己对应的偏移量

  ![](C:\Users\29678\Desktop\learn\ptyhon笔记\python的基础语法\每个元素都有自己对应的偏移量.png)

- 从列表中提取单个元素

  ```python
  students = ['小明','小红','小刚']
  print(students[0])
  
  >>>小明	#调取student列表中的第1页，也就是student[0]
  ```

- 从列表中提取多个元素

  - 选取规则

    ```python
    #左右空，取到头；左要取，右不取
    ```

```python
list = [5,6,7,8,9]
print(list[:])
print(list[2:])
print(list[:2])
print(list[1:3])
print(list[2:4])

>>>[5, 6, 7, 8, 9]
>>>[7, 8, 9]
>>>[5, 6]
>>>[6, 7]
>>>[7, 8]
```

- 给列表增加元素

  - ```python
    增加: .append()
         .extend()
    #用 append()每次只能增加一个元素
    #不过 extend()不会把列表或者元组视为一个整体，而是把它们包含的元素逐个添加到列表中
    ```

  - ```python 
    实例:
    list_1 = ['小明','小红','小刚']
    list_1.append('小花')
    list_1.extend('小白')
    print(list_1)
    
    >>>['小明', '小红', '小刚', '小花', '小', '白']
    ```

- 给列表删除元素

  - ```python
    删除：del
    ```

  - ```python
    list_2 = ['小明','小红','小刚']
    del list_2[1]
    print(list_2)
    
    >>>['小明', '小刚']
    ```

## 元组`type`

- 元组组成元素

  ```python
  ty = ("小明","小红","小刚")
  ```

```python
#元组type的用法和列表用法类似
```

### 列表和元组区别与联系

|                  | 列表list | 元组type |
| :--------------: | :------: | :------: |
| 元素是否可以更改 |   可以   |  不可以  |
| 是否是可迭代对象 |    是    |    是    |

## 字典`dict` 

- 组成元素

  ```python
  dict = {'小明':95,'小红':90,'小刚':90}
  #	键 = key
  #	值 = value
  ```

  ![](C:\Users\29678\Desktop\字典的组成元素.png)

- 给字典增加元素

  - ```python
    #增加元素:
    #第一种:	字典名[key] = value
    #第二种:	字典名.update({"key":"value"})
    ```

  - ```python
    #实例:
    dict = {"小明":96, "小红":90}
    dict["小刚"] = 98
    dict.update({"country":"china"})
    print(dict)
    
    >>>{'小明': 96, '小红': 90, '小刚': 98, 'country': 'china'}
    ```

- 给字典删除元素

  - ```python
    #删除元素:
    #		del 字典名[key]
    ```

  - ```python
    #实例:
    dict_1 = {"小明":96, "小红":90}
    del dict_1["小明"]
    print(dict_1)
    
    >>>{'小红': 90}
    ```

### 列表`list` 和字典`dict` 的异同

- 两者不同点

  ```python
  列表:有序，需要用偏移量来定位
  字典:无序，便通过唯一的键来取值
  ```

- 两者相同点

  ```python
  #first: 两者如果要修改元素，都可以用赋值语句
  #second:支持任意嵌套
  ```

## 循环语句`for...in...`

- `for...in...`循环

  ![](C:\Users\29678\Desktop\for..in..循环.png)

```python
for i in [1,2,3,4,5]:	# i 就是空房间
   print(i)				#空房间学名叫做【元素】[item];可以把它当作一个变量

#有一群数字在排队办业务，也就是列表[1,2,3,4,5]
#它们中的每一个被叫到号的时候(for i in)，就轮流进去一个空房间办业务
#每一个数字进去房间之后，都对计算机说：“喂，我要办这个业务：帮忙把我自己打印出来”，也就是print(i)
#然后计算机忠实的为每一个数字提供了打印服务，将1,2,3,4,5都打印在了屏幕上
#这个过程叫做【遍历】
```

### `range()`函数

```python
#当你想把一段代码固定重复n次时，就可以直接使用 for i in range(n)解决问题
```

![](C:\Users\29678\Desktop\learn\ptyhon笔记\python的基础语法\range()函数.png)

```python
#实例1:
#使用range(x)函数，就可以生成一个从 0 到 x-1 的整数序列
for i in range(3):
    print(i)

>>>0
   1
   2
```

```python
#实例2:
#使用range(a,b) 函数，你可以生成了一个【取头不取尾】的整数序列。
for i in range(13,17):
    print(i)
   
>>> 13
	14
    15
    16
```

```python
#实例3:
#当你想把一段代码固定重复n次时，就可以直接使用for i in range(n)解决问题。
for i in range(4):
    print("哈哈哈")
   
>>> 哈哈哈
	哈哈哈
    哈哈哈
    哈哈哈
```

```python
#实例4:
for i in range(0,10,3):
    print(i)
   
>>> 0
	3
    6
    9
```

## 循环`while`

- 基本句型

  ```python
  while xxx(判断语句):
      xxx(执行代码)
      print(x)
  ```

![](C:\Users\29678\Desktop\learn\ptyhon笔记\python的基础语法\while循环语句.png)

```python
a = 0                #先定义变量a，并赋值
while a < 5:         #设定一个放行条件：a要小于5，才能办事
    a = a + 1  # 满足条件时，就办事：将a+1
    print(a)   # 继续办事：将a+1的结果打印出来 
```

```python
#放行条件:当条件被满足时，就会循环执行while内部的代码（while子句）。
#办事流程:while循环，在满足条件的时候，会一轮又一轮地循环执行代码。
```

### `for..in..`循环 VS `while` 循环

|                 | `for..in..`循环 | `while` 循环 |
| :-------------: | :-------------: | :----------: |
|  循环次数明确   |      Ture       |    False     |
| 循环次数不明确  |      False      |     Ture     |
| 把一件事重复N遍 |      Ture       |     Ture     |

## 布尔值（用数据做判断）

- 计算机用数据做判断的过程

  ```python
  - 用数据做逻辑判断的过程叫做【布尔运算】
  - 【布尔运算】会产生【布尔值】
  - 【布尔值】分为 True (判断为真) 和 False (判断为假)
  - Ture 和 False 就像 【开关】一样，决定 if 语句和 while 循环语句是否运行。
  ```

- 两个数值作比较:

  ```pthon
  #python中的比较运算符
  ```

  | 等于 | 不等于 | 大于 | 小于 | 大于等于 | 小于等于 |
  | :--: | :----: | :--: | :--: | :------: | :------: |
  |  ==  |   !=   |  >   |  <   |    >=    |    <=    |

- 直接用数值做运算

  ```python
  #python中的真假判断
  ```

  |           假           |         其他都是真的          |
  | :--------------------: | :---------------------------: |
  |         False          |             Ture              |
  |           0            | 5(任意整数) ; 1.0(任意浮点数) |
  |      ""(空字符串)      |       "苏东坡"(字符串)        |
  |      []（空列表）      |            [1,2,3]            |
  |      {}（空字典）      |     {1:"春风", 2:"秋分"}      |
  | None(代表的是【空值】) |                               |

- `bool()`函数

  ```python
  #实例:
  print('以下数据判断结果都是【假】：')
  print(bool(False))
  print(bool(0))
  print(bool(''))
  print(bool(None))
  
  print('以下数据判断结果都是【真】：')
  print(bool(True))
  print(bool(1))
  print(bool('abc'))
  
  >>> 以下数据判断结果都是【假】：
  	False
  	False
  	False
  	False
  	以下数据判断结果都是【真】：
  	True
  	True
  	True
  ```

- 布尔值之间的运算

  |  and   |        要求条件都满足才 Ture         |
  | :----: | :----------------------------------: |
  |   or   |    只要求其中一个条件满足就为Ture    |
  |  not   |            计算会反转真假            |
  |   in   |  用来判断一个元素是否在一堆数据之中  |
  | not in | 用来判断一个元素是否不在一堆数据之中 |

## `break` 语句

- `break` 的意思是"打破"，是用来结束循环的，一般写作`if...break`。

```python
# break语句搭配for循环
for...in...:
    ...
    if ...:
        break

# break语句搭配while循环
while...(条件):
    ...
    if ...:
        break
```

```python
#if...break的意思是如果满足了某一个条件，就提前结束循环。
#if...break只能在循环内部使用。
```

```python
#实例:
i = 0
while i<5:
    print('明日复明日')
    i = i+1
    if i==3:  # 当i等于3的时候触发
        break # 结束循环

>>> 明日复明日
	明日复明日
	明日复明日        
```

## `continue` 语句

- `continue` 的意思是”继续“，当某个条件被满足的时候，触发continue语句，将跳过之后的代码，直接回到循环的开始。

```python
# continue语句搭配for循环
for...in...:
    ...
    if ...:
        continue
    ...

# continue语句搭配while循环
while...(条件):
    ...
    if ...:
        continue
    ...
```

```python
#continue的作用就是就是当某个条件为真时，又提前回到循环，而不会执行下面的代码。
#continue只能在循环内部使用。
```

## `pass`语句

- `pass` 的意思是“跳过”

  ```python
  #如果没有pass来占据一个位置表示“什么都不做”，以上的代码执行起来会报错：
  ```

  ```python
  #实例:
  a = int(input('请输入一个整数:'))
  if a >= 100:
      pass
  else:
      print('你输入了一个小于100的数字')
  
  >>> 请输入一个整数:24
  	你输入了一个小于100的数字
  ```

## `else`语句

- `else` 不但可以和 `if` 配合使用，它还能跟 `for` 循环和`while` 循环配合使用。

  ```python
  for ...(item) in ...:
      ...
  else:
      ...
      
  while ...(条件):
      ...
  else:
      ...    
  ```

  ```python
  #实例1(for..in..):
  for i in range(5):
      a = int(input('请输入0结束循环，你有5次机会:'))
      if a == 0:
          print('你触发了break语句，导致else语句不会生效。')    
          break
  else:
      print('5次循环你都错过了，else语句生效了。')
      
  >>> 请输入0结束循环，你有5次机会:3
  	请输入0结束循环，你有5次机会:2
  	请输入0结束循环，你有5次机会:3
  	请输入0结束循环，你有5次机会:3
  	请输入0结束循环，你有5次机会:3
  	5次循环你都错过了，else语句生效了。
  ```

  ```python
  #实例2(while)
  i = 0
  while i<5: 
      a = int(input("请输入0结束循环，你有5次机会:"))
      i = i+1
      if a == 0:
          print('你触发了break语句，导致else语句不会生效。')    
          break
  else:
      print('5次循环你都错过了，else语句生效了。')
  
  >>> 请输入0结束循环，你有5次机会:2
  	请输入0结束循环，你有5次机会:3
  	请输入0结束循环，你有5次机会:2
  	请输入0结束循环，你有5次机会:4
  	请输入0结束循环，你有5次机会:5
  	5次循环你都错过了，else语句生效了。   
  ```

## 四大语句总结

|  break语句   |        从循环内跳出(必须与if语句连用)        |
| :----------: | :------------------------------------------: |
| continue语句 |       跳跃到循环开头(必须和if语句连用)       |
|   pass语句   |          什么都不做(常用在if语句下)          |
|   else语句   | 用在循环句后，如果正常结束循环就执行else语句 |

## 格式化字符串

- 格式化字符串

|      |    含义    |
| :--: | :--------: |
| `%s` | 字符串显示 |
| `%f` | 浮点数显示 |
| `%d` |  整数显示  |

```python
 % 后面的类型码用什么，取决于你希望这个 % 占住的这个位置的数据以什么类型展示出来;如果你希望它以字符串形式展示，那就写 %s ，如果你希望它以整数形式展示，那就写 %d 。
```

```python
#例子:
print(‘血量：’+str(player_life)+’攻击：’+str(player_attack))
print(‘血量：%s 攻击：%s’ % (player_life,player_attack))
```

### 新的”格式化字符串“方法：`format()`函数

```python
#优势1：不用担心用错类型码。
print("%s%d"%("数字:",0))				#普通格式化
print("{}{}".format("数字:",0))		#format()格式化

>>> 数字:0
	数字:0
 
#不设置指定位置时，默认按顺序对应。
print("%d, %d"%(0,1))				#普通格式化
print("{},{}".format(0,1))			#format()格式化

>>> 0,1
	0,1
   
#优势2:当设置指定位置时，按指定的对应。
print("{1},{0}".format(0,1))		#format()格式化

>>>1,0

#优势3:可多次调用format后的数据。
print("%d, %d, %d"%(0,1,0))			#普通格式化
print("{0},{1},{0}".format(0,1))	#format()格式化

>>> 0, 1, 0
	0,1,0
   
#format()函数也接受通过参数传入数据。
name_1 = 'Python'				    #普通格式化
print("i am learning %s"% name_1)

name_2 = "python基础语法"			 #format()格式化
print("我正在学{}".format(name_2))

>>> i am learning Python
	我正在学python基础语法
```

### 参数`end`

- 用来控制换行行数和结尾字符

  ```python
  print("hello" , end = "")
  print("world")
  
  print("hello" , end = "  ")
  print("world")
  
  print("hello" , end = "!")
  print("world")
  
  >>> helloworld
  	hello  world
      hello!world
  ```

### print("")控制换行

- `print()`用来换行，如果要换行必须在你要换行的下一行

  ```python
  print("hello", end = "  ")
  print("")
  print("world")
  
  >>> hello  
  	world
  ```

### time模块(计时器)

- `sleep` 函数

  ```python
  import time   #调用time模块
  time.sleep(secs)   
  #使用time模块下面的sleep()函数，括号里填的是间隔的秒数（seconds，简称secs）
  #time.sleep(1.5)就表示停留1.5秒再运行后续代码
  ```

### random模块

- randint()函数

  ```python
  randint()函数:随机生成整数
  ```

```python
#实例1:
import random 
#调用random模块，与
a = random.randint(1,100)
# 随机生成1-100范围内（含1和100）的一个整数，并赋值给变量a
print(a)

>>36		#随机生成的，可多运行几次看看是否随机生成。
```

## 函数(function)

### 函数的作用

函数是组织好的、可以重复使用的、用来实现单一功能的代码。

```python
#总而言是就是:
	我们之前所写的代码都是立即运行且只能被执行一次，而函数可以让我们整合打包好代码，以便这些代码能够随时被复用，这样能极大地减少代码冗余。
#函数出现的原因:
	随着我们想要实现的功能越来越复杂，代码可能会有几百上千行，这样对写代码和读代码都是一个挑战。如果将一个程序用函数拆分成多个独立的子任务来完成，就会让代码结构变得清晰许多。
```

### 函数的组成

- 内置函数(python本身就携带的函数)

  ![](C:\Users\29678\Desktop\learn\ptyhon笔记\python的基础语法\内置函数.png)

- 参数

  ```python
  【参数】指向的是函数要接收、处理怎样的数据(暂且可以把它理解成自变量)
  ```

  ```python
  #仔细观看图片里的函数后面都跟了个括号;
  #括号里放的东西，也就是我们需要输入给函数的数据，它在函数中被称作【参数】。
  ```

- 函数与参数

  ```python
  len("谁都不在谁都不是")
  #len() : 为函数
  #"谁都不在谁都不是" : 为参数
  ```

### 定义函数的基本语法

```python
def 函数名 (参数):
    函数体
    return 语句
```

```python
#实例: (用y = 3x+5为例子)
def math(x):
    y = 3*x + 5
    return y
#第一行:
def的意思是定义(define)，math是【函数名】（自己取的），再搭配一个英文括号和冒号，括号里面的x是参数（参数名也是自己取）。

#第二行:
def下一行开始缩进的代码就是函数要实现的功能，也叫【函数体】。这里的功能就是：根据x计算出一个值y。

#第三行:
return语句是返回的意思，可以指定函数执行完毕后最终会返回什么值或表达式，否则计算机是无法判断出函数最终要输出什么结果的。
```

### 函数基本语法使用的注意事项

```python
# 函数名：1. 名字最好能体现函数的功能，一般用小写字母和单下划线、数字等组合.
#        2. 不可与内置函数重名（内置函数不需要定义即可直接使用）.
# 参数：根据函数功能，括号里可以有多个参数，也可以不带参数，命名规则与函数名相同.
# 规范：括号是英文括号，后面的冒号不能丢.
# 函数体：函数的执行过程，体现函数功能的语句，要缩进，一般是四个空格.
# return语句：后面可以接多种数据类型，如果函数不需要返回值的话，可以省略.
```

### 函数的调用

```python
函数的调用:就是输入函数名和参数所对应的值，这个过程在函数里叫作参数的传递(pass)。
```

```python
#实例1:
def math(x):
    y =  x ** 2 + x
    return y

a = math(10) 	#math(10)的意思是将整数10赋值给参数x并运行该函数。
print(a)		#函数执行完毕后最终返回了y的值即110，然后将这个结果赋值给变量a，再用print()将变量a打印出来。

>>> 110
```

```python
#实例2:
def my_len(worlds):
    counter = 0
    for i in worlds:
        counter = counter + 1
    return counter
a = '三根皮带，四斤大豆'
worlds = a
print(my_len(worlds))

>>> 9
```

### 参数类型

#### 位置参数

```python
#用例子来说明:
def menu(appetizer, course):
    print('一份开胃菜：' + appetizer)
    print('一份主食：' + course)

menu('话梅花生','牛肉拉面')

>>> 一份开胃菜：话梅花生
	一份主食：牛肉拉面
#这里的'话梅花生'和'牛肉拉面'是对应参数的位置顺序传递的，所以appetizer和course被叫作【位置参数】，当有多个参数的时候，我们就必须按照顺序和数量传递，这也是最常见的参数类型。
```

```python
#如果不按位置顺序传递，极容易出现乌龙或者bug
```

```python
#例如:
def menu(appetizer, course):
    print('一份开胃菜：' + appetizer)
    print('一份主食：' + course + '\n')

menu('牛肉拉面','话梅花生')
menu('话梅花生','牛肉拉面')

>>> 一份开胃菜：牛肉拉面
	一份主食：话梅花生

	一份开胃菜：话梅花生
	一份主食：牛肉拉面
```

```python
#如果怕出现位置安排错误可以选择下面这种形式传递，就不需要理会参数位置
```

```python
def menu(appetizer, course):
    print('一份开胃菜：' + appetizer)
    print('一份主食：' + course + '\n')

menu(course = "牛肉拉面" , appetizer = "话梅花生")   

>>> 一份开胃菜：话梅花生
	一份主食：牛肉拉面
```

#### 默认参数

```python
#如果一个函数的某个参数值总是固定的，那么设置默认参数就免去了每次都要传递的麻烦。
#默认参数必须放在位置参数之后。
```

```python
#实例:
def  menu(appetizer, course, dessert = '绿豆沙'):
    print('一份开胃菜：' + appetizer)
    print('一份主食：' + course)
    print('一份甜品：' + dessert)

menu('话梅花生','牛肉拉面')
#因为已经默认将'绿豆沙'传递给dessert，调用时无须再传递。

>>> 一份开胃菜：话梅花生
	一份主食：牛肉拉面
    一份甜品：绿豆沙0
```

```python
#默认参数并不意味着不能改变。
```

```python
#实例:
def menu(appetizer, course, dessert = '绿豆沙'):
    print('一份开胃菜：' + appetizer)
    print('一份主食：' + course)
    print('一份甜品：' + dessert)

menu('话梅花生','牛肉拉面','银耳羹')

>>> 一份开胃菜：话梅花生
	一份主食：牛肉拉面
	一份甜品：银耳羹
```

```python
#而默认参数为什么会改变呢？
#因为前两个位置参数已经有对应的值传递，Python会自动将'银耳羹'传递给参数dessert，替换了默认参数的默认值。
```

#### 不定参数

```python
#即传递给参数的数量是可选的、不确定的。
#它的格式也是比较特殊的，它的返回值也比较特殊。
#为一个星号*加上参数名。
```

```python
#实例:
def menu(*barbeque):
    for i in barbeque:
        print('一份烤串：' + i)
#括号里的这几个值都会传递给参数barbeque

menu('烤香肠', '烤肉丸')        
menu('烤鸡翅', '烤茄子', '烤玉米')
# 不定长参数可以接收任意数量的值

>>> 一份烤串：烤香肠
	一份烤串：烤肉丸
	一份烤串：烤鸡翅
	一份烤串：烤茄子
	一份烤串：烤玉米
```

##### 解析`print()`函数的参数

```python
print(*objects, sep = ' ', end = '\n', file = sys.stdout, flush = False)
#print()函数的完整的参数
```

```python
#第一个参数objects带了*号，为不定长参数——这也是为什么print()函数可以传递任意数量的参数
#其余四个都是默认参数
```

```python
#实例:
#现在通过修改默认值来改变参数，对比一下下列代码的输出结果。
print('金枪鱼', '三文鱼', '鲷鱼')
print('金枪鱼', '三文鱼', '鲷鱼', sep = '+')
# sep控制多个值之间的分隔符，默认是空格
print('金枪鱼', '三文鱼', '鲷鱼', sep = '+', end = '=?')
# end控制打印结果的结尾，默认是换行

>>> 金枪鱼 三文鱼 鲷鱼
	金枪鱼+三文鱼+鲷鱼
	金枪鱼+三文鱼+鲷鱼=?
```

##### 随机功能

- 可使用`random`模块中的`random.choice()`函数

```python
#实例看返回值的实例
```

### `return`返回多个值

```python
#要返回多个值，只需将返回的值写在return语句后面，用英文逗号隔开即可。
#不可分开写，因为函数在执行的过程中遇到第一个return语句就会停止执行，排在后面的return语句就永远无法执行。
```

```python
#实例1:
import random 
appetizer = ['话梅花生','拍黄瓜','凉拌三丝']
def coupon(money):
    if money < 5:
        a = random.choice(appetizer)
        return a
    elif 5 <= money < 10:
        b = random.choice (appetizer)
        return b, '溏心蛋'

print(coupon(6))
print(type(coupon(6)))

>>> ('凉拌三丝', '溏心蛋')
	<class 'tuple'>
```

```python
#实例2:
#元组和列表一样，可以通过索引来提取当中的某个元素；将元组中的两个元素分别打印出来吧。
#方法一
import random 
appetizer = ['话梅花生','拍黄瓜','凉拌三丝']
def coupon(money):
    if money < 5:
        a = random.choice(appetizer)
        return a
    elif 5 <= money < 10:
        b = random.choice (appetizer)
        return b, '溏心蛋'

result = coupon(6)
# result是一个元组
print(result[0])
print(result[1])

>>> 凉拌三丝
	溏心蛋
    
#方法二
#可以同时定义多个变量，来接收元组中的多个元素
import random

appetizer = ['话梅花生', '拍黄瓜', '凉拌三丝']

def coupon(money):
    if money < 5:
        a = random.choice(appetizer)
        return a, ''
    elif 5 <= money < 10:
        b = random.choice(appetizer)
        return b, '溏心蛋'

dish, egg = coupon(7)
# 元组的两个元素分别赋值给变量dish和egg
print(dish)
print(egg)

>>> 拍黄瓜
	溏心蛋
```

### 变量作用域

```python
#程序中的变量并不是在哪个位置都可以被使用的，使用权限决定于这个变量是在哪里赋值的。
#目前只需了解两种变量作用域
#1.【局部变量】:一个在函数内部赋值的变量仅能在该函数内部使用(局部作用域)
#2.【全局变量】:在所有函数之外赋值的变量，可以在程序的任何位置使用(全局作用域)
```

![](C:\Users\29678\Desktop\learn\ptyhon笔记\python的基础语法\变量作用域.png)

```python
#在上图中可以看出:
#变量rent是在函数外被赋值的，所以它是全局变量，能被sum_cost()函数直接使用。
#而变量variable_cost是在cost()函数内定义的，属于局部变量，其余函数内部如sum_cost()无法访问。
```

如何解决“局部变量”与“全局变量”之间的矛盾

```python
#第一种:
把局部变量都放在函数外，变成全局变量。
#实例:
rent = 3000
utilities = int(input('请输入本月的水电费用'))
food_cost = int(input('请输入本月的食材费用'))
variable_cost = utilities + food_cost 
# 以上均为全局变量
print('本月的变动成本是' + str(variable_cost))

def sum_cost():
    sum = rent + variable_cost
    print('本月的总成本是' + str(sum))

sum_cost()
```

```python
#第二种:
用global语句在函数内修改
#实例1:
def egg(): 
    global quantity
    quantity = 108

egg()
print(quantity)

>>> 108

#实例2:
rent = 3000

def cost():
    global variable_cost
    utilities = int(input('请输入本月的水电费用'))
    food_cost = int(input('请输入本月的食材费用'))
    variable_cost = utilities + food_cost
    print('本月的变动成本是' + str(variable_cost))

def sum_cost():
    sum = rent + variable_cost
    print('本月的总成本是' + str(sum))

cost()
sum_cost()

>>> 请输入本月的水电费用234
	请输入本月的食材费用345
	本月的变动成本是579
	本月的总成本是3579
```

### 函数嵌套

函数嵌套就是:一个函数内部调用其他函数

```python
#最简单的实例:
#这是print()嵌套了len()
#Python会先执行len()函数，得到一个返回值，再由print()打印出来
print(len("我和你"))
```

```python
#实例2:
rent = 3000
def cost():
    utilities = int (input("请输入本月的水电费用"))
    food_cost = int(input("请输入本月的食材费用"))
    variable_cost = utilities + food_cost
    print("本月的变动成本是" + str(variable_cost))
    return variable_cost

def sum_cost():
    sum = rent + cost()
    print("本月的总成本是" + str(sum))
    
sum_cost()

>>> 请输入本月的水电费用61
	请输入本月的食材费用500
	本月的变动成本是561
	本月的总成本是3561
    
   
#cost()函数运行结束后会返回变量variable_cost,而sum_cost()函数内部调用了cost();因此调用sum_cost的时候，cost()也就调用了，并得到返回值variable_cost。
```

```python
#实例3:
def div(num1,num2):
    growth = (num1 - num2) / num2
    percent = str(growth * 100) + "%"
    return percent

def warning():
    print("Error:你确定上个月一毛钱都不赚不亏吗？")
   
def main():
    while True:
        num1 = float(input("请输入本月所获利润"))
        num2 = float(input("请输入上月所获利润"))
        if num2 == 0:
            warning()
        else:
            print("本月的利润增长率:" + div(num1,num2))
            break
            
main()  

>>> 请输入本月所获利润400
	请输入上月所获利润300
	本月的利润增长率:33.33333333333333%
```

## 面向对象编程(Object Oriented Programming)

### 类与对象

```python
类（class）
类是某个特定的群体，实例是群体中某个具体的个体。
```

```python
对象{面向对象编程中的对象(object)}
Python中的对象等于类和实例的集合:即类可以看作是对象，实例也可以看作是对象；例如列表list是个类对象，[1,2]是个实例对象。
```

```python
因此在Python中有这么一句话:万事万物，皆为对象。
```

### 类的创建

- 类中的属性和方法

  ![](C:\Users\29678\Desktop\learn\ptyhon笔记\python的基础语法\类中的属性和方法.png)

- 类的创建

```python
class Computer:
#类的创建:class + 类名 + 冒号，后面语句要缩进
    screen = True
    #类的属性创建:通过赋值语句(即定义"是怎样的")
    def start(self):
    #实例方法的创建:def + 方法名(self):
        print("电脑正在开机中...") 
        #方法具体的执行过程，即定义"能做什么"
       
注:
1.在类中赋值的变量叫做属性，类中定义的函数叫作方法(以此和普通函数区分)
2.实例方法是指类中参数带self的函数，是类方法的一种形式，也是最常用的用法。
3.类名的首字母要大写，一便让我们轻松地辨认出“哦！这个是类！”
```

```python
#小例子:
#创建一个"中国人"的类，并为其创建一个属性和一个方法
#属性:眼睛是黑色的
#方法:打印出"吃饭，选择用筷子。"
class China:
    eye = "black"
    def eat(self):
        print("吃饭，选择用筷子。")
```

### 类的调用

- 类的实例化

  即在某个类下创建一个实例对象。

![](C:\Users\29678\Desktop\learn\ptyhon笔记\python的基础语法\类的实例化.png)

```python
#例如:
class Computer:
    screen = True
    def start(self):
        print("电脑正在开机中...")
my_computer = Computer
print(my_computer.screen)
my_computer.start()
```

```python
#调用的关键在第七行代码: my_computer = Computer().
#这个过程就叫作:类的实例化，即在某个类下创建一个实例对象。
```

- 进一步了解类的调用

```python
class Computer:
    screen = True
    
    def start(self):
        print("电脑正在开机中...")
my_computer = computer()
print(type(my_computer))
print(my_computer)
print(my_computer.screen)
my_computer.start()

>>> <class '__main__.Computer'>
	<__main__.Computer object at 0x000002668EF13FD0>
	True
	电脑正在开机中...
```

```python
<class '__main__.Computer'> 
验证了my_computer属于Computer这个类
```

```python
<__main__.Computer object at 0x000002668EF13FD0>
打印出Computer类的一个实例对象(object)，后面的一串字符表示这个对象的内存地址。
```

```python
True
先是获取到类属性screen对应的值True，再用print()打印出来。
```

```python
电脑正在开机中...
调用方法start()，这个方法的功能是直接打印出'电脑正在开机中...'。
```

```python
#实例1:
class Chinese:
    eye = "black"
    
    def eat(self):
        print("吃饭，选择用筷子。")
      
selymu = Chinese()
print(selymu.eye)
selymu.eat()

>>> black
	吃饭，选择用筷子。
```

```python
#类中创建的属性和方法可以被其所有的实例调用，而且，实例的数目在理论上是无限的；因此我们可以同时“新建”多个实例
#实例2:
class Chinese:
    eye = 'black'

    def eat(self):
        print('吃饭，选择用筷子。')

# 类的实例化：创建多个实例
wufeng = Chinese()
jiangjiang = Chinese()
kaxi = Chinese()

print(jiangjiang.eye)
wufeng.eat()
kaxi.eat()

>>> black
	吃饭，选择用筷子。
	吃饭，选择用筷子。
```

```python 
#类也被称为“实例工厂”，因其为所有实例提供了一套蓝图(即预先设定好有什么属性和方法)。
```

- 归纳

​	创建一个类——类的实例化——用实例调用类的属性和方法。

![](C:\Users\29678\Desktop\learn\ptyhon笔记\python的基础语法\类的创建和调用.png)

### 创建类的两个关键点

#### 特殊参数：self

- ```python
  self会接收实例化过程中传入的数据，当实例对象创建后，实例会代替self,在代码中运行。
  换而言之，self是所有实例的替身。
  ```

```python
#实例1:
#在之前举例的类方法只有一个self参数，实际上类的方法也可以设置多个参数:
class Chinese:

    name = '吴枫'  # 类属性name

    def say(self, someone):  # 带有两个参数的方法
        print(someone + '是中国人')

person = Chinese()
print(person.name)
person.say('吴枫') 
# self调用时要忽略，'吴枫'传给参数someone

>>> 吴枫
	吴枫是中国人
```

```python
实例1这样写没错，但实际上是多此一举，因为只要在say方法内部调用类属性"吴枫"，就可以实现相同的功能。
```

```python
怎么在方法内部调用类属性呢？
如果要在类的外部调用类属性，我们得先创建一个实例，在用实例名.属性的格式调用
因此如果想要在类的内部调用类属性，而实例又还没创建之前，我们就需要有个变量先代替实例接收数据，而这个变量就是参数self。
```

```python
#实例2:
class Chinese:

    name = '吴枫'  # 类属性name

    def say(self):     
        print(self.name + '是中国人')

person = Chinese()   # 创建Chinese的实例person
person.say()         # 调用实例方法

>>> 吴枫是中国人
```

```python
实例2在在最后一行代码运行时，实例person会像参数一样传给self，替换掉self，第六行的self.name等价于person.name。
person.name就相当于调用了类属性name(即"吴枫")，然后跑完整个方法。
```

```python
#实例3:
#作用与实例2相同，只是为了做个代码对比
class Chinese:

    name = '吴枫'  # 类属性name

    def say(person):     
        print(person.name + '是中国人')

person = Chinese()   # 创建Chinese的实例person
person.say()         # 调用实例方法

>>> 吴枫是中国人
```

```python
由此可见，self的作用相当于先给实例占了个位置，等到实例创建好就"功成身退，退位让贤"。
```

```python
同理，如果想在类的方法内部调用其他方法时，我们也需要用到self来表示实例。
```

```python
#实例4:
class Chinese:

    def greeting(self):
        print('很高兴遇见你')

    def say(self):
        self.greeting() 
        print('我来自中国')

person = Chinese()
# 创建实例person
person.say()
# 调用say()方法

>>> 很高兴遇见你
	我来自中国
```

```python
当最后一行实例person调用say()方法时，便会执行say()内部的语句
此时self.greeting()就变成person.greeting()，也就是调用实例方法greeting()，打印出'很高兴遇见你'，再打印出'我来自中国'。
```

- 总结

  ```python
  self代表的是类的实例本身，方便数据的流转。
  因此需要记住两点:
  ```

1. 只要在类中用`def`创建方法时，就必须把`第一个参数`位置留给self，并在调用方法时忽略它（不用给`self`传参）。
2. 当在类的方法`内部`想调用类属性或其他方法时，就要采用`self.属性名`或`self.方法名`的格式。

#### 特殊方法：初始化方法（又叫构造函数）

```python
定义初始化方法的格式:
    def_init_(self)
是由init加左右两边的双下划线组成{initialize"初始化"的缩写}
初始化方法的作用在于:当每个实例对象创建时，该方法内的代码无须调用就会自动运行。
```

```python
#实例1:
class Chinese:

    def __init__(self): 
        print('很高兴遇见你，我是初始化方法')

person = Chinese()

>>> 很高兴遇见你，我是初始化方法
```

```python
利用这个特性，在编写习惯上，我们会在初始化方法内部完成类属性的创建，为类属性设置初始值，这样类中的其他方法就能直接、随时调用。
```

```python
#实例2:
class Chinese:
    def __init__(self):
        self.mouth = 1
        self.eye = 2


    def body(self):
        print("我有%s张嘴巴" % self.mouth)
        print("我有%s只眼睛" % self.eye)


person = Chinese()
person.body()

>>> 我有1张嘴巴
	我有2只眼睛
```

```python
除了设置固定常量，初始化方法同样可以接收其它参数，让传入的这些数据能作为属性在类的方法之间流转。
```

```python
#实例3:
class Chinese:
    def __init__(self, name, birth, region):
        self.name = name
        self.birth = birth
        self.region = region
       
    def born(self):
        print(self.name + "出生在" + self.birth)
       
    def live(self):
        print(self.name + "居住在" + self.region)
       
person = Chinese("吴枫","广东","深圳") #传入初始化方法的参数
person.born()
person.live()

>>> 吴枫出生在广东
	吴枫居住在深圳
```

```python
先来看看实例3传入初始化方法参数的那一行:
    当初始化方法有多个参数的时候，在实例化的时候就要传入相应的值，这里{“吴枫”传给了name;“广东”传给了birth;“深圳”传给了region}
```

```python
如此一来，类的其他方法就能通过self.属性名的形式调用传入的数据了（还记得self是实例的替身吧）
```

```python
或许你可能会有这样的疑惑：不用初始化方法不是也能实现吗？写多个方法不是更麻烦吗？
```

```python
#实例4:
class Chinese:
    def bron(self, name, birth):
        print(name + "出生在" + birth)
       
    def live(self, name ,region):
        print(name + "居住在" +region)
       
person = Chinese()
person.born("吴枫","广东")
person.live("吴枫","深圳")

>>> 吴枫出生在广东
	吴枫居住在深圳
```

```python
实例3与实例4对比:实例4的代码确实少了些
可随着我们想实现的功能愈发复杂，我们会在类内部编写很多的方法，如果我们需要传入的数据能在类中长久保存并能随时调用，初始化方法就是一个不错的解决方案。   
```

## 类的继承

- 理论及概念

![](C:\Users\29678\Desktop\learn\ptyhon笔记\python的基础语法\类的继承.png)

```python
1.在Python中，我们习惯表述是:A类是B类的子类，而B类是A类的父类（或超类）。
2.类的继承，让子类拥有父类拥有的所有属性和方法。
```

### 继承的基础语法

```python
class A(B):  #继承的语法
```

![](C:\Users\29678\Desktop\learn\ptyhon笔记\python的基础语法\继承的基础语法.png)

```python
而子类继承的属性和方法，也会传递给子类创建的实例。
```

```python
#实例1:
class Chinese:
    eye = 'black'

    def eat(self):
        print('吃饭，选择用筷子。')

class Cantonese(Chinese):  
# 通过继承，Chinese类有的，Cantonese类也有
    pass

# 验证子类可以继承父类的属性和方法，进而传递给子类创建的实例
yewen = Cantonese()  
# 子类创建的实例，从子类那间接得到了父类的所有属性和方法
print(yewen.eye)  
# 子类创建的实例，可调用父类的属性
yewen.eat()  
# 子类创建的实例，可调用父类的方法

>>> black
	吃饭，选择用筷子。
```

```python
通过实例1可见：通过一个小括号，子类就能轻轻松松地拥有父类所拥有的一切。
```

```python
#实例2:
class Cat:
    tail = True
    
    def say(self):
        print('喵喵喵喵喵~')
class Ragdoll(Cat):
    pass
hua = Ragdoll()
print(hua.tail)
hua.say()

>>> True
	喵喵喵喵喵~
```

- 很多类在创建时也不带括号，如`class Chinese`。这是否意味它们没有父类吗？
- 并不是；实际上`class Chinese:`在运行时相当于`class Chinese(object):`。
- 而`object`是所有类的父类，我们称其为根类（可理解为类的始祖。）

### `isinstance()`函数

- 用来判断某个实例是否属于某个类。

- 具体用法：输入两个参数（第一个是实例，第二个是类或类组成的元组），输出是布尔值（Ture 或 Flase）。

  ```python
  #实例1:{简单例子}
  print(isinstance(1,int))
  # 判断1是否为整数类的实例
  print(isinstance(1,str))
  
  print(isinstance(1,(int,str)))
  # 判断实例是否属于元组里几个类中的一个
  
  >>> True
  	False
  	True
  ```

  ```python
  #实例2:{正式验证}
  class Chinese:
      pass
  
  class Cantonese(Chinese):
      pass
  
  gonger = Chinese()
  # 宫二，电影《一代宗师》女主，生于东北
  yewen = Cantonese()
  # 叶问，电影《一代宗师》男主，生于广东
  
  print('\n验证1：子类创建的实例同时也属于父类')
  print(isinstance(gonger,Chinese))  
  print(isinstance(yewen,Chinese))  
  
  print('\n验证2：父类创建的实例不属于子类。')
  print(isinstance(gonger,Cantonese))
  
  print('\n验证3：类创建的实例都属于根类。')
  print(isinstance(gonger,object))  
  print(isinstance(yewen,object))
  
  >>> 验证1：子类创建的实例同时也属于父类
  	True
  	True
  
  	验证2：父类创建的实例不属于子类。
  	False
  
  	验证3：类创建的实例都属于根类。
  	True
  	True
  ```

### 总结

|     各级实例和各级类间的关系     |
| :------------------------------: |
| 1.子类创建的实例，同时属于父类； |
|  2.父类创建的实例，不属于子类；  |
|  3.所有实例，都属于根类object。  |

- 在类的继承中，不仅子类属于父类，子类所创建的实例实际上也同时属于父类。
- 理论上，父类可以被无限个子类所继承（这一点好比类的属性方法可以传递给无限个实例）

```python
#举个例子:
如果如果要为每个省级行政区的人各创建一个类，并添加各种属性和方法。那么，只要创建一个父类Chinese，在父类中将共同的属性和方法写好，然后34个类都可以通过类的继承得到Chinese的属性和方法，代码量可以减少十几甚至几十倍。
```

### 类的继承之多层继承

```python
多层继承(属于继承的深度拓展)
```

- 继承不仅可以发生在两个层级之间（即父类-子类），还可以有父类的父类、父类的父类的父类……

![](C:\Users\29678\Desktop\learn\ptyhon笔记\python的基础语法\类的继承之多层继承.png)

- 这样一来，层级就出来了。只要你愿意，你可以继续拓展上面的例子，或往上（地球人），或往下（深圳人）。

```python
#实例1:
class Earthman:
    eye_number = 2

# 中国人继承了地球人
class Chinese(Earthman):
    eye_color = 'black'

# 广东人继承了中国人，同时也继承了地球人。
class Cantonese(Chinese):
    pass

yewen = Cantonese()
print(yewen.eye_number)
print(yewen.eye_color)

>>> 2
	black
```

- 实例`yewen`可以调用父类`Chinese`和父类的父类`Earthman`中的属性。可得结论：子类创建的实例可调用所有层级父类的属性和方法。

### 类的继承之多重继承

```python
多重继承(属于继承的宽度拓展)
```

- 一个类，可以同时继承多个类

```python
语法为: class A(B,C,D):
```

- 假设我们将“出生在江苏，定居在广东的人”设为一个类Yuesu，那么，它的创建语句则为`class Yuesu(Yue,Su)`。
- `class Yuesu(Yue,Su)`括号里`Yue`和`Su`的顺序是有讲究的。和子类更相关的父类会放在更左侧。我认为“出生在江苏，定居在广东的人”在穿着和饮食等方面会更接近广东人，所以将 `Yue` 放在`Su`的左侧。
- 所以，广东人创建的实例在调用属性和方法时，会先在左侧的父类中找，找不到才会去右侧的父类找。（可理解为“就近原则”）

```python
#实例1:
class Su:
    born_city = 'Jiangsu'
    wearing = 'thick'  # 穿得较厚

    def diet(self):
        print('我们爱吃甜。')

class Yue:
    settle_city = 'Guangdong'
    wearing = 'thin'  # 穿得较薄

    def diet(self):
        print('我们吃得清淡。')

class Yuesu(Yue,Su):
    pass

xiaoming = Yuesu()
print(xiaoming.wearing)
print(xiaoming.born_city)
xiaoming.diet()

>>> thin
	Jiangsu
	我们吃得清淡。
```

- 代码中体现的就近原则：越靠近子类（即越靠左）的父类，越亲近，越优先考虑。子类调用属性和方法时，会先在靠左的父类里找，找不到才往右找。

#### 多层继承与多重继承的对比

![](C:\Users\29678\Desktop\learn\ptyhon笔记\python的基础语法\多层继承与多重继承的对比.png)

- 多层继承和多重继承的结合，让继承的类拥有更多的属性和方法，且能更灵活地调用。进而，继承的力量也得以放大了很多倍。

```PYTHON
#实例2:尝试用代码完成下面的继承关系，按照下图类名和属性创建5个类，并打印出C4类的实例的属性name和num。
```

![](C:\Users\29678\Desktop\learn\ptyhon笔记\python的基础语法\多层与多重的训练例子.png)

```python
class C0:
    name = "C0"

class C1:
    num = 1

class C2(C0):
    num = 2

class C3:
    name = "C3"

class C4(C1,C2,C3):
    pass

C5 = C4
print(C5.name)
print(C5.num)

>>> C0
	1
```

- 就近原则中的一个细节：多重继承中，若某父类还有父类的话，会先继续往上找到顶。例如代码中的`ins.name`调用的是`C2`的父类`C0`的值而非 `C3`。

## 类的定制

- 如果只是继承的话就不需要用到继承，只需直接使用父类就行
- 为什么需要继承是因为：子类也可以在继承的基础上进行个性化的定制，包括：（1）创建新属性、新方法；（2）修改继承到的属性或方法。
- 简而言之：类的定制，不仅可以让子类拥有新的功能，还能让它有权修改继承到的代码

### 定制，可以新增代码

- 我们可以在子类下新建属性或方法，让子类可以用上父类所没有的属性和方法。**这种操作，属于定制中的一种：新增代码。**

```python
class Chinese:
    eye = "black"
    def eat(self):
        print("吃饭，选择用筷子。")
   
class Cantonese(Chinese):		#类的传承
    native_place = "guangdong"	#类的定制
    def dialect(self):			#类的定制
        print("我们会说广东话。")
   
yewen = Cantonese()
print(yewen.eye)				#父类的属性能用
print(yewen.native_place)		#子类的定制属性也能用
yewen.eat()						#父类的方法也能用
yewen.dialect()					#子类的定制方法也能用

>>> black
	guangdong
	吃饭，选择用筷子。
	我们会说广东话。
```

### 定制，也可重写代码

- 重写代码，是在子类中，对父类代码的修改

```python
举个例子：已知中国的陆地面积，也知道广东的陆地面积占比为1.88%。
那么，两个类的方法可以写成这样：
class Chinese:
    def land_area(self,area):
        print('我们居住的地方，陆地面积是%d万平方公里左右。'% int(area))

class Cantonese(Chinese):
    # 直接对方法进行重写
    def land_area(self,area):
        print('我们居住的地方，陆地面积是%d万平方公里左右。'% int(area * 0.0188))

yewen = Cantonese
yewen.land_area(0,960)

   
>>> 我们居住的地方，陆地面积是18万平方公里左右。
```

- 虽然问题解决了，但这是个不好的示范。目的达成了，但直接重写并不优雅（有点类似洗去了旧方法，然后补上新方法。）
- 想一想：假设有34个子类需定制这个方法，都是直接重写。那么，假设父类的方法改变，如说法改为“我们脚下的大地的面积有960万平方公里”。那么，就需要将所有子类的代码中的说法也改变。
- 显然，这样对代码的维护很不友好。

```python
#因此下面介绍更优雅的重写方式：
class Chinese:

    def land_area(self,area):
        print('我们居住的地方，陆地面积是%d万平方公里左右。'% area)

class Cantonese(Chinese):
    # 间接对方法进行重写
    def land_area(self, area, rate = 0.0188):
        Chinese.land_area(self, area * rate)
        # 直接继承父类方法，再调整参数。

gonger = Chinese()
yewen = Cantonese()
gonger.land_area(960)
yewen.land_area(960)

>>> 我们居住的地方，陆地面积是960万平方公里左右。
	我们居住的地方，陆地面积是18万平方公里左右。
```

- 子类继承父类方法的操作是在`def`语句后接`父类.方法（参数）`
- 这样一来，父类方法`land_area`中的说法改变，子类也不用去动，因为子类直接继承了父类的方法。只不过，在继承的基础上，通过参数的调整完成了定制。

```python
#参数的调整，可以增加参数（如 rate），也可以改变参数的默认值
#例子如下：
class Chinese:

    def land_area(self,area):
        print('我们居住的地方，陆地面积是%d万平方公里左右。' % area)

class Cantonese(Chinese):
    # 为参数 area 设置默认值。
    def land_area(self, area = 960, rate = 0.0188):
        Chinese.land_area(self, area * rate)

yewen = Cantonese()
yewen.land_area()
# 两个参数都有默认值，所以可以这么调用。

>>> 我们居住的地方，陆地面积是18万平方公里左右。
```

- 通过参数默认值的改变，完成子类的定制，让程序的运行结果为“雷猴！欢迎来到广东。

```python
#实例1:
# 提示：初始化方法的定制，和一般的实例方法的定制是一样的。
class Chinese:
    def __init__(self, greeting='你好', place='中国'):
        self.greeting = greeting
        self.place = place

    def greet(self):
        print('%s！欢迎来到%s。' % (self.greeting, self.place))

# 请为子类完成定制，代码量：两行。
class Cantonese(Chinese):
    def __init__(self,greeting = '雷猴',place='广东'):
        Chinese.__init__(self,greeting,place)

yewen = Cantonese()
yewen.greet()

>>> 雷猴！欢迎来到广东。
```

- 这就是定制：在复用代码的基础上，又能满足个性化的需求。

## 编码

```python
编码的本质就是让只认识0和1的计算机，能够理解我们人类使用的语言符号，并且将数据转换为二进制进行存储和传输。
这种从人类语言到计算机语言转换的形式，就叫做编码表，它让人类语言和计算机语言能够一一对应起来。
要了解编码，我们还得先来聊聊二进制。由于有二进制，0和1这两个数字才能像“太极生两仪，两仪生四象，四象生八卦”一样，涵盖容纳世间所有的信息。
```

### 二进制

```python
说起二进制，我就想起了周幽王烽火戏诸侯。所以接下里我会用烽火这种古老的信息传递形式，来比喻说明计算机是怎么传输和存储数据的。
假设我们都是看守城墙的小兵，你在烽火台A上，我在烽火台B上，只要你那边来了敌人，你就点着烽火台通知我。
如果只有一个烽火台，那么只有“点着火”和“没点火”两种状态，这就像电子元件里“通电”和“没通电”的状态，所以只有0和1.
但是你光告诉我来敌人还不够啊，还得告诉我敌人的数量有多少，让我好call齐兄弟做好准备。现在问题是你要怎么通知我敌人的数量呢？
所以，我们之间就约定了特别的“暗号”，来通知彼此敌情。
```

|        |      烽火      | 二进制 | 十进制 | 敌人数量 |
| :----: | :------------: | :----: | :----: | :------: |
| 状态一 |   两个都没点   |   00   |   0    | 没有敌人 |
| 状态二 | 左边没点右边点 |   01   |   1    | 一个敌人 |
| 状态三 | 左边点右边没点 |   10   |   2    | 两个敌人 |
| 状态四 |   两个都点了   |   11   |   3    | 三个敌人 |

- 所以两个二进制位可以表示十进制的0，1，2，3四种状态。
- 当有三座烽火台的时候不，我们可以表示0-7八种状态（也就是2的3次方）
- 依此类推，当有八座烽火台的时候，我们就能表示2的8次方，也就是256种状态，它由8个0或1组成。

```python
#00000000表示状态0:烽火全暗，一个敌人没有，平安无事，放心睡觉。
#11111111 表示状态255：烽火全亮，来了255个敌人。起来打啊！
```

- 用来存放一位0或1，就是计算机里最小的存储单位，叫做【位】，也叫【比特】（bit）。我们规定8个比特构成一个【字节】（byte），这是计算机里最常用的单位。

| bit位/比特： | 存放一位二进制数，即0或1，最小的存储单位。 |
| ------------ | ------------------------------------------ |
| byte字节:    | 8个二进制位为一个字节（B），最常见的单位。 |

- **bit**和**byte**长得有点像，可别混淆！**1 byte = 8 bit**，也就是1字节等于8比特。

```python
这些计算机单位，可与我们息息相关，你的手机“流量”，就是这么计算的：
```

![](C:\Users\29678\Desktop\learn\ptyhon笔记\level_design\python的基础语法\数据流量.png)

- 而百兆宽带，下载速度最多能达到十多兆，是因为运营商的带宽是以**比特每秒**为单位的，比如100M就是100Mbit/s。
- 而我们常看到的下载速度KB却是以**字节每秒**为单位显示的，1byte = 8bit，所以运营商说的带宽得先除以8，你的百兆宽带下载速度，也就是十几兆了。
- 二进制居然能牵扯出这么多生活中的问题，你是否也很意外？哈哈，其实生活处处是知识呀。

### 编码表

```python
#编码表的历史点
- 大家如果想要互相沟通而不造成混乱，就必须使用相同的编码规则。如果使用了不同的编码规则，那就会彼此读不懂，这就是“乱码”的由来。
- 为了避免乱码，一段世界历史就此启动。一开始，是美国首先出台了**ASCII**编码（读音：**/ˈæski/**），统一规定了常用符号用哪些二进制数来表示。
- 因为英文字母、数字再加上其他常用符号，也就100来个，因此使用7个比特位（最多表示128位）就够用了，所以一个字节中被剩下的那个比特位就被默认为0。
- 再后来呢，这套编码表传入欧洲，才发现这128位不够用啊。比如说法语字母上面还有注音符，这个怎么区分？得！把最后一个比特位也编进来吧。因此欧洲普遍使用一个全字节（8个比特位）进行编码，最多可表示256位，至此，一个字节就用满了！
- 当计算机漂洋过海来到中国后，问题又来了，计算机完全不认识博大精深的中文，当然也没法显示中文；而且一个字节的256位都被占满了，但中国有10万多个汉字，256位连塞牙缝都不够啊。
- 于是中国科学家自力更生，重写了一张编码表，也就是GB2312，它用2个字节，也就是16个比特位，来表示绝大部分（65535个）常用汉字。后来，为了能显示更多的中文，又出台了GBK标准。
- 不仅中国，其他国家也都搞出自己的一套编码标准，这样的话地球村村民咋沟通？日本人发封email给中国人，两边编码表不同，显示的都是乱码。
- 为了沟通的便利，Unicode（万国码）应运而生，这套编码表将世界上所有的符号都纳入其中。每个符号都有一个独一无二的编码，现在Unicode可以容纳100多万个符号，所有语言都可以互通，一个网页上也可以显示多国语言。
- 看起来皆大欢喜。但是！问题又来了，自从英文世界吃上了Unicode这口大锅饭，为迁就一些占用字节比较多的语言，英文也要跟着占两个字节。比如要存储A，原本00010001就可以了，现在偏得用两个字节：00000000 00010001才行，这样对计算机空间存储是种极大的浪费！
- 基于这个痛点，科学家们又提出了天才的想法：UTF-8（8-bit Unicode Transformation Format）。它是一种针对Unicode的可变长度字符编码，它可以使用1~4个字节表示一个符号，根据不同的符号而变化字节长度，而当字符在ASCII码的范围时，就用一个字节表示，所以UTF-8还可以兼容ASCII编码。
- Unicode与UTF-8这种暧昧的关系一言以蔽之：Unicode是内存编码的规范，而UTF-8是如何保存和传输Unicode的手段。
```

- 将上述这段编码史浓缩成一个表格表示，就是：

|     编码表      |            适用性            |                             特点                             |
| :-------------: | :--------------------------: | :----------------------------------------------------------: |
|     ASCII码     | 英文大小写，字符，不支持中文 |                   美国人的发明，占用空间小                   |
| GB2312码、GBK码 |           支持中文           |                     GBK码是GB2312的升级                      |
|    Unicode码    |         支持国际语言         |                     占用空间大，适用性强                     |
|     UTF-8码     |         支持国际语言         | 是Unicode的升级，两者可以非常容易地互相转化，占用空间小。ASCII码被UTF-8码包含 |

- **编码表是计算机世界的字典**

- 接下来，我为你介绍几种编码方案在当前的使用情况。
- 第0，计算机是有自己的工作区的，这个工作区被称为“内存”。数据在内存当中处理时，使用的格式是**Unicode**，统一标准。在**Python3**当中，程序处理我们输入的字符串，是默认使用**Unicode**编码的，所以你什么语言都可以输入。

![](C:\Users\29678\Desktop\learn\ptyhon笔记\level_design\python的基础语法\编码表1.png)

- 第1，数据在硬盘上存储，或者是在网络上传输时，用的是**UTF-8**，因为节省空间。但你不必操心如何转换**UTF-8**和**Unicode**，当我们点击保存的时候，程序已经“默默地”帮我们做好了编码工作。
- 第2，一些中文的文件和中文网站，还在使用**GBK**，和**GB2312**。基于此，有时候面对不同编码的数据，我们要进行一些操作来实现转换。这里就涉及接下来要讲的【encode】（编码）和【decode】（解码）的用法。

### `encode()`和`decode()`

- 编码，即将人类语言转换为计算机语言，就是【编码】**encode()**；反之，就是【解码】**decode()**。它们的用法如下图所表示：

```python
"你想编码的内容".encode("你使用的编码表")
"你想解码的内容".decode("你使用的编码表")
```

```python
#小练习:
print("吴枫".encode("utf-8"))
print("吴枫".encode("gbk"))
print(b"\xe5\x90\xb4\xe6\x9e\xab".decode("utf-8"))
print(b"\xce\xe2\xb7\xe3".decode("gbk"))

>>> b'\xe5\x90\xb4\xe6\x9e\xab'
	b'\xce\xe2\xb7\xe3'
	吴枫
	吴枫
```

- 将人类语言编码后得到的结果，有一个相同之处，就是最前面都有一个**字母b**，比如**b'\xce\xe2\xb7\xe3'**，这代表它是bytes（字节）类型的数据。我们可以用**type()**函数验证一下:

```python
print(type('吴枫'))
print(type(b'\xce\xe2\xb7\xe3')) 

>>> <class 'str'>
	<class 'bytes'>
```

- 所谓的编码，其实本质就是把str（字符串）类型的数据，利用不同的编码表，转换成bytes（字节）类型的数据。
- 我们再来区分下字符和字节两个概念。字符是人们使用的记号，一个抽象的符号，这些都是字符：**'1'， '中'， 'a'， '$'， '￥'** 。
- 而字节则是计算机中存储数据的单元，一个8位的二进制数。
- 编码结果中除了标志性的**字母b**，你还会在编码结果中看到许多**\x**，你再观察一下这个例子：**b'\xce\xe2\xb7\xe3'**。
- **\x**是分隔符，用来分隔一个字节和另一个字节。
- 分隔符还挺常见的，我们在上网的时候，不是会有网址嘛？你经常会看到网址里面有好多的**%**，它们也是分隔符，替换了Python中的**\x**。比如像下面这个：

```python
https://www.baidu.com/s?wd=%E5%90%B4%E6%9E%AB
```

- 它的意思就是在百度里面，搜索“吴枫”，使用的是**UTF-8**编码。你眯着眼睛看一看上面的**UTF-8**编码结果和这一串网址的差异，其实它们除了分隔符以外，是一模一样的。

```python
\xe5\x90\xb4\xe6\x9e\xab 	#python编码“吴枫”的结果
%E5%90%B4%E6%9E%AB			#网址里的 “吴枫”
```

- 此外，用**decode()**解码的时候则要注意，UTF-8编码的字节就一定要用UTF-8的规则解码，其他编码同理，否则就会出现乱码或者报错的情况。

```python
#例如用的"utf-8"换成"gbk":
print(b'\xe6\x88\x91\xe7\x88\xb1\xe4\xbd\xa0'.decode('gbk'))

>>> Traceback (most recent call last):
  File "C:\Users\29678\python\pycharm\pythonProject\wind_changed_programme\draft.py", line 1, in <module>
    print(b'\xe6\x88\x91\xe7\x88\xb1\xe4\xbd\xa0'.decode('gbk'))
UnicodeDecodeError: 'gbk' codec can't decode byte 0xa0 in position 8: incomplete multibyte sequence
```

- 最后我们再来看下**ASCII**编码，它不支持中文，所以我们来转换一个大写英文字母**K**。

```python
print('K'.encode('ASCII'))

>>> b'K'
```

```python
- 你看到大写字母K被编码后还是K，但这两个K对计算机来说意义是不同的。前者是字符串，采用系统默认的Unicode编码，占两个字节。后者则是bytes类型的数据，只占一个字节。这也验证我们前面所说的编码就是将str类型转换成bytes类型。
- 编码知识虽然看起来很琐碎，但它又是非常重要的，如果不能理解这些背景知识，指不定你哪天就会遇到坑，就像隐藏在丛林中的蛇，时不时地咬你一口。而它和我们接下来要教的文件读写也有点关系。
```

## 文件读写

- 文件读写，是Python代码调用电脑文件的主要功能，能被用于读取和写入文本记录、音频片段、Excel文档、保存邮件以及任何保存在电脑上的东西。
- 你可能会疑惑：为什么要在Python打开文件？我直接打开那个文件，在那个文件上操作不就好了吗？
- 一般来说直接打开操作当然是没问题的。但假如你有一项工作，需要把100个Word文档里的资料合并到1个文件上，一个个地复制粘贴多麻烦啊，这时你就能用上Python了。或者，当你要从网上下载几千条数据时，直接用Python帮你把数据一次性存入文件也是相当方便。
- 要不然怎么说，Python把我们从重复性工作中解放出来呢～;【文件读写】，是分为【读】和【写】两部分的，我们就先来瞧瞧【读文件】是怎么实现的？

### 读取文件

- 只有三步：**读：** 打开文件--->读文件--->关闭文件
- 我们先在桌面新建一个**test**文件夹，然后在文件夹里新建一个名为**adc**的txt文件，在里面随便写点儿什么，我写的是：李析沐，李析。
- 我用PyCharm打开这个这个文件是这样的

![](C:\Users\29678\Desktop\learn\ptyhon笔记\level_design\python的基础语法\读取文件1.png)

- 然后，你可以用PyCharm新建一个**open.py**的Python文件，也放在**test**文件夹里，我们就在这里写代码。

- #### **【第一步-开】使用`open()`函数打开文件。**

```python
#语法是这样的:
file1 = open('C:\\Users\\29678\\Desktop\\test\\adc.txt',"r",encoding="utf-8")
```

- `file1`这个变量是存放读取文件数据的，以便对文件进行下一步的操作。
- `open()`函数里面有三个参数

```python
1 - 'C:\\Users\\29678\\Desktop\\test\\adc.txt'
2 - "r"
3 - encoding="utf-8"
```

- **第一个参数是文件的保存地址**，一定要写清楚，否则计算机找不到。注意：我和你的文件地址是不一样的哦。
- 要找到你的文件地址，只需要打开你存放adc.txt文件的地方点击中间框框就会弹出文件的绝对路径。
- 例如我的：

![](C:\Users\29678\Desktop\learn\ptyhon笔记\level_design\python的基础语法\读取文件2.png)

- 文件的地址有两种:**相对路径**和**绝对路径**，这两种地址，Mac和Windows电脑还有点傲娇地不太一样；（我的是Windows系统）
- **绝对路径**就是最完整的路径，**相对路径**指的就是【相对于当前文件夹】的路径，也就是你编写的这个py文件所放的文件夹路径！
- 如果你要打开的文件和**open.py**在同一个文件夹里，这时只要使用相对路径就行了，而要使用其他文件夹的文件则需使用绝对路径。
- Windows系统里，常用**\**来表示绝对路径，**/**来表示相对路径，所以当你把文件拖入终端的时候，绝对路径就变成：

```python
C:\Users\29678\Desktop\test\adc.txt
```

- 但是呢，别忘了**\**在Python中是转义字符，所以时常会有冲突。为了避坑，Windows的绝对路径通常要稍作处理，写成以下两种格式:

```python
open('C:\\Users\\29678\\Desktop\\test\\adc.txt')
#将"\"替换成"\\"

open(r"C:\Users\29678\Desktop\test\adc.txt")
#在路径前加上字母r
```

- **第二个参数表示打开文件时的模式。**这里是字符串 **'r'**，表示 read，表示我们以**读**的模式打开了这个文件。
- 你可能会疑惑，为什么打开的时候就要决定是读还是写，之后决定不行吗？这是因为，计算机非常注意数据的保密性，在打开时就要决定以什么模式打开文件。
- 除了**'r'**,其他还有**'w'**(写入)，**'a'**(追加)等模式，我们稍后会涉及到。
- **第三个参数encoding="utf-8"**,表示的是返回的书籍采用何种编码，一般采用`utf-8`或`gbk`。  {注意这里是写**encoding**而不是**encode**噢。}
- #### **【第二部-读】打开文件**file1**之后，就可以用**read()**函数进行读取的操作了。**

```python
file1 = open('C:\\Users\\29678\\Desktop\\test\\adc.txt',"r",encoding="utf-8")
filecontent = file1.read()  
```

```python
- 第1行代码是我们之前写的。是以读取的方式打开了文件“abc.txt”。
- 第2行代码就是在读取file1的内容，写法就是变量file1后面加个.句点，再加个read(),并且把读到的内容放在变量filencontent里面，这样我们才能拿到文件的内容。
```

- 那么，现在我们想要看看读到了什么数据，可以用**print()**函数看看。请你在自己的电脑里，把剩下的代码补全，可参考下面的代码:

```python
file1 = open('C:\\Users\\29678\\Desktop\\test\\adc.txt',"r",encoding="utf-8")
filecontent = file1.read()
print(filecontent)

>>> 李析沐
	李析
```

- 你这是就会发现，打印了`adc.txt`文件里的内容，它会读成字符串的数据形式。

- #### **【第3步-关】关闭文件，使用的是close()函数**

```python
file1 = open('C:\\Users\\29678\\Desktop\\test\\adc.txt',"r",encoding="utf-8")
filecontent = file1.read()            
print(filecontent)
file1.close() 
```

- 变量file1后面加个点，然后再加个close()，就代表着关闭文件。千万要记得后面的括号可不能丢。

- 为啥要关闭文件呢？原因有两个：1.计算机能够打开的文件数量是有限制的，open()过多而不close()的话，就不能再打开文件了。2.能保证写入的内容已经在文件里被保存好了。

- 文件关闭之后就不能再对这个文件进行读写了。如果还需要读写这个文件的话，就要再次 open() 打开这个文件。

- ### **小总结**

```python
# - 读文件：开——读——关
file1 = open('C:\\Users\\29678\\Desktop\\test\\adc.txt',"r",encoding="utf-8") 
filecontent = file1.read()            
file1.close()

#以读的方式打开文件"adc.txt"
#读取"adc.txt"文件的内容，然后保存在变量filecontent里
#关闭文件
#尤其需要留意的是第二、三步，即读和关的写法。
```

### 写入文件

- 写文件也是三步：打开文件——写入文件——关闭文件

- ### **【第1步-开】以写入的模式打开文件。**

```python
file1 = open('C:\\Users\\29678\\Desktop\\test\\adc.txt',"w",encoding="utf-8")
```

- 这行代码：以写入的模式打开文件"adc.txt"。

- open() 中还是三个参数，其他都一样，除了要把第二个参数改成**'w'**，表示write，即以写入的模式打开文件。

- ### **【第2步-写】往文件中写入内容，使用write()函数**

```python
file1 = open('C:\\Users\\29678\\Desktop\\test\\adc.txt',"w",encoding="utf-8")
file1.write("李大爷\n")
file1.write("李二爷\n")

#最后两行代码：往“abc.txt”文件中写入了“李大爷”和“李二爷”这两个字符串。\n表示另起一行。
```

- 运行程序后，当你打开txt文件查看数据：

![](C:\Users\29678\Desktop\learn\ptyhon笔记\level_design\python的基础语法\写入文件1.png)

- 诶？原来文件里的李析沐和李析去哪里了？
- 是这样子的，**'w'**写入模式会给你暴力清空掉文件，然后再给你写入。如果你只想增加东西，而不想完全覆盖掉原文件的话，就要使用**'a'**模式，表示append，你学过，它是追加的意思。

```python
file1 = open('C:\\Users\\29678\\Desktop\\test\\adc.txt',"a",encoding="utf-8")
file1.write("李大爷\n")
file1.write("李二爷\n")
```

- 运行代码后，当你打开txt文件查看数据：

![](C:\Users\29678\Desktop\learn\ptyhon笔记\level_design\python的基础语法\写入文件2.png)

- ### **【第3步-关】还是要记得关闭文件，使用close()函数**

```python
file1 = open('C:\\Users\\29678\\Desktop\\test\\adc.txt',"a",encoding="utf-8")
file1.write("李大爷\n")
file1.write("李二爷\n")
file1.close()
```

- 还是熟悉的配方，还是熟悉的味道。这样就搞定【写文件】了。

- **对了，有两个小提示：**

- 1.**write()**函数写入文本文件的也是字符串类型。

- 2.在**'w'**和**'a'**模式下，如果你打开的文件不存在，那么**open()**函数会自动帮你创建一个

- ### **小总结**

```python
#写文件：开——写——关
file1 = open("C:\\Users\\29678\\Desktop\\test\\adc.txt","a",encoding="utf-8")
file1.write("李大爷\n")
file1.close()
#以追加的方式打开文件"adc.txt"
#再把字符串"李大爷"写入文件file1
#关闭文件
```

- 这里再顺便补充一个用法，为了避免打开文件后忘记关闭，占用资源或当不能确定关闭文件的恰当时机的时候，我们可以用到关键字with，之前的例子可以写成这样：

```python
#普通写法
file1 = open("adc.txt","a")
file1.write("李大爷")
file1.close()

#使用with关键字的写法
with open("adc.txt","a") as file1:
#with open("文件地址","读写模式") as 变量名:
	#格式:冒号不能丢
    file1.write("李大爷")
    #格式:对文件的操作要缩进
    #格式:无需用close()关闭
```

- 所以之后当你看到**with open...as**这种打开文件的语法格式也要淡定，这种还挺常见的。

- ### `open()`函数的使用表格

|                  |                                                 | b(bytes,字节)            | +                        | b +                               |
| ---------------- | ----------------------------------------------- | ------------------------ | ------------------------ | --------------------------------- |
| `r`(read,读)     | `r`只读，指针在开头，文件不存在则报错           | `rb`二进制只读，其余同左 | `r+`读写，其余同左       | `rb+`二进制读写，其余同左         |
| `w`(write,写)    | `w`只写，文件不存在则新建，存在则覆盖           | `wb`二进制只写，其余同左 | `w+`读写，其余同左       | `wb+`二进制读写，其余同左         |
| `a`(append,追加) | `a`追加，文件存在指针放在末尾，文件不存在则新建 | `ab`二进制追加，其余同左 | `a+`追加且可读，其余同左 | `ab+`二进制追加，且可读，其余同左 |

- 如果我们想写入的数据不是文本内容，而是音频和图片的话，该怎么做呢？
- 我们可以看到里面有**'wb'**的模式，它的意思是以二进制的方式打开一个文件用于写入。因为图片和音频是以二进制的形式保存的，所以使用wb模式就好了。

#### readlines()函数

- 功能为：按行读取。

#### split()函数

- 功能：可以把字符串分开，它会按空格把字符串里面的内容分开。

#### join()函数

- 功能：把字符串合并起来。

```python
a=['c','a','t']
b=''
print(b.join(a))
c='-'
print(c.join(a))

>>> cat
	c-a-t
```

- **join()**的用法是**str.join(sequence)**，str代表在这些字符串之中，你要用什么字符串连接，在这里两个例子，一个是空字符串，一个是横杠，sequence代表数据序列，在这里是列表a。

### 小练习：

- 我们现在自己的电脑中新建一个`scores.txt`,并在此文件中保存以下信息：

```python
罗恩 23 35 44
哈利 60 77 68 88 90
赫敏 97 99 89 91 95 90
马尔福 100 85 90
```

- 希望你来统计这四个学生的魔法作业的总得分，然后再写入一个txt文件。
- 一个非常粗糙的思路应该是：拿到txt文件里的数据，然后对数据进行统计，然后再写入txt文件。
- 首先，毫无疑问，肯定是打开文件，还记得用什么函数吗？

```python
file1 = open(r"C:\Users\29678\Desktop\test\scores.txt",encoding= "utf-8")
```

- 接着呢，就是读取文件了。一般来说，我们是用**read()**函数，但是在这里，我们是需要把四个人的数据分开处理的，我们想要按行处理，而不是一整个处理，所以读的时候也希望逐行读取。
- 因此我们就能使用`readlines()`函数

```python
file1 = open(r"C:\Users\29678\Desktop\test\scores.txt",encoding= "utf-8")
file_lines = file1.readlines()      
file1.close()
print(file_lines)

>>> ['罗恩 23 35 44\n', '哈利 60 77 68 88 90\n', '赫敏 97 99 89 91 95 90\n', '马尔福 100 85 90']
```

- 从结果可以看出：**readlines()** 会从txt文件取得一个列表，列表中的每个字符串就是**scores.txt**中的每一行。而且每个字符串后面还有换行的**\n**符号。
- 这样一来，我们就可以使用**for循环**来遍历这个列表，然后处理列表中的数据；因此接下来可以这样写：

```python
file1 = open(r"C:\Users\29678\Desktop\test\scores.txt",encoding= "utf-8")
file_lines = file1.readlines()
file1.close()

for i in file_lines:    #用for...in...把每一行的数据遍历
    print(i)            #打印变量i
    
>>> 罗恩 23 35 44

	哈利 60 77 68 88 90

	赫敏 97 99 89 91 95 90

	马尔福 100 85 90
```

- 现在我们要把这里每一行的名字、分数也分开。
- 因此我们就能使用`split()`函数；将字符串切分成更细的一个个的字符串。

```python
file1 = open(r"C:\Users\29678\Desktop\test\scores.txt",encoding= "utf-8")
file_lines = file1.readlines()
file1.close()

for i in file_lines:    #用for...in...把每一行的数据遍历
    data = i.split()	#把字符串切分成更细的一个个的字符串
    print(data)            #打印出来看看

>>> ['罗恩', '23', '35', '44']
	['哈利', '60', '77', '68', '88', '90']
	['赫敏', '97', '99', '89', '91', '95', '90']
	['马尔福', '100', '85', '90']
```

- 根据终端得出的结果；这4个列表的第0个数据是姓名，之后的就是成绩。我们需要先统计各人的总成绩，然后把姓名和成绩放在一起。
- 于是我们还可以用`for...in...`循环进行加法的操作。

```python
file1 = open(r"C:\Users\29678\Desktop\test\scores.txt",encoding= "utf-8")
file_lines = file1.readlines()
file1.close()

for i in file_lines:
    data =i.split()    
    sum = 0                    #先把总成绩设为0
    for score in data[1:]:     #遍历列表中第1个数据和之后的数据
        sum = sum + int(score) #然后依次加起来，但分数是字符串，所以要转换    
    result = data[0]+str(sum)  #结果就是学生姓名和总分
    print(result)

>>> 罗恩102
	哈利383
	赫敏561
	马尔福275
```

- 接下来就是把成绩写入一个空的列表，因为这样才有助于我们之后写入一个txt文件。

```python
file1 = open(r"C:\Users\29678\Desktop\test\scores.txt",encoding= "utf-8")
file_lines = file1.readlines()
file1.close()

final_scores = []                        #新建一个空列表
 
for i in file_lines:
    data =i.split()    
    sum = 0                    
    for score in data[1:]:     
        sum = sum + int(score)     
    result = data[0]+str(sum)+'\n'       #后面加上换行符，写入的时候更清晰。    
    final_scores.append(result)#每统计一个学生的总分，就把姓名和总分写入空列表
print(final_scores)
    
>>> ['罗恩102\n', '哈利383\n', '赫敏561\n', '马尔福275\n']
```

- 写到现在，我们就基本处理好了，就只差写入文件咯

```python
file1 = open(r"C:\Users\29678\Desktop\test\scores.txt",encoding= "utf-8")
file_lines = file.readlines()
file.close()

final_scores = [] 

for i in file_lines:
    data =i.split()    
    sum = 0                    
    for score in data[1:]:     
        sum = sum + int(score)     
    result = data[0]+str(sum)+'\n'    
    final_scores.append(result)

winner = open(w,"C:\Users\29678\Desktop\test\winner.txt",encoding='utf-8') 
winner.writelines(final_scores)
winner.close()
```

- 运行结果：

![](C:\Users\29678\Desktop\learn\ptyhon笔记\level_design\python的基础语法\15关的小练习.png)

- 倒数第三行代码是打开一个叫**winner.txt**的文件。(如果电脑中不存在winner.txt的话，这行代码会帮你自动新建一个空白的winner.txt)
- 倒数第二行代码是以**writelines()**的方式写进去，为什么不能用**write()**？因为**final_scores**是一个列表，而**write()**的参数必须是一个字符串，而**writelines()**可以是序列，所以我们使用**writelines()**。
- 最后一行代码是关闭文件。这个，你记得不要把括号丢掉就好咯。

## 模块

- 模块是最高级别的程序组织单元。
- 意味者：模块什么都能封装
- 在模块中，我们不但可以直接存放变量，还能存放函数，还能存放类。

![](C:\Users\29678\Desktop\learn\ptyhon笔记\level_design\python的基础语法\模块-16486255755991.png)

- 更独特的是，定义变量需要用赋值语句，封装函数需要用**def**语句，封装类需要用**class**语句，但封装模块不需要任何语句。
- 之所以不用任何语句，是因为每一份单独的Python代码文件（后缀名是**.py**的文件）就是一个单独的模块。
- 如果你使用过**vscode**或**pycharm**等编程工具编写python程序，每次都需要先创建一个后缀名为**.py**的Python程序文件，才能运行程序：

![](C:\Users\29678\Desktop\learn\ptyhon笔记\level_design\python的基础语法\模块1.png)

- 我们每次运行的代码，本质上都是在运行一个名为**main.py**的程序文件：

![](C:\Users\29678\Desktop\learn\ptyhon笔记\level_design\python的基础语法\模块2-16486260266282.png)

- 像这样：每一个单独的py文件，本质上都是一个模块。
- 封装模块的目的也是为了把程序代码和数据存放起来以便再次利用。如果封装成类和函数，主要还是便于自己调用，但封装了模块，我们不仅能自己使用，文件的方式也很容易共享给其他人使用。
- 所以，我们使用模块主要有两种方式，一种是自己建立模块并使用，另外一种是使用他人共享的模块。

### 使用自己的模块

- 建立模块，其实就是在主程序的py文件中，使用**import**语句导入其他py文件。

#### 模块中相关的常用语句

##### `import`语句

- 我们使用import语句导入一个模块，最主要的目的并不是运行模块中的执行语句，而是为了利用模块中已经封装好的变量、函数、类。

![](C:\Users\29678\Desktop\learn\ptyhon笔记\level_design\python的基础语法\模块4.png)

```python
#案例:
a = '我是模块中的变量a'

def hi():
    a = '我是函数里的变量a'
    print('函数“hi”已经运行！')

class Go2:
    a = '我是类2中的变量a'
    def do2(self):
        print('函数“do2”已经运行！')

print(a)  # 打印变量“a”

hi()  # 调用函数“hi”

A = Go2()  # 实例化“Go2”类
print(A.a)  # 打印实例属性“a”
A.do2()  # 调用实例方法“do2”
```

- 麻雀虽小，五脏俱全。这段代码中基本上展现了所有的调用方式。
- 现在我们要做的是把这段代码拆分成两个模块，把封装好的变量、函数、类，放到**test.py**文件中，把执行相关的语句放到**main.py**文件中。

```python
#test.py
a = '我是模块中的变量a'

def hi():
    a = '我是函数里的变量a'
    print('函数“hi”已经运行！')

class Go2:
    a = '我是类2中的变量a'
    def do2(self):
        print('函数“do2”已经运行！')
```

```python
#main.py
import test

print(test.a)

test.hi()

A = test.Go2()
print(A.a)
A.do2()

>>> 我是模块中的变量a
	函数“hi”已经运行！
	我是类2中的变量a
	函数“do2”已经运行！
```

- 你是否注意到，当我们导入模块后，要使用模块中的变量、函数、类，需要在使用时加上**模块.**的格式。

```python
# 这是主程序main.py
# 请阅读代码注释

import test  # 导入test模块

print(test.a)  # 使用“模块.变量”调用模块中的变量

test.hi()  # 使用“模块.函数()”调用模块中的函数

A = test.Go2()  # 使用“变量 = 模块.类()”实例化模块中的类
print(A.a)  # 实例化后，不再需要“模块.”
A.do2()  # 实例化后，不再需要“模块.”
```

- 学到现在，我们来做个练习。把下面的代码拆分到两个模块中，其中执行语句放到**main.py**文件，封装好的变量、函数和类放到**story.py**文件。

```python
sentence = '从前有座山，'

def mountain():
    print('山里有座庙，')

class Temple:
    sentence = '庙里有个老和尚，'
    def reading(self):
        print('在讲一个长长的故事。')

for i in range(10):
    print(sentence)
    mountain()
    A = Temple()
    print(A.sentence)
    A.reading()
    print()
```

- **story.py**文件{封装变量，函数和类}

```python
sentence = '从前有座山，'

def mountain():
    print('山里有座庙，')

class Temple:
    sentence = '庙里有个老和尚，'
    def reading(self):
        print('在讲一个长长的故事。')
```

- **main.py**文件{执行语句}

```python
import story

for i in range(10):
    print(story.sentence)
    story.mountain()
    A = story.Temple()
    print(A.sentence)
    A.reading()
    print()
```

- **import**语句还有一种用法是**import…as…**。比如我们觉得**import story**太长，就可以用**import story as s**语句，意思是为“story”取个别名为“s”。
- 上面的案例中，**main.py**文件可以写成这样：

```python
import story as s

for i in range(10):
    print(s.sentence)
    s.mountain()
    A = s.Temple()
    print(A.sentence)
    A.reading()
    print()
```

- 另外，当我们需要同时导入多个模块时，可以用逗号隔开。比如**import a,b,c**可以同时导入“a.py，b.py，c.py”三个文件。

##### `from...import...`语句

- **from … import …**语句可以让你从模块中导入一个指定的部分到当前模块。
- 格式如下：

|        |                      `from...import...`                      |
| :----: | :----------------------------------------------------------: |
| 格式： |  `from`（模式名）`import`（指定模块中的变量名/函数名/类名）  |
| 效果： | 1.导入模块中的指定部位（变量名/函数名/类名）                        2.导入后指定的部分可以直接使用，无需加上“模块.”前缀 |

```python
#例子：
# 【文件：test.py】
def hi():
    print('函数“hi”已经运行！')

# 【文件：main.py】
from test import hi  # 从模块test中导入函数“hi”
hi()  # 使用函数“hi”时无需加上“模块.”前缀
```

- 当我们需要从模块中同时导入多个指定内容，也可以用逗号隔开，写成**from xx模块 import a,b,c**的形式。

```python
#案例1：
#【文件:test.py】
a = '我是模块中的变量a'

def hi():
    a = '我是函数里的变量a'
    print('函数“hi”已经运行！')

class Go2:
    a = '我是类2中的变量a'
    def do2(self):
        print('函数“do2”已经运行！')

   
#【文件:main.py】
from test import a,hi,Go2

print(a)  # 打印变量“a”

hi()  # 调用函数“hi”

A = Go2()  # 实例化“Go2”类
print(A.a)  # 打印实例属性“a”
A.do2()  # 调用实例方法“do2”
```

- 对于**from … import …**语句要注意的是，没有被写在**import**后面的内容，将不会被导入。
- 当我们需要从模块中指定所有内容直接使用时，可以写成**【from xx模块 import \*】**的形式，*代表“模块中所有的变量、函数、类”。

```python
#案例2:
#【文件:test.py】
a = '我是模块中的变量a'

def hi():
    a = '我是函数里的变量a'
    print('函数“hi”已经运行！')

class Go2:
    a = '我是类2中的变量a'
    def do2(self):
        print('函数“do2”已经运行！')
#【文件:main.py】
from test import *

print(a)  # 打印变量“a”

hi()  # 调用函数“hi”

A = Go2()  # 实例化“Go2”类
print(A.a)  # 打印实例属性“a”
A.do2()  # 调用实例方法“do2”
```

- 不过，一般情况下，我们不要为了图方便直接使用【from xx模块 import *】的形式。
- 这是因为，**模块.xx**的调用形式能通过阅读代码一眼看出是在调用模块中的变量/函数/方法，而去掉**模块.**后代码就不是那么直观了。
- 做一个小练习：在**main.py**文件导入**story**模块，将类**Temple**的属性**'庙里有个老和尚，'**打印出来。

```python
## 【文件：story.py】

sentence = '从前有座山，'

def mountain():
    print('山里有座庙，')

class Temple:
    sentence = '庙里有个老和尚，'
    def reading(self):
        print('在讲一个长长的故事。')

# 【文件：main.py】

import story

for i in range(10):
    print(story.sentence)
    story.mountain()
    A = story.Temple()
    print(A.sentence)
    A.reading()
    print()
```

- 答案：

```python
from story import Temple
f = Temple
print(f.sentence)
```

- 学会了**import**语句和**from … import …**语句后，你就能愉快地导入模块了。

##### `if __name__ == '__main__'`语句

- 为了解释什么是`【if __name__ == '__main__'】`，我先给讲解一个概念“程序的入口”。
- 对于Python和其他许多编程语言来说，程序都要有一个运行入口。
- 在Python中，当我们在运行某一个py文件，就能启动程序 ——— 这个py文件就是程序的运行入口。

![](C:\Users\29678\Desktop\learn\ptyhon笔记\level_design\python的基础语法\主程序入口1.png)

- 更复杂的情况，我们也可以运行一个主模块，然后层层导入其他模块：

![](C:\Users\29678\Desktop\learn\ptyhon笔记\level_design\python的基础语法\主程序入口2.png)					

- 但是，当我们有了一大堆py文件组成一个程序的时候，为了【指明】某个py文件是程序的运行入口，我们可以在该py文件中写出这样的代码：

```python
#【文件:xx.py】
。。。。。。。。。。
代码块1。。。。。。。
。。。。。。。。。。
if __name__ == '__main__':
    代码块2。。。。。。。。。
    。。。。。。。。。。。。
```

```python
#而上面这段语句的意思是这样的：
1.当xx.py文件被直接运行时，代码块2将被运行。
2.当xx.py文件作为模块是被其他程序导入时，代码块2不被运行。
```

- 这里的`【if __name__ == '__main__'】`就相当于是 Python 模拟的程序入口。Python 本身并没有规定这么写，这是一种程序员达成共识的编码习惯。
- 我用代码来解释一下以上的两种情况：
- 第一种情况：直接运行

```python
#【文件:story.py】
sentence = '从前有坐山，'

def mountain():
    print('山里有座庙，')

class Temple:
    sentence = '庙里有个老和尚，'
    def reading(self):
        print('在讲一个长长的故事。')
#【文件:main.py】
import story

if __name__ == '__main__':
    print(story.sentence)
    story.mountain()
    A = story.Temple()
    print(A.sentence)
    A.reading()
    print()
   
>>> 从前有座山，
	山里有座庙，
	庙里有个老和尚，
	在讲一个长长的故事。
```

- 第二种情况：被其他程序调用

```python
#【文件:story.py】
sentence = '从前有坐山，'

def mountain():
    print('山里有座庙，')

class Temple:
    sentence = '庙里有个老和尚，'
    def reading(self):
        print('在讲一个长长的故事。')
#【文件:main.py】
import story
print("没有执行if __name__ == '__main__'语句")
if __name__ == '__main__':
    print(story.sentence)
    story.mountain()
    A = story.Temple()
    print(A.sentence)
    A.reading()
    print()
   
#【文件:main1.py】{执行文件是main1.py；用以表明main.py文件后的问题}
import main
print(main)

>>> 没有执行if __name__ == '__main__'语句
	<module 'main3' from 'C:\\Users\\29678\\python\\pycharm\\pythonProject\\wind_changed_programme\\level_design_16\\main3.py'>
#输出结果还会有main的存放地址;我的是文件名是main3.py.
```

### 使用他人的模块

- 在之前学习的过程中，常常用到这样的语句：

```python
import time   
print('第一句话，过两秒出现第二句。')
time.sleep(2)
print('第二句话。')

>>> 第一句话，过两秒出现第二句。
	第二句话。
```

- 又或者用到这样的功能：

```python
import random  
a = random.randint(0,100)  # 随机从0-100（包括0和100）之间抽取一个数字
print(a)

>>> 76
```

- 这两个例子中的第一句代码**import time**和**import random**其实就是在导入**time**和**random**模块。

#### 初探借用模块

- time模块和random模块是Python的系统内置模块，也就是说Python安装后就准备好了这些模块供你使用。
- 此外，Python作为一门胶水语言，一个强大的优势就是它拥有许多第三方的模块可以直接拿来使用。
- 如果是第三方编写的模块，我们需要先从Python的资源管理库下载安装相关的模块文件。
- 下载安装的方式是打开终端，Windows用户输入**pip install + 模块名**；苹果电脑输入：**pip3 install + 模块名**，点击enter即可。（需要预装python解释器和pip）
- 比如说，爬虫时我们会需要用到**requests**这个库（库是具有相关功能模块的集合），就需要在终端输入**pip3 install requests**(Mac用户)的指令。
- 现在主要来学习Python的内置模块。
- 如果内置模块是用Python语言编写的话，就能找到py文件：

![](C:\Users\29678\Desktop\learn\ptyhon笔记\level_design\python的基础语法\内置模块1.png)

- 用命令`random.__file__`找出了**random**模块的文件路径，就可以去打开查看它的代码：

```python
from warnings import warn as _warn
from types import MethodType as _MethodType, BuiltinMethodType as _BuiltinMethodType
from math import log as _log, exp as _exp, pi as _pi, e as _e, ceil as _ceil
from math import sqrt as _sqrt, acos as _acos, cos as _cos, sin as _sin
from os import urandom as _urandom
from _collections_abc import Set as _Set, Sequence as _Sequence
from hashlib import sha512 as _sha512
import _random

__all__ = ["Random","seed","random","uniform","randint","choice","sample",
           "randrange","shuffle","normalvariate","lognormvariate",
           "expovariate","vonmisesvariate","gammavariate","triangular",
           "gauss","betavariate","paretovariate","weibullvariate",
           "getstate","setstate", "getrandbits",
           "SystemRandom"]

NV_MAGICCONST = 4 * _exp(-0.5)/_sqrt(2.0)
TWOPI = 2.0*_pi
LOG4 = _log(4.0)
SG_MAGICCONST = 1.0 + _log(4.5)
BPF = 53        # Number of bits in a float
RECIP_BPF = 2**-BPF

class Random(_random.Random):
    VERSION = 3     # used by getstate/setstate

    def __init__(self, x=None):
        self.seed(x)
        self.gauss_next = None

    def seed(self, a=None, version=2):
        if a is None:
            try:
……
……
```

- 由于代码太长，我们就不全部展示了。不过可以看到，random模块的源代码是这样的结构：

![](C:\Users\29678\Desktop\learn\ptyhon笔记\level_design\python的基础语法\random模块.png)

- 函数**random.choice(list)**，功能是从列表中随机抽取一个元素并返回。它的代码被找到了：

```python
def choice(self, seq):
    """Choose a random element from a non-empty sequence."""
    try:
        i = self._randbelow(len(seq))
    except ValueError:
        raise IndexError('Cannot choose from an empty sequence')
    return seq[i]
```

- 函数**random.randint(a,b)**，功能是在a到b的范围随机抽取一个整数。它的代码也被找到了：

```python
def randint(self, a, b):
    """Return random integer in range [a, b], including both end points."""
    return self.randrange(a, b+1)
```

- 像这样，通过阅读源代码我们能找到所有能够使用的变量、函数、类方法。
- 虽然你可以通过看源代码的方式来理解这个模块的功能。但如果你想要高效地学会使用一个模块，看源代码并不是最佳选项。我们接着谈谈“如何自学模块”。

#### 如何自学模块

- 学习模块的核心是搞清楚模块的功能，也就是模块中的**函数**和**类方法**有什么作用，以及具体使用案例长什么样。
- 用自学“random”模块为例，如果英文好的同学，可以直接阅读官方文档：https://docs.python.org/3.6/library/random.html
- 也可以去网上找，搜到教程后，重点关注的是模块中的**函数**和**类方法**有什么作用，然后把使用案例做成笔记。
- 例如random模块的关键知识（也就是比较有用的函数和类方法），可以做成这样的笔记：

```python
import random  # 调用random模块

a = random.random()  # 随机从0-1之间（包括0不包括1）抽取一个小数
print(a)

a = random.randint(0,100)  # 随机从0-100（包括0和100）之间抽取一个数字
print(a)

a = random.choice('abcdefg')  # 随机从字符串，列表等对象中抽取一个元素（可能会重复）
print(a)

a = random.sample('abcdefg', 3) # 随机从字符串，列表等对象中抽取多个不重复的元素
print(a)

items = [1, 2, 3, 4, 5, 6]  # “随机洗牌”，比如打乱列表
random.shuffle(items)
print(items)
```

- 还可以使用**dir()**函数查看一个模块，看看它里面有什么变量、函数、类、类方法。

```python
import random  # 调用random模块

print(dir(random))

>>> ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_floor', '_index', '_inst', '_isfinite', '_log', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
```

- 这就像是查户口一样，可以把模块中的函数（函数和类方法）一览无余地暴露出来。对于查到的结果`"__xx__"`结构的(如`__doc__`)，它们是系统相关的函数，我们不用理会，直接看全英文的函数名即可。
- 这样查询的好处是便于我们继续搜索完成自学。比如我们在列表中看到一个单词“seed”，我们就可以搜一搜**random.seed**的用法
- 甚至不是模块，我们也可以用这种方式自学：**dir(x)**，可以查询到x相关的函数，x可以是模块，也可以是任意一种对象。

```python
#例子表示:
a = ''  # 设置一个字符串
print('字符串：')
print(dir(a))    # 把字符串相关的函数展示出来

a = []  # 设置一个列表
print('列表：')
print(dir(a))    # 把列表相关的函数展示出来

a = {}  # 设置一个字典
print('字典：')
print(dir(a))  # 把字典相关的函数展示出来

>>> 字符串：
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
	列表：
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
	字典：
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
```

- 总结一下模块的学习方法，其实可以归纳成三个问题：

![](C:\Users\29678\Desktop\learn\ptyhon笔记\level_design\python的基础语法\模块三问.png)

- 对了提醒下:
- 比较小的模块（比如random模块）可以通过这样的方式自学，大型模块的学习就比较困难（除非你有充足的专业背景知识）。

#### 学习csv模块

- csv是一种文件格式，你可以把它理解成“简易版excel”。学会了**csv模块**，你就可以用程序处理简单的电子表格了。

![](C:\Users\29678\Desktop\learn\ptyhon笔记\level_design\python的基础语法\csv模块.png)

- 如果要手动新建csv文件，我们可以先新建一个excel表格，然后选择另存为“csv”格式即可。

![](C:\Users\29678\Desktop\learn\ptyhon笔记\level_design\python的基础语法\csv模块2.png)

- 同样的，当我们有了一张csv格式的表格，我们也可以选择另存为“excel”格式。
- 那如何用csv模块读写csv文件呢？
- 先使用import语句导入csv模块，然后用**dir()**函数看看它里面有什么东西：

```python
import csv

# dir()函数会得到一个列表，用for循环一行行打印列表比较直观
for i in dir(csv):
    print(i)

>>> Dialect
	DictReader
	DictWriter
	Error
	QUOTE_ALL
	QUOTE_MINIMAL
	QUOTE_NONE
	QUOTE_NONNUMERIC
	Sniffer
	StringIO
	_Dialect
	__all__
	__builtins__
	__cached__
	__doc__
	__file__
	__loader__
	__name__
	__package__
	__spec__
	__version__
	excel
	excel_tab
	field_size_limit
	get_dialect
	list_dialects
	re
	reader
	register_dialect
	unix_dialect
	unregister_dialect
	writer
```

- 还可以搜索到csv模块的官方英文教程：https://docs.python.org/3.6/library/csv.html
- 以及csv模块的中文教程：https://yiyibooks.cn/xx/python_352/library/csv.html#module-csv

![](C:\Users\29678\Desktop\learn\ptyhon笔记\level_design\python的基础语法\csv模块的实例.png)

- 跟着案例动手试试如何读取csv文件，可见**open()**后面跟了两个参数，用**csv.reader(文件变量)**创建一个reader对象。
- 新建一个名为**test.csv**的文件，里面的内容是这样：

![](C:\Users\29678\Desktop\learn\ptyhon笔记\level_design\python的基础语法\案例1.png)

- 创建一个名为learn_csv.py的文件模块，并编写以下代码：

```python
import csv

with open("test.csv",newline = '')  as f:
    reader = csv.reader(f)
    #使用csv的reader()方法，创建一个reader对象
    for row in reader: 
    #遍历reader对象的每一行
        print(row)

print("读取完毕！")

>>> ['\ufeff1', '2', '3', '4', '5']
	['6', '7', '8', '9', '10']
	['11', '12', '13', '14', '15']
	['16', '17', '18', '19', '20']
	['21', '22', '23', '24', '25']
	['26', '27', '28', '29', '30']
	['31', '32', '33', '34', '35']
	['36', '37', '38', '39', '40']
	读取完毕！
```

- 可以看到终端输出的每一行信息都是一个列表。
- 而写入数据的方式是这样的：

```python
import csv
with open("C:\\Users\\29678\\Desktop\\test\\test.csv","a",newline="") as f:
    # a代表追加写入文件
    writer = csv.writer(f)
    #实例化writer对象
    writer.writerow([1,2,3,4,5])
    #调用“writer.writerow()”方法写入一行数据

```

- 先创建一个变量名为writer（也可以是其他名字）的实例，创建方式是writer = csv.writer(x)，然后使用writer.writerow(列表)就可以给csv文件写入一行列表中的内容。

- 关于open函数的参数，也就是图中的**'a'**，我们来复习一下：

  |                  |                                                 |                          |                          |                                   |
  | :--------------: | :---------------------------------------------: | ------------------------ | ------------------------ | --------------------------------- |
  |                  |                                                 | b(bytes,字节)            | +                        | b +                               |
  |   `r`(read,读)   |      `r`只读，指针在开头，文件不存在则报错      | `rb`二进制只读，其余同左 | `r+`读写，其余同左       | `rb+`二进制读写，其余同左         |
  |  `w`(write,写)   |      `w`只写，文件不存在则新建，存在则覆盖      | `wb`二进制只写，其余同左 | `w+`读写，其余同左       | `wb+`二进制读写，其余同左         |
  | `a`(append,追加) | `a`追加，文件存在指针放在末尾，文件不存在则新建 | `ab`二进制追加，其余同左 | `a+`追加且可读，其余同左 | `ab+`二进制追加，且可读，其余同左 |

- 试试用**writerow()**方法为它追加写入两行列表吧：**['4', '猫砂', '25', '1022', '886']**、**['5', '猫罐头', '18', '2234', '3121']**。

```python
import csv
with open('test.csv','a', newline='',encoding='utf-8') as f:
    writer  = csv.writer(f)
    writer.writerow(['4', '猫砂', '25', '1022', '886'])
    writer.writerow(['5', '猫罐头', '18', '2234', '3121'])
  
>>>    
#显示的就是空白的，但是文件内容已经修改完成
```

- 到这里，最基本的csv表格读取和录入方法我们就已经学会了。**csv模块**虽然比**random模块**稍微复杂一点点，但按照模块三问（这模块有哪些函数可用？有哪些属性或方法可用？使用格式是什么？）的学习方式，我们一样可以学会它的基本用法。
- 小总结：

![](C:\Users\29678\Desktop\learn\ptyhon笔记\level_design\python的基础语法\模块相关语句.png)
