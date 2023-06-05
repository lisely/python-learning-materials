# `Matplotlib`数据可视化

## `Matplotlib`是什么

- `Matplotlib` 提供了一个套面向绘图对象编程的` API` 接口，能够很轻松地实现各种图像的绘制，并且它可以配合 Python GUI 工具（如 `PyQt`、`Tkinter` 等）在应用程序中嵌入图形。同时 `Matplotlib` 也支持以脚本的形式嵌入到 `IPython shell`、`Jupyter` 笔记本、web 应用服务器中使用。

### `Matplotlib`架构组成

- `Matplotlib` 由三个不同的层次结构组成，分别是脚本层、美工层和后端层。

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\Matplotlib架构图.png)

#### 脚本层

- 脚本层是 `Matplotlib` 结构中的最顶层。我们编写的绘图代码大部分代码都在该层运行，它的主要工作是负责生成图形与坐标系。

#### 美工层

- 美工层是结构中的第二层，它提供了绘制图形的元素时的给各种功能，例如，绘制标题、轴标签、坐标刻度等。

#### 后端层

- 后端层是 `Matplotlib` 最底层，它定义了三个基本类，首先是 `FigureCanvas`（图层画布类），它提供了绘图所需的画布，其次是 Renderer（绘图操作类），它提供了在画布上进行绘图的各种方法，最后是 Event（事件处理类），它提供了用来处理鼠标和键盘事件的方法。

### `Matplotlib`图形组成

- `Matplotlib` 生成的图形主要由以下几个部分构成：

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\matplotlib图像组成.png)

#### `Figure`

- 指整个图形，您可以把它理解成一张画布，它包括了所有的元素，比如标题、轴线等。

#### `Axes`

- 绘制 `2D `图像的实际区域，也称为轴域区，或者绘图区。

#### `Axis`

- 指坐标系中的垂直轴与水平轴，包含轴的长度大小（图中轴长为 7）、轴标签（指 x 轴，y轴）和刻度标签。

#### `Artist`

- 您在画布上看到的所有元素都属于 Artist 对象，比如文本对象（title、`xlabel`、`ylabel`）、`Line2D` 对象（用于绘制`2D`图像）等。

### `Matplotlib`功能扩展包

- 许多第三方工具包都对 `Matplotlib` 进行了功能扩展，其中有些安装包需要单独安装，也有一些允许与 `Matplotlib` 一起安装。常见的工具包如下：

```python
- Bashmap：这是一个地图绘制工具包，其中包含多个地图投影，海岸线和国界线；
- Cartopy：这是一个映射库，包含面向对象的映射投影定义，以及任意点、线、面的图像转换能力；
- Excel tools： 这是 Matplotlib 为了实现与 Microsoft Excel 交换数据而提供的工具；
- Mplot3d：它用于 3D 绘图；
- Natgrid：这是 Natgrid 库的接口，用于对间隔数据进行不规则的网格化处理。
```

## `Matplotlib.pyplot API`

- `Matplotlib` 中的 `pyplot` 模块是一个类似命令风格的函数集合，这使得 `Matplotlib` 的工作模式和 `MATLAB` 相似。
- `pyplot` 模块提供了可以用来绘图的各种函数，比如创建一个画布，在画布中创建一个绘图区域，或是在绘图区域添加一些线、标签等。以下表格对这些函数做了简单地介绍。

### 绘图类型

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\绘图类型.png)

### `Image`函数

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\图像函数.png)

### `Axis`函数

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\axis函数.png)

### `Figure`函数

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\Figure函数.png)

## 第一个`Matplotlib`绘图程序

- 本节学习第一个 `Matplotlib` 绘图程序，如何使用 `Matplotlib` 绘制一个简单的折线图。下面绘制一个简单正弦曲线图，它显示了角度与正弦函数值之间的关系。

### 第一个绘图程序

首先导入 `Matplotlib` 包中的 `Pyplot`模块，并以 as 别名的形式简化引入包的名称。

```python
import matplotlib.pyplot as plt
```

接下来，使用 `NumPy` 提供的函数 `arange()` 创建一组数据来绘制图像。

```python
#引入numpy包
import numpy as np
#获得0到2π之间的ndarray对象
x = np.arange(0, math.pi*2, 0.05)
```

上述所得 x 的值作用到 x 轴上，而该值对应的正弦值，也就是 y 值，使用以下方法获取：

```python
y = np.sin(x)
```

使用 plot() 函数对 x、y 进行绘制。

```python
plt.plot(x,y)
```

主要的绘图工作已经完成，不过还需要绘制一些细节，需要我们补充一下，比如图像的标题(title)、x 轴与 y 轴的标签（label）等。

```
plt.xlabel("angle")
plt.ylabel("sine")
plt.title('sine wave')
```

完整的程序代码如下：

```python
from matplotlib import pyplot as plt
import numpy as np
import math
#调用math.pi方法弧度转为角度
x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)
plt.plot(x,y)
plt.xlabel("angle")
plt.ylabel("sine")
plt.title('sine wave')
#使用show展示图像plt.show()
```

代码执行后，显示结果如下：

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\第一次绘图程序.png)

## `PyLab`绘制曲线图

`PyLab` 是一个面向 `Matplotlib` 的绘图库接口，其语法和 `MATLAB` 十分相近。它和 `Pyplot` 模快都够实现 `Matplotlib` 的绘图功能。`PyLab` 是一个单独的模块，随 `Matplotlib` 软件包一起安装，该模块的导包方式和 `Pyplot` 不同，如下所示：

```python 
#Pyplot导包方式
from matplotlib import pyplot as plt
#PyLab导包有两种方式
import pylab
from pylab import *
```

### 基本绘图

提供一对相同长度的数组（或序列），然后使用`plot()`绘制曲线，示例如下：

```python
from numpy import *
from pylab import *
x = linspace(-3, 3, 30)
y = x**2
plot(x, y)
show()
```

输出结果：

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\绘制曲线图.png)

如果您要绘制特殊类型的线条，并想添加一些颜色，`PyLab`提供了如下方法：

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\绘制颜色.png)

使用示例如下：

```python 
from pylab import *
x = linspace(-3, 3, 30)
y = x**2
plot(x, y, 'r.')
show()
```

输出结果：

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\红点曲线图.png)

如果您想在同一绘图区域内绘制多个图形，只需要使用多个绘图命令。示例如下：

```python 
from pylab import *
plot(x, sin(x))
plot(x, cos(x), 'r-')
plot(x, -sin(x), 'g--')
show()
```

输出结果：

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\绘制多条曲线图.png)

如果您想清除图像，直接在程序末尾调用 `clf()` 方法即可。

## `Matplotlib figure`图形对象

通过前面的学习，我们知道`matplotlib.pyplot`模块能够快速地生成图像，但如果使用面向对象的编程思想，我们就可以更好地控制和自定义图像。

在 `Matplotlib` 中，面向对象编程的核心思想是创建图形对象（`figure object`）。通过图形对象来调用其它的方法和属性，这样有助于我们更好地处理多个画布。在这个过程中，`pyplot `负责生成图形对象，并通过该对象来添加一个或多个 axes 对象（即绘图区域）。

`Matplotlib` 提供了`matplotlib.figure`图形类模块，它包含了创建图形对象的方法。通过调用 `pyplot `模块中` figure()` 函数来实例化 `figure `对象。如下所示：

```python
from matplotlib import pyplot as plt
#创建图形对象
fig = plt.figure()
```

该函数的参数值，如下所示：

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\参数值.png)

下面使用 figure() 创建一个空白画布：

```python
fig = plt.figure()
```

我们使用 add_axes() 将 axes 轴域添加到画布中。如下所示：

```python
ax=fig.add_axes([0,0,1,1])
```

add_axes() 的参数值是一个序列，序列中的 4 个数字分别对应图形的左侧，底部，宽度，和高度，且每个数字必须介于 0 到 1 之间。

设置 x 和 y 轴的标签以及标题，如下所示：

```python
ax.set_title("sine wave")
ax.set_xlabel('angle')
ax.set_ylabel('sine')
```

调用 axes 对象的 plot() 方法，对 x 、 y 数组进行绘图操作：

```python
ax.plot(x,y)
```



完整的代码如下所示：

```python
from matplotlib import pyplot as plt
import numpy as np
import math
x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)
fig = plt.figure()a
x = fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.set_title("sine wave")
ax.set_xlabel('angle')
ax.set_ylabel('sine')
plt.show()
```

输出结果如下：

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\画布.png)



## `Matplotlib axes`类使用详解

`Matplotlib` 定义了一个 axes 类（轴域类），该类的对象被称为 axes 对象（即轴域对象），它指定了一个有数值范围限制的绘图区域。在一个给定的画布（figure）中可以包含多个 axes 对象，但是同一个 axes 对象只能在一个画布中使用。

```python
#2D 绘图区域（axes）包含两个轴（axis）对象；如果是 3D 绘图区域，则包含三个。
```

通过调用 add_axes() 方法能够将 axes 对象添加到画布中，该方法用来生成一个 axes 轴域对象，对象的位置由参数`rect`决定。

rect 是位置参数，接受一个由 4 个元素组成的浮点数列表，形如 [left, bottom, width, height] ，它表示添加到画布中的矩形区域的左下角坐标(x, y)，以及宽度和高度。如下所示：

```python
ax=fig.add_axes([0.1,0.1,0.8,0.8])
```

注意：每个元素的值是画布宽度和高度的分数。即将画布的宽、高作为 1 个单位。比如，[ 0.1, 0.1, 0.8, 0.8]，它代表着从画布 10% 的位置开始绘制, 宽高是画布的 80%。

下面介绍 axes 类的其他成员函数，这些函数在绘图过程中都承担着不同的作用:

### legend()绘制图例

axes 类的 legend() 方法负责绘制画布中的图例，它需要三个参数，如下所示：

```python
ax.legend(handles, labels, loc)
```

```python
- labels 是一个字符串序列，用来指定标签的名称；
- loc 是指定图例位置的参数，其参数值可以用字符串或整数来表示；
- handles 参数，它也是一个序列，它包含了所有线型的实例；
```

下面是` loc` 参数的表示方法，分为字符串和整数两种，如下所示：

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\loc参数.png)

### `axes.plot()`

这是 axes 类的基本方法，它将一个数组的值与另一个数组的值绘制成线或标记，plot() 方法具有可选格式的字符串参数，用来指定线型、标记颜色、样式以及大小。

颜色代码如下表：

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\plot颜色.png)

标记符号如下表：

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\plot标记符号.png)

线型表示字符，如下表：

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\plot线性表示字符.png)

下面的例子，以直线图的形式展示了电视、智能手机广告费与其所带来产品销量的关系图。其中描述电视的是带有黄色和方形标记的实线，而代表智能手机的则是绿色和圆形标记的虚线:

```python
import matplotlib.pyplot as plt
y = [1, 4, 9, 16, 25,36,49, 64]
x1 = [1, 16, 30, 42,55, 68, 77,88]
x2 = [1,6,12,18,28, 40, 52, 65]
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
#使用简写的形式color/标记符/线型
l1 = ax.plot(x1,y,'ys-') 
l2 = ax.plot(x2,y,'go--') 
ax.legend(labels = ('tv', 'Smartphone'), loc = 'lower right') # legend placed at lower right
ax.set_title("Advertisement effect on sales")
ax.set_xlabel('medium')
ax.set_ylabel('sales')
plt.show()
```

输出结果如下：

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\2.png)



## `Matplotlib subplot()`函数用法详解

在使用 `Matplotlib` 绘图时，我们大多数情况下，需要将一张画布划分为若干个子区域，之后，我们就可以在这些区域上绘制不用的图形。在本节，我们将学习如何在同一画布上绘制多个子图。

`matplotlib.pyplot`模块提供了一个 subplot() 函数，它可以均等地划分画布，该函数的参数格式如下：

```python
plt.subplot(nrows, ncols, index)
```

`nrows` 与 `ncols` 表示要划分几行几列的子区域（`nrows`*`nclos`表示子图数量），index 的初始值为1，用来选定具体的某个子区域。

例如： subplot(233)表示在当前画布的右上角创建一个两行三列的绘图区域（如下图所示），同时，选择在第 3 个位置绘制子图:

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\子图.png)

如果新建的子图与现有的子图重叠，那么重叠部分的子图将会被自动删除，因为它们不可以共享绘图区域。

```python
import matplotlib.pyplot as plt
plt.plot([1,2,3])
#现在创建一个子图，它表示一个有2行1列的网格的顶部图。
#因为这个子图将与第一个重叠，所以之前创建的图将被删除
plt.subplot(211)
plt.plot(range(12))
#创建带有黄色背景的第二个子图
plt.subplot(212, facecolor='y')
plt.plot(range(12))
```

上述代码运行结果，如下图所示：

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\双图绘制.png)

如果不想覆盖之前的图，需要使用 add_subplot() 函数，代码如下：

```python
import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot([1,2,3])
ax2 = fig.add_subplot(221, facecolor='y')
ax2.plot([1,2,3])
```

执行上述代码，输出结果如下：

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\嵌套图.png)

通过给画布添加 axes 对象可以实现在同一画布中插入另外的图像:

```python
import matplotlib.pyplot as plt
import numpy as np
import math
x = np.arange(0, math.pi*2, 0.05)
fig=plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
axes2 = fig.add_axes([0.55, 0.55, 0.3, 0.3]) # inset axes
y = np.sin(x)
axes1.plot(x, y, 'b')
axes2.plot(x,np.cos(x),'r')
axes1.set_title('sine')
axes2.set_title("cosine")
plt.show()
```

输出结果如下：

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\嵌套图1.png)



## `Matplotlib subplots()`函数详解

`matplotlib.pyplot`模块提供了一个 subplots() 函数，它的使用方法和 subplot() 函数类似。其不同之处在于，subplots() 既创建了一个包含子图区域的画布，又创建了一个 figure 图形对象，而 subplot() 只是创建一个包含子图区域的画布。

subplots 的函数格式如下：

```python
fig , ax = plt.subplots(nrows, ncols)
```

`nrows` 与 `ncols` 表示两个整数参数，它们指定子图所占的行数、列数。

函数的返回值是一个元组，包括一个图形对象和所有的 axes 对象。其中 axes 对象的数量等于 `nrows` * `ncols`，且每个 axes 对象均可通过索引值访问（从1开始）。

下面我们创建了一个 2 行 2 列的子图，并在每个子图中显示 4 个不同的图像:

```python
import matplotlib.pyplot as plt
fig,a =  plt.subplots(2,2)
import numpy as np
x = np.arange(1,5)
#绘制平方函数
a[0][0].plot(x,x*x)
a[0][0].set_title('square')
#绘制平方根图像
a[0][1].plot(x,np.sqrt(x))
a[0][1].set_title('square root')
#绘制指数函数
a[1][0].plot(x,np.exp(x))
a[1][0].set_title('exp')
#绘制对数函数
a[1][1].plot(x,np.log10(x))
a[1][1].set_title('log')
plt.show()
```

上述代码的输出结果如下：

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\并行图.png)



## `Matplotlib subplot2grid()`函数详解

`matplotlib.pyplot` 模块提供了 `subplot2grid()`，该函数能够在画布的特定位置创建 axes 对象（即绘图区域）。不仅如此，它还可以使用不同数量的行、列来创建跨度不同的绘图区域。与 subplot() 和 subplots() 函数不同，`subplot2gird()` 函数以非等分的形式对画布进行切分，并按照绘图区域的大小来展示最终绘图结果。

函数语法格式如下：

```python
plt.subplot2grid(shape, location, rowspan, colspan)
```

参数含义如下：

- shape：把该参数值规定的网格区域作为绘图区域；
- location：在给定的位置绘制图形，初始位置 (0,0) 表示第1行第1列；
- `rowsapan/colspan`：这两个参数用来设置让子区跨越几行几列。

下面，在画布（figure）中添加了行、列跨度均不相同的绘图子区域，然后在每个绘图区上，绘制不同的图形。示例代码如下:

```python
import matplotlib.pyplot as plt
#使用 colspan指定列，使用rowspan指定行
a1 = plt.subplot2grid((3,3),(0,0),colspan = 2)
a2 = plt.subplot2grid((3,3),(0,2), rowspan = 3)
a3 = plt.subplot2grid((3,3),(1,0),rowspan = 2, colspan = 2)
import numpy as np
x = np.arange(1,10)
a2.plot(x, x*x)
a2.set_title('square')
a1.plot(x, np.exp(x))
a1.set_title('exp')
a3.plot(x, np.log(x))
a3.set_title('log')
plt.tight_layout()
plt.show()
```

输出结果如下：

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\任意格式.png)



## `Matplotlib grid()`设置网格格式

通过 `Matplotlib axes`对象提供的 grid() 方法可以开启或者关闭画布中的网格（即是否显示网格）以及网格的主/次刻度。除此之外，grid() 函数还可以设置网格的颜色、线型以及线宽等属性。

grid() 的函数使用格式如下：

```python
grid(color='b', ls = '-.', lw = 0.25)
```

参数含义如下：

- `color`：表示网格线的颜色；
- `ls`：表示网格线的样式；
- `lw`：表示网格线的宽度；

网格在默认状态下是关闭的，通过调用上述函数，网格会被自动开启，如果您只是想开启不带任何样式的网格，可以通过 grid(True) 来实现。

实例如下：

```python
import matplotlib.pyplot as plt
import numpy as np
#fig画布；axes子图区域
fig, axes = plt.subplots(1,3, figsize = (12,4))
x = np.arange(1,11)
axes[0].plot(x, x**3, 'g',lw=2)
#开启网格
axes[0].grid(True)
axes[0].set_title('default grid')
axes[1].plot(x, np.exp(x), 'r')
#设置网格的颜色，线型，线宽
axes[1].grid(color='b', ls = '-.', lw = 0.25)
axes[1].set_title('custom grid')
axes[2].plot(x,x)
axes[2].set_title('no grid')
fig.tight_layout()
plt.show()
```

上述代码执行后，输出结果：

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\输出结果.png)



## `Matplotlib`坐标轴格式

在一个函数图像中，有时自变量 x 与因变量 y 是指数对应关系，这时需要将坐标轴刻度设置为对数刻度。`Matplotlib` 通过 axes 对象的`xscale`或`yscale`属性来实现对坐标轴的格式设置。

示例：右侧的子图显示对数刻度，左侧子图则显示标量刻度：

```python
import matplotlib.pyplot as plt
import numpy as np
fig, axes = plt.subplots(1, 2, figsize=(10,4))
x = np.arange(1,5)
axes[0].plot( x, np.exp(x))
axes[0].plot(x,x**2)
axes[0].set_title("Normal scale")
axes[1].plot (x, np.exp(x))
axes[1].plot(x, x**2)
#设置y轴
axes[1].set_yscale("log")
axes[1].set_title("Logarithmic scale (y)")
axes[0].set_xlabel("x axis")
axes[0].set_ylabel("y axis")
axes[0].xaxis.labelpad = 10
#设置x、y轴标签
axes[1].set_xlabel("x axis")
axes[1].set_ylabel("y axis")
plt.show()
```

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\对数.png)

轴是连接刻度的线，也就是绘图区域的边界，在绘图区域（axes 对象）的顶部、底部、左侧和右侧都有一个边界线（轴）。通过指定轴的颜色和宽度，从而对进行显示格式设置，比如将所有轴的颜色设置为 None，那么它们都会成为隐藏状态，或者也可以给轴添加相应的颜色。以下示例为左侧轴、底部轴分别设置了红色、蓝色，如下所示：

```python
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
#为左侧轴，底部轴添加颜色
ax.spines['bottom'].set_color('blue')
ax.spines['left'].set_color('red')
ax.spines['left'].set_linewidth(2)
#将侧轴、顶部轴设置为None
ax.spines['right'].set_color(None)
ax.spines['top'].set_color(None)
ax.plot([1,2,3,4,5])
plt.show()
```

输出结果如下：

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\输出.png)



## `Matplotlib`刻度和刻度标签

刻度指的是轴上数据点的标记，`Matplotlib` 能够自动的在 x 、y 轴上绘制出刻度。这一功能的实现得益于 `Matplotlib` 内置的刻度定位器和格式化器（两个内建类）。在大多数情况下，这两个内建类完全能够满足我们的绘图需求，但是在某些情况下，刻度标签或刻度也需要满足特定的要求，比如将刻度设置为“英文数字形式”或者“大写阿拉伯数字”，此时就需要对它们重新设置。

`xticks()` 和 `yticks()` 函数接受一个列表对象作为参数，列表中的元素表示对应数轴上要显示的刻度。如下所示：

```python
ax.set_xticks([2,4,6,8,10])
```

x 轴上的刻度标记，依次为 2，4，6，8，10。您也可以分别通过 `set_xticklabels()` 和 `set_yticklabels()` 函数设置与刻度线相对应的刻度标签。

下面示例对刻度和标签的使用方法做了说明:

```python
import matplotlib.pyplot as plt
import numpy as np
import math
x = np.arange(0, math.pi*2, 0.05)
#生成画布对象
fig = plt.figure()
#添加绘图区域
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
y = np.sin(x)
ax.plot(x, y)
#设置x轴标签
ax.set_xlabel('angle')
ax.set_title('sine')
ax.set_xticks([0,2,4,6])
#设置x轴刻度标签
ax.set_xticklabels(['zero','two','four','six'])
#设置y轴刻度
ax.set_yticks([-1,0,1])
plt.show()
```

输出结果如下：

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\输出1.png)



## `Matplotlib`柱状图

柱状图是一种用矩形柱来表示数据分类的图表，柱状图可以垂直绘制，也可以水平绘制，它的高度与其所表示的数值成正比关系。柱状图显示了不同类别之间的比较关系，图表的水平轴 X 指定被比较的类别，垂直轴 Y 则表示具体的类别值。

`Matplotlib` 提供了`bar()`函数来绘制柱状图，它可以应用在`MATLAB` 样式以及面向对象的绘图方法中。当它与 axes 对象一起使用时，其语法格式如下：

```python
ax.bar(x, height, width, bottom, align)
```

该函数的参数说明，如下表所示：

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\bar函数.png)

该函数的返回值是一个 `Matplotlib` 容器对象，该对象包含了所有柱状图。

下面是一个关于 `Matplotlib` 柱状图的简单示例。它用来显示了不同编程语言的学习人数。

```python
import matplotlib.pyplot as plt
#创建图形对象
fig = plt.figure()
#添加子图区域，参数值表示[left, bottom, width, height ]
ax = fig.add_axes([0,0,1,1])
#准备数据
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,17,35,29,12]
#绘制柱状图
ax.bar(langs,students)
plt.show()
```

输出结果如下：

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\bar绘画.png)

通过调整柱状图的宽度，可以实现在同一 x 轴位置绘制多个柱状图。您可以将它们设置成不同的颜色，从而使它们更容易区分。下面示例描述了某工程学院过去四年中，三个专业录取的统招学生数量。

```python
import numpy as np
import matplotlib.pyplot as plt
#准备数据
data = 
[[30, 25, 50, 20],
[40, 23, 51, 17],
[35, 22, 45, 19]]
X = np.arange(4)
fig = plt.figure()
#添加子图区域
ax = fig.add_axes([0,0,1,1])
#绘制柱状图
ax.bar(X + 0.00, data[0], color = 'b', width = 0.25)
ax.bar(X + 0.25, data[1], color = 'g', width = 0.25)
ax.bar(X + 0.50, data[2], color = 'r', width = 0.25)
```

上述代码执行后，将显示四个柱状图，将每个柱状图又均分为三个小柱状图，每个柱状图占据 0.25 个单位。

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\ma绘图.png)

柱状图除了上述使用方法外，还有另外一种堆叠柱状图。所谓堆叠柱状图就是将不同数组别的柱状图堆叠在一起，堆叠后的柱状图高度显示了两者相加的结果值。

bar() 函数提供了一个可选参数`bottom`，该参数可以指定柱状图开始堆叠的起始值，一般从底部柱状图的最大值开始，依次类推。

下面是一个不同国家参加奥林匹克运动会所得奖牌（金银铜）的柱状堆叠图示例，如下所示：

```python
import numpy as np
import matplotlib.pyplot as plt
countries = ['USA', 'India', 'China', 'Russia', 'Germany'] 
bronzes = np.array([38, 17, 26, 19, 15]) 
silvers = np.array([37, 23, 18, 18, 10]) 
golds = np.array([46, 27, 26, 19, 17]) 
# 此处的 _ 下划线表示将循环取到的值放弃，只得到[0,1,2,3,4]
ind = [x for x, _ in enumerate(countries)] 
#绘制堆叠图
plt.bar(ind, golds, width=0.5, label='golds', color='gold', bottom=silvers+bronzes) 
plt.bar(ind, silvers, width=0.5, label='silvers', color='silver', bottom=bronzes) 
plt.bar(ind, bronzes, width=0.5, label='bronzes', color='#CD853F') 
#设置坐标轴
plt.xticks(ind, countries) 
plt.ylabel("Medals") 
plt.xlabel("Countries") 
plt.legend(loc="upper right") 
plt.title("2019 Olympics Top Scorers")
plt.show()
```

在上述代码中，第一次调用`plt.bar()`绘制了黄色柱状图， 第二次调用`plot.bar()`时绘制了灰色柱状图，最后一次调用`plt.bar()`则绘制最底部的柱状图。两个柱状图相接触的位置就是顶部与底部的位置，这样就构成了柱状堆叠图。

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\柱状.png)



## `Matplotlib`饼状图

饼状图用来显示一个数据系列，具体来说，饼状图显示一个数据系列中各项目的占项目总和的百分比。

`Matplotlib` 提供了一个 pie() 函数，该函数可以生成数组中数据的饼状图。您可使用 x/sum(x) 来计算各个扇形区域占饼图总和的百分比。pie() 函数的参数说明如下：

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\饼状.png)

以下示例：关于不同计算机语言学习人数的饼状图。`autopct` 参数设置为 `%1.2f%` ，并将各项所占总和的百分比显示在相对应的扇形区内。

```python
from matplotlib import pyplot as plt
import numpy as np
#添加图形对象
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
#使得X/Y轴的间距相等
ax.axis('equal')
#准备数据
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,17,35,29,12]
#绘制饼状图
ax.pie(students, labels = langs,autopct='%1.2f%%')
plt.show()
```

输出结果如下：

![](C:\Users\29678\Desktop\learn\python笔记\level_design\Matplotlib数据可视化\饼状2.png)







