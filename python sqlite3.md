# python sqlite3

- SQLite是一个C库，它提供了一个轻量级的基于磁盘的数据库，它不需要单独的服务器进程，并允许使用SQL查询语言的非标准变体访问数据库。一些应用程序可以使用SQLite进行内部数据存储。也可以使用SQLite对应用程序进行原型设计，然后将代码移植到更大的数据库，如PostgreSQL或Oracle。
- sqlite3模块由GerhardHäring编写。它提供了一个符合[**PEP 249**](https://www.python.org/dev/peps/pep-0249)描述的DB-API 2.0规范的SQL接口。

## 创建一个代表数据的对象

- 使用该模块，您必须首先创建一个代表数据库的对象。这里的数据将被存储在文件中：`Connection``example.db`

```python
import sqlite3
conn = sqlite3.connect('example.db')
```

