# 文档字符串，也就是文档说明
def print_max(x, y):
    '''Prints the maximum of two numbers.打印两个数值中的最大数。
    
    The two values must be integers.这两个数都应该是整数'''
    # 如果可能，将其转换至整数类型
    # 文档说明是用三引号括起来的多行内容，第一行类似于标题，第二行为空行，第三行及以后各行为函数详细说明这是一个风格。
    x = int(x)
    y = int(y)
    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')


print_max(3, 5)
print(print_max.__doc__)
# 输出文档字符串的属性用__doc__（这里是双下划线），也就会输出函数说明，功能与help()函数相同
help(print_max)