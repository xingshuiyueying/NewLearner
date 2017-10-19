# 这个程序调用了另外一个程序，被调用的程序需要在相同的位置
# 这里是以import来引入的
import mymodule
mymodule.say_hi()
# 直接调用模块类似于使用函数，只是使用时以“模块.函数（或参数）”表示,被调用模块的所有函数、变量都用这个形式
print('Version', mymodule.__version__)