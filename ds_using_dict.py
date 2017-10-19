# 字典，也就是地址簿，将名字（键值）与地址（值）进行配对
# 字典的顺序需要提前设定
# 字典用花括号，基本形式如下
# d = { key1 : value1 , key2 : value2 , key3 : value3}
# “ab”是地址（ Address） 簿（ Book） 的缩写
ab = {
'Swaroop': 'swaroop@swaroopch.com',
'Larry': 'larry@wall.org',
'Matsumoto': 'matz@ruby-lang.org',
'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is", ab['Swaroop'])

# 删除一对键值—值配对
del ab['Spammer']
print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

# format对要输出的参数进行规定和格式化
for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

# 添加一对键值—值配对
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])

ab['Larry'] = 'saramer33@gmail.com'
if 'Larry' in ab:
    print("\nLarry's address is", ab['Larry'])