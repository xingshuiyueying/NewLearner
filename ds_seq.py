# 序列无处不在
shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

# Indexing or 'Subscription' operation #
# 索引或“下标（ Subcription） ”操作符 #
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
# 这里列表的-1指的是倒数第一个项目，就是反着数
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

# Slicing on a list # 截取列表中的某些项目
# 截取范围包括起始位置，但不包括结束位置,即[a,b)
# 这里的1至3指的是1,2，即[1,3)
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
# 这里的1至-1指的是[1,-1),-1=最后一个数
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

# 从某一字符串中切片 # 截取某个字符串中的某些字符
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])

# 截取中同样可以包括step [1:10:1]，步长位置在最后一个冒号后面
shoplist = ['apple', 'mango', 'carrot', 'banana']
print(shoplist[::1])
print(shoplist[::2])
print(shoplist[::3])
# 负数总是很意外，反着来
print(shoplist[::-1])