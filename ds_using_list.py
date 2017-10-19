# 列表就像买东西，要买的东西有个顺序，买完了删去
# shoplist = ['apple', 'mango', 'carrot', 'banana']
# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase.')

# 用end结束语句就不会总是自动换行
print('These items are:', end=' ')
# item就是列表中项目的意思
for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice.')
# append可在列表最后加上一个项目
shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list now')
# sort字面意思就是对列表中的项目进行整理，不会改变字符串
shoplist.sort()
print('Sorted shopping list is', shoplist)
# 列表从零开始
print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
# del删除某个项目
del shoplist[0]
# 上面已经删去的项目就像没有存在过一样，新的列表的第一个项目是banana
print('I bought the', olditem)
print('My shopping list is now', shoplist)

# 善用 help()很重要
help(list)
# 列表是方括号