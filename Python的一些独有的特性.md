# Python的一些独有的特性

## 01	为什么会出现这种情况，其底层逻辑是什么

当我给X赋值是一个不可变的类型时，会改变当前的内存地址

例如：

```python
x=2
print(id (x))
```

输出结果是：162430048

```python
x=2
print(id(x))
x=5
print(id(x))
```

输出结果是：162430048    162430096



## 02   python没有常量这个数据类型

程序员之间的规定：如果这个变量的命名都是大写字母，那么就视为一个常量 



## 03   python中 ' int ' 是没有大小局限的

很多教材中都会说有局限

一直试大小会出现死机



