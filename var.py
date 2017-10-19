# 文件名：var.py
# 同一行不同语句之间可用分号连接，使物理行意义更完整可读。
# 然而，没事还是不要用分号。
i = 5
print(i)
i = i + 1
print(i)
s = '''This is a multi-line string.
This is the second line.'''
print(s)

# 有时候，还特别需要把一逻辑行拆分成几个物理行，用反斜杠就好了
s = 'This is a string. \
This continues the string.'
print(s)

# a不是斜杠，是数字5。
a = \
    5
print(a)

# 不能随随便便空格，但是空格和缩进很重要
i = 5
# 下面将发生错误，注意行首有一个空格（已经去掉了）
print('Value is', i)
print('I repeat, the value is', i)





