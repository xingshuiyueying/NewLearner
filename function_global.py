# 全局变量
x = 50
def func():
    global x
    # 将x声明为全局变量
    print('x is', x)
    x = 2
    # 全局变量总会起作用
    print('Changed global x to', x)

func()
print('Value of x is', x)