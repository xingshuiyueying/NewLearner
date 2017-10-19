# 这是一个字符串对象
name = 'Swaroop'
# 检测开始的字母
if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')
# 检测是否包含某个字符串
if 'a' in name:
    print('Yes, it contains the string "a"')
# 检测是否包含某字符串及其位置
# find方法用于定位字符串中给定的子字符串的位置。如果找不到相应的子字符串， find会返回 -1。
if name.find('war') != -1:
    print('Yes, it contains the string "war"')

# 插入定界符，分隔符
delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))