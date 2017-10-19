class Person:
    def __init__(self, name):
        self.name = name
        # 以上两个name是不一样的前者属于类的实例一部分，后者是一个局部变量

    def say_hi(self):
        print('Hello, my name is', self.name)

# 类被赋予了对象
p = Person('Swaroop')
p.say_hi()
# 前面两行同时也能写作
# Person('Swaroop').say_hi()