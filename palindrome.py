# 判断某个字符串是不是回文
# 这个小程序没有完成

def reverse(text):
    return text[::-1]
    # 步长为-1是字符串翻转

def is_palindrome(text):
    return text == reverse(text)
    # 翻转之后和翻转之前相同

forbidden = (".", "?", "!", ":", ";", "-", "—", "()", "[]", "...", "'", '""', "/", ",", " ")
# 判断中排除符号
something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")