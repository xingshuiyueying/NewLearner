# 模块使用，sys为系统模块
import sys
print('The command line arguments are:')
for i in sys.argv:
    # sys.argv是sys模块的一系列字符串列表，类似于矩阵，它也包括命令行参数
    print(i)

# 运行的是python module_using_sys.py we are arguments
# 运行脚本之后的是命令行参数，将其赋值给了sys.argv，和脚本一起存储在sys.argv中
print('\n\n The PYTHONPATH is', sys.path, '\n')

import os;
# 查看程序目前所处在的目录
print(os.getcwd())