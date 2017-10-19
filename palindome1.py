# 网上copy下来的,未完成要求
# 设置需要过虑的标点符号
forbidden = (".", "?", "!", ":", ";", "-", "—", "()", "[]", "...", "'", '""', "/", ",", " ")
# 获取一个字符串，书中要求确认"Rise to vote, sir."是回文
text = input("请输入：")
#将字符串倒过来
def reverse(text):
    str_tmp = []
    str = ""
    for i in range(0,len(text)):
        if text in forbidden:
            continue
        else:
            str_tmp.append(text.lower())#方便比较，将字母转成小写字母
            return str.join(str_tmp)[::-1]
            #做是否是回文检测
def is_palindrome(text):
    str_tmp = []
    str = ""
    for i in range(0,len(text)):
        if text in forbidden:
            continue
        else:
            str_tmp.append(text.lower())
            return str.join(str_tmp) == reverse(text)

#输出检测结果
if is_palindrome(text):
    print(text, "是回文")
else:
    print(text, "不是回文")