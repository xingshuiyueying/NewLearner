# coding=UTF-8
class SchoolMember:
    '''代表任何学校里的成员。'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''告诉我有关我的细节。'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    # 定义子类时，用基类的名称作为继承元组，也就定义了父子关系
    '''代表一位老师。'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        # 因为子类同样定义了初始化函数，而二者的定义的变量不同
        # 显式调用基类函数的好处是继承基类的初始化对象
        # 如果子类没有定义初始化，它会自动调用基类的初始化函数
        # 子类的功能也不会实现
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        # 这里调用的是子类的函数，程序首先从当前所在的类开始寻找
        # 找不到才会去基类找相应的函数
        print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
    '''代表一位学生。'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

# 打印一行空白行
print()

members = [t, s]
for member in members:
    # 对全体师生工作
    member.tell()