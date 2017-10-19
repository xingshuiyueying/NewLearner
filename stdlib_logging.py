# os 模块用以和操作系统交互
# platform 模块用以获取平台——操作系统——的信息
#  logging 模块用来记录（ Log）信息

import os
import platform
import logging

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                os.getenv('HOMEPATH'),
                                'test.log')

else:
    logging_file = os.path.join(os.getenv('HOME'),
                                'test.log')
print("Logging to", logging_file)
# 这里打印的是输出日志的地址和名称

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    # 这里获取了系统时间
    filename=logging_file,
    filemode='w',)
# 这里规定了输出日志内容的格式

# 这里是输出日志的内容，形参和实参相对应
logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")