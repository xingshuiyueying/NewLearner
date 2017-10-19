# encoding=utf-8
import io
# 打开模式可以是阅读模式（'r' ） ，写入模式（'w' ） 和追加模式（'a' ） 。
# 我们还可以选择是通过文本模式（'t' ） 还是二进制模式（'b' ） 来读取、写入或追加文本。
# 在默认情况下， open() 会将文件视作文本（ text） 文件，并以阅读（ read） 模式打开它。

f = io.open("abc.txt", "wt", encoding="utf-8")
f.write(u"Imagine non-English language here")
f.close()
text = io.open("abc.txt", encoding="utf-8").read()
print(text)

print(u'hello world')
print(type(u'hello world'))
# 以上都是Python2下面的写法，所有字符串前面带u

