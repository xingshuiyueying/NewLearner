# 列表推导
# 输出原来列表中大于2的数字的2倍组成新的列表
listone = [2, 3, 4]
listtwo = [2*i for i in listone if i > 2]
print(listtwo)