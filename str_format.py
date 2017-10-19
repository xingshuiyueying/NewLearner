# 用format格式化参数
age = 20
name = 'Swaroop'
print('{0} was {1} years old when he wrote this book.'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

# 参数索引数字可以省略
age = 20
name = 'Swaroop'
print('{} was {} years old when he wrote this book.'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

# 其他格式转换
# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1.0/3))
# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:_^11}'.format('hello'))
# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

# 用end来阻止换行，用空格替代换行
print('a', end='')
print('b', end=' ')

print('a', end='  ')
print('b', end='  ')
print('c')

# 用反斜杠注明单引号不是行的末尾
print('What\'s your name?')
print("What's your name?")

# 用三引号换行
print('''这是第一行
这是第二行
这是第三行
''')

# 用\n换行
print("这是第一行\n这是第二行\n")

# 一个放置在末尾的反斜杠表示字符串将在下一行继续，但不会添加新的一行。
print("This is the first sentence.  \
This is the second sentence.")

# 同上
print("This is the first sentence.  This is the second sentence.")

# 定义原始变量，用r或R
print(r"Newlines are indicated by \n")

