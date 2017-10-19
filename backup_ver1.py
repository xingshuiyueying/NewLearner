# 这是一个备份程序

import os
import time
# 1.需要备份的文件与目录将被指定在一个列表中。
# 例如在 Windows 下：
# source = ['"C:\\My Documents"', 'C:\\Code']
# 又例如在 Mac OS X 与 Linux 下：
source = ['/home/caesar5/桌面']
# 在这里要注意到我们必须在字符串中使用双引号
# 用以括起其中包含空格的名称。

# 2.备份文件必须储存在主备份目录中
#例如在 Windows 下：
# target_dir = 'E:\\Backup'
# 又例如在 Mac OS X 和 Linux 下：
target_dir = '/home/caesar5/cpp'
# 要记得将这里的目录地址修改至你将使用的路径

# 3.备份文件将打包成zip文件。
# 4.zip文件的文件名由当前的日期与时间构成。
# os.sep将根据你的操作系统给出相应的分隔符，
# 在GNU/Linux 与 Unix 中它会是 '/' ，在 Windows 中它会是 '\\' ，在 Mac OS 中它会是':' 。
# time,strftime在这里给出系统日期和时间
target = target_dir + os.sep + \
    time.strftime('%Y%m%d%H%M%S') + '.zip'

# 如果目标目录不存在，进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # 创建目录

# 5.使用zip命令将文件打包成zip格式
zip_command = 'zip -r {0} {1}'.format(target,
                                      ''.join(source))
# 使用join将列表source转换成字符串，用format将字符串格式化
# zip -r /home/caesar5/cpp/20170508162853.zip /home/caesar5/桌面 就是shell里面的命令行

# 运行备份
print('Zip command is:')
print(zip_command)
print('Running')
if os.system(zip_command) == 0:
    print('Successful backup to',target)
else:
    print('Backup FAILED')