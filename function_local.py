# 局部变量的赋值只在该作用域中有效，出了作用域就消失
x = 50
def func(x):
    print('x is', x)
    x = 2
    # 这里的2只是局部变量的值
    # 注意这一行的缩进，是对齐的
    print('Changed local x to', x)

func(x)
print('x is still', x)