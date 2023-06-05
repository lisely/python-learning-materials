"""
1、生成器
"""
'''
scq = (num for num in range(1, 10) if num % 2 == 0 )
# print(scq)
print(next(scq))
print(next(scq))
for s in scq:
    print(s)
'''
def test1():
    res1 = yield 1
    print(res1)   # None

    res2 = yield 2
    print(res2)

    res3 = yield 3
    print(res3)

t = test1()
print(t.__next__())  # next() 等价于 t.__next__()
# print(t.__next__())
# print(t.__next__())
# send()函数    t.send(str)
print(t.send("==="))   # t.__next__() + 给上一次的yield附上返回值
# 关闭生成器
t.close()
# print(t.__next__())
"""
2、递归函数
"""
def jc(n):
    if n == 1:
        return 1
    return n * jc(n-1)

print(jc(3))
"""
3、作用域
"""
num = 10
def acb():
    global num
    num = 4
    print(num)

acb()
print(num)