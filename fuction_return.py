# return返回函数，中断函数，返回一个值。
def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y


print(maximum(3, 9))

# 每一个函数都在其末尾隐含了一句 return None,所以会返回一个None
def some_function():
    pass
print(some_function())