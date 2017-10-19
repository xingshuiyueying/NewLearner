# 编写一个命令行地址簿

profile = {'Swaroop': ['892292082','swaroop@swaroopch.com','WHU'],
           'Larry': ['123456789', 'larry@wall.org','WTU'],
           'Matsumoto': ['23638292','matz@ruby-lang.org','HUST'],
           'Hu Ankai': ['10026554','caesarhjk@qq.com','CCNU']}

for name, adress in profile.items():
    print('\nThe profile of {} is {}'.format(name, adress))

print("\nHu Ankai's profile is", profile['Hu Ankai'])

del profile['Matsumoto']

profile['Caesar'] = ['53638783','jhakdh@163.com','ZCEU']

profile['Hu Ankai'] = ['892292888','caesar5@163.com','CCNU']

for name, adress in profile.items():
    print('\nThe profile of {} is {}'.format(name, adress))

if 'Larry' in profile:
    print("\nLarry's profile is", profile['Larry'])

print("\nHu Ankai's newest profile is", profile['Hu Ankai'])
print('\nThere are {} people in the contacts now.\n'.format(len(profile)))
