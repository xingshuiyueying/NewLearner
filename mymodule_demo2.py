# 这里是以from...import的形式导入其他模块的
# 形式是“from 模块 import 函数，变量...”
from mymodule import say_hi, __version__
# from mymodule import *用法类似，导入这个模块的所有公共名称，除了双下划线的名称
# 导入该模块的函数和变量之后使用方法如同直接使用函数和变量
# 因此，两个程序（模块）之中不能有相同的函数或参数名称
say_hi()
print('Version', __version__)

help(int)