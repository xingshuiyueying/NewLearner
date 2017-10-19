# range逐步递增，每次只生成一个数字
# for循环与C语言中不同， for（i = 1;i < 6;i++）
# for循环中可以用else,除非有break语句才不会执行
for i in range(1, 5):
    print(i)
else:
    print('The for loop is over')

for i in range(1, 5):
    print(i ** 2)
else:
    print('Over')

# 以2为步数跳过中间数
for i in range(1, 5, 2):
    print(i ** 2)
else:
    print('Over')