# 默认参数
def say(message, times=1):
    print(message * times)

# 不对打印次数赋值默认值为1，赋值为5后打印五次
say('Hello')
# 只有位于参数表末尾的参数才能赋予默认值
say('World', 5)