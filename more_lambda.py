# lambda创建新的函数
points = [{'x': 2, 'y': 3},
          {'x': 4, 'y': 1}]
points.sort(key=lambda i: i['x'])
            # 用lambda定义一个新函数，进行一次自定义排序
            # 按x的升序排列列表的参数
            # 列表是可以改变的，有顺序的
print(points)