# python re.match函数

- re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。

## 函数语法:

```python
re.match(pattern, string, flags=0)
```

### 函数说明：

![]()![re.match函数说明](C:\Users\29678\Desktop\re.match函数说明.png)

- 匹配成功re.match方法返回一个匹配的对象，否则返回None。
- 我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。

![](C:\Users\29678\Desktop\匹配对象方法.png)

实例一：

```python
import re
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

>>> (0, 3)
	None
```

实例二：

```python
import re
 
line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# (.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
   print("matchObj.group(0):", matchObj.group(0))
else:
   print ("No match!!")

>>> matchObj.group() :  Cats are smarter than dogs
	matchObj.group(1) :  Cats
	matchObj.group(2) :  smarter
	matchObj.group(0): Cats are smarter than dogs
```

