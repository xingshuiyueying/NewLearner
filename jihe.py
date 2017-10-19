# 集合是无序的
bri = set(['brazil', 'russia', 'india'])
# 检测某些元素是不是集合中的
print('india' in bri)
print('usa' in bri)
# 复制原来的集合并加入新元素
bric = bri.copy()
print(bric)
bric.add('china')
print(bric)
# 检测bri是否是bric的子集
print(bric.issuperset(bri))
# 集合中同样可以删除一些元素
bri.remove('russia')
print(bri)
# 找出两个集合的子集
print(bri & bric)
#整个是无序的

