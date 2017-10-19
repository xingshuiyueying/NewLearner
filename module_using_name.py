# 关于了解一个模块是它自己在运行还是被其他模块调用的，也就是谁是主，谁是客。
if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')