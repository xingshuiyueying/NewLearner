# try...except的使用
try:
    text = input('Enter something --> ')
except EOFError:
    print('Why did you do an EOF on me?')
    # Press ctrl + d
except KeyboardInterrupt:
    print('You cancelled the operation.')
    # Press ctrl + c
else:
    print('You entered {}'.format(text))