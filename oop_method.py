class Person:
    def say_hi(self):
        # say_hi执行不需要函数，但是仍然定义了self这个参数名称
        print('Hello, how are you?')
p = Person()
p.say_hi()
# 前面两行同样可以写作
# Person().say_hi()