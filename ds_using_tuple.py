# 元组（tuple）,不能被修改
# 元祖中的项目可以是各种参数，列表，元组...
# zoo = ('item1', 'item2', 'item3')
# 我会推荐你总是使用括号
# 来指明元组的开始与结束
# 尽管括号是一个可选选项。
# 明了胜过晦涩，显式优于隐式。
zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

new_zoo = 'monkey', 'camel', zoo
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)

# 通过指定位置访问项目,第三个项目，第三个项目的第三个项目
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])

print('Number of animals in the new zoo is',len(new_zoo)-1+len(new_zoo[2]))