# print('hello world!')
#
# if 3 > 0:
#     print('yes')
#     print('ok')
#
# print('abc')
# # print语句各项之间默认用空格分隔
# print('Hello world')
# # print语句各项之间也可以自定义分隔符
# print('Hello','World',sep='***')
# # 字符串可以使用+进行拼接
# print('Hello'+'world')
# #print语句默认最后会加入一个回车\n 可以用end来自定义结束
# print('Hello World',end='1231')
# print('hello world')
# a = input('number: ')
# print(a)
# #b = a+10   input读入的数据都是字符型 字符不能和数字相加
# print(int(a)+10)  #将a转成整数后和10相加 再打印出来结 果
# print(a+str(10))  #将10转成字符串后和a拼接 再打印出来 结果
# a = input('shu')
# acp={'name':'大锤','age':18}
# a=input("name:")
# print('age:',acp['age'])
# #help(print)
# print("hello World")
# print('hello'+' world')
# print('hello','world')
# print('hell0','world',sep='***')
# print('hello','world',sep='***',end='aaaa')
# help(input)
# num = input ("Number:")
# print(num + int(10))
#num = input ("Number:")
#print(num + str(10))
#num = input ("Number:")
#print(int(num) + 10)
# words = ('tom is sundasha bushi')
# if 'tom' in words:
#     print ('yes')
# if 'tom' not in words:
#     print('not in')
# else:
#     print('tom in words')
# if -0.0:
#     print('ok')
# if -0.01:
#     print('ok')
# if ' ':
#     print('space is ture')
# if '':
#     print('空字串是Flase')
# if not None:
#     print('None也是False 表示为空')
# import getpass
# a = input ('用户名：')
# b = getpass.getpass ('密码：')
# if a  == 'bob'and b == '123456' :
#     print('login successful')
# else:
#     print('login inorrect')
# import os
# os.chmod('/tmp/zhuji', 0o600)
# import random
# number = random.randint(1,100)
# print('number -> ',number)
# answer = int(input('猜数1-100：'))
# if answer > number:
#     print('猜大了')
# elif answer < number:
#     print('猜小了')
# else:
#     print('猜对了')
# a = 100
# b = 80
# if a < b :
#     small = a
# else:
#     small = b
# fenshu = int(input('成绩：'))
# if 70> fenshu >= 60:
#     print('及格')
# elif 80 > fenshu >= 70:
#     print('良')
# elif 90 > fenshu >= 80:
#     print('好')
# elif fenshu >= 90:
#     print('优秀')
# else:
#     print('你要努力啊！')
# words = ['石头','剪刀','布']
# yonghu = input('猜拳：')
# if yonghu == words[0] or yonghu == words[1] or yonghu == words[2]:
#     print (words)
# import random
# www = ['石头','剪刀','布']
# words = random.choice (['石头','剪刀','布'])
# yonghu = input('请猜拳：')
# if words == yonghu :
#     print('电脑：',words)
#     print('用户',yonghu)
#     print ('平手')
# elif yonghu == www[0] and words ==www[1]:
#     print('电脑：',www[1])
#     print('用户：',www[0])
#     print ('你赢了')
# elif yonghu == www[1] and words ==www[2]:
#     print('电脑：',www[2])
#     print('用户：',www[1])
#     print ('你赢了')
# elif yonghu == www[2] and words ==www[0]:
#     print('电脑：',www[0])
#     print('用户：',www[2])
#     print ('你赢了')
# elif yonghu == www[2] and words ==www[1]:
#     print('电脑：',www[1])
#     print('用户：',www[2])
#     print ('你输了')
# elif yonghu == www[0] and words ==www[2]:
#     print('电脑：',www[2])
#     print('用户：',www[0])
#     print ('你输了')
# elif yonghu == www[1] and words ==www[0]:
#     print('电脑：',www[0])
#     print('用户：',www[1])
#     print ('你输了')
# else:
#     print('电脑：',words)
#     print('用户',yonghu)
#     print('你输了')
# import random
# www = [['石头','剪刀'],['布','石头'],['剪刀','布']]
# words = random.choice (['石头','剪刀','布'])
# yonghu = input('请猜拳(石头/剪刀/布)：')
# print('你的出拳：',yonghu,'电脑的出拳：',words)
# if yonghu == words :
#     print ('平局！！！')
# elif [yonghu,words] in www:
#     print('你赢了！！！！！')
# else:
#     print('你输了！！！！！！！！！！！！！！！！！！')
# import random
# www = [['石头','剪刀'],['布','石头'],['剪刀','布']]
# words = random.choice (['石头','剪刀','布'])
# pooo = """(0) 石头
# (1) 剪刀
# (2) 布
# 请出拳(0/1/2)"""
# yonghu = int(input(pooo))
# print('你的出拳：',yonghu,'电脑的出拳：',words)
# if yonghu == words :
#     print ('\033[32;1m平局！！！\033[0m')
# elif [yonghu,words] in www:
#     print('\033[35;1m你赢了！！！！！\033[0m')
# else:
#     print('\033[30;1m你输了！！！！！！！！！！！！！！！！！！\033[0m')
# sum100=0
# counter = 1
# while counter <=100:
#     sum100 += counter
#     counter += 1
# print(sum100)
# import random
# number=random.randint(1,100)
# running = True
# #answer = int(input('猜数（1-100）:'))
# while running:
#     answer = int(input('猜数（1-100）:'))
#     if answer > number:
#         print('猜大了')
#     elif answer < number:
#         print('猜小了')
#     else:
#         print('猜对了')
#         running=False
# import random
# number = random.randint(1,100)
# while  True:
#     answer = int(input('猜数（1-100）：'))
#     if answer > number:
#         print('猜大了')
#     elif answer < number:
#         print('猜小了')
#     else:
#         print('猜对了')
#         break
# sum100 = 0
# counter = 0
# while counter < 100:
#     counter +=1
#     if counter % 2:  #结果只有0或1 0为False 1为True
#         continue
#     sum100 += counter
# print(sum100)

# sum111 = 0
# counter = 2
# while counter < 100:
#     counter+= 2
#     sum111 += counter
# print(sum111)
# import random
# number = random.randint(1,100)
# tries = 0
# while tries < 5 :
#     acccc = int(input('请输入数字：'))
#     if acccc < number:
#         print('\033[32;1m猜小了!\033[0m')
#     elif acccc > number:
#         print('\033[32;1m猜大了！\033[0m')
#     else:
#         print('\033[32;1m猜对了！!!!!\033[0m')
#         break
#     tries += 1
# else:
#     print('正确的数字是： ',number)

# user = ('石头','剪刀','布')
# import random
# choice = ['石头','剪刀','布']
#pc = random.choice(['石头','剪刀','布'])
# ww = [['石头','剪刀'],['剪刀','布'],['布','石头']]
# pooo = """(0) 石头
# (1) 剪刀
# (2) 布
# 请猜拳(0/1/2)"""
#index = int(input(pooo))
#user2=choice[index]
#print ('电脑猜拳：',pc,'你的猜拳：',user2)
# import random
# choice = ['石头','剪刀','布']
# ww = [['石头','剪刀'],['剪刀','布'],['布','石头']]
# pooo = """(0) 石头
# (1) 剪刀
# (2) 布
# 请猜拳(0/1/2)"""
# a = 0
# while a < 3:
#     a += 1
#     pc = random.choice(['石头', '剪刀', '布'])
#     index = int(input(pooo))
#     user2 = choice[index]
# #    print('电脑猜拳：', pc, '你的猜拳：', user2)
#     while user2 == pc :
#         #print ('\033[31;1m平局！\033[0m')
#         break
#     if  [user2,pc] in ww :
#         print('电脑猜拳：', pc, '你的猜拳：', user2)
#         print ('\033[31;1m正确\033[0m')
#         continue
#     else:
#         print('电脑猜拳：', pc, '你的猜拳：', user2)
#         print ('\033[31;1m错误\033[0m')
    # while b == 1:
    #     print('\033[31;1mYOUWIN!!!!\033[0m')
    # else:
    #     print('\033[31;1mYOULOSE!!!!\033[0m')
# import random
# choice = ['石头','剪刀','布']
# ww = [['石头','剪刀'],['剪刀','布'],['布','石头']]
# pooo = """(0) 石头
# (1) 剪刀
# (2) 布
# 请猜拳(0/1/2)"""
# a = 0
# b = 0
# c = 0
# while a < 3:
#     a += 1
#     pc = random.choice(['石头', '剪刀', '布'])
#     index = int(input(pooo))
#     user2 = choice[index]
#     while user2 == pc:
#         break
#     if  [user2,pc] in ww :
#         print('电脑猜拳：', pc, '你的猜拳：', user2)
#         print ('\033[31;1m正确\033[0m')
#         b += 1
#         continue
#     else:
#         print('电脑猜拳：', pc, '你的猜拳：', user2)
#         print ('\033[31;1m错误\033[0m')
#         c += 1
#         continue
# while b == 1:
#     print('\033[31;1mYOUWIN!!!!\033[0m')
#     break
# while c == 1:
#     print('\033[31;1mYOULOSE!!!!\033[0m')
#     break
# import random
# choice = ['石头','剪刀','布']
# ww = [['石头','剪刀'],['剪刀','布'],['布','石头']]
# pooo = """(0) 石头
# (1) 剪刀
# (2) 布
# 请猜拳(0/1/2)"""
# a = 0
# b = 0
# c = 0
# while a < 3:
#     a += 1
#     pc = random.choice(['石头', '剪刀', '布'])
#     index = int(input(pooo))
#     user2 = choice[index]
#     while user2 == pc:
#         break
#     if  [user2,pc] in ww :
#         print('电脑猜拳：', pc, '你的猜拳：', user2)
#         print ('\033[31;1m正确\033[0m')
#         b += 1
#         continue
#     while b == 2:
#         print('\033[31;1mYOUWIN!!!!\033[0m')
#         break
#     else:
#         print('电脑猜拳：', pc, '你的猜拳：', user2)
#         print ('\033[31;1m错误\033[0m')
#         c += 1
#         continue
#     while c == 2:
#         print('\033[31;1mYOULOSE!!!!\033[0m')
#         break
# while b == 2:
#     print('\033[31;1mYOUWIN!!!!\033[0m')
#     break
# while c == 2:
#     print('\033[31;1mYOULOSE!!!!\033[0m')
#     break
# import random
# choice = ['石头','剪刀','布']
# ww = [['石头','剪刀'],['剪刀','布'],['布','石头']]
# pooo = """(0) 石头
# (1) 剪刀
# (2) 布
# 请猜拳(0/1/2)"""
# a = 0
# b = 0
# c = 0
# while a < 3:
#     a += 1
#     pc = random.choice(['石头', '剪刀', '布'])
#     index = int(input(pooo))
#     user2 = choice[index]
#     while user2 == pc:
#         break
#     if  [user2,pc] in ww :
#         print('电脑猜拳：', pc, '你的猜拳：', user2)
#         print ('\033[31;1m正确\033[0m')
#         b += 1
#         continue
#     # if b>=2:
#     #     break
#     # while b == 2:
#     #     print('\033[31;1mYOUWIN!!!!\033[0m')
#     #     break
#     else:
#         print('电脑猜拳：', pc, '你的猜拳：', user2)
#         print ('\033[31;1m错误\033[0m')
#         c += 1
#         continue
#     # if c>=2:
#     #     break
# while b >= 2:
#     print('\033[31;1mYOUWIN!!!!\033[0m')
#     break
# while c >= 2:
#     print('\033[31;1mYOULOSE!!!!\033[0m')
#     break
# import random
# choice = ['石头','剪刀','布']
# ww = [['石头','剪刀'],['剪刀','布'],['布','石头']]
# pooo = """(0) 石头
# (1) 剪刀
# (2) 布
# 请猜拳(0/1/2)"""
# a = 0
# b = 0
# c = 0
# while a < 3:
#     a += 1
#     pc = random.choice(['石头', '剪刀', '布'])
#     index = int(input(pooo))
#     user2 = choice[index]
#     while user2 == pc:
#         break
#     if  [user2,pc] in ww :
#         print('电脑猜拳：', pc, '你的猜拳：', user2)
#         print ('\033[31;1m正确\033[0m')
#         b += 1
#         continue
#     else:
#         print('电脑猜拳：', pc, '你的猜拳：', user2)
#         print ('\033[31;1m错误\033[0m')
#         c += 1
#         continue
# # while b >= 2:
# #     print('\033[31;1mYOUWIN!!!!\033[0m')
# #     break
# # while c >= 2:
# #     print('\033[31;1mYOULOSE!!!!\033[0m')
# #     break
# import random
# www = ['石头','剪刀','布']
# words = random.choice (['石头','剪刀','布'])
# yonghu = input('请猜拳：')
# if words == yonghu :
#     print('电脑：',words)
#     print('用户',yonghu)
#     print ('平手')
# elif yonghu == www[0] and words ==www[1]:
#     print('电脑：',www[1])
#     print('用户：',www[0])
#     print ('你赢了')
# elif yonghu == www[1] and words ==www[2]:
#     print('电脑：',www[2])
#     print('用户：',www[1])
#     print ('你赢了')
# elif yonghu == www[2] and words ==www[0]:
#     print('电脑：',www[0])
#     print('用户：',www[2])
#     print ('你赢了')
# elif yonghu == www[2] and words ==www[1]:
#     print('电脑：',www[1])
#     print('用户：',www[2])
#     print ('你输了')
# elif yonghu == www[0] and words ==www[2]:
#     print('电脑：',www[2])
#     print('用户：',www[0])
#     print ('你输了')
# elif yonghu == www[1] and words ==www[0]:
#     print('电脑：',www[0])
#     print('用户：',www[1])
#     print ('你输了')
# else:
#     print('电脑：',words)
#     print('用户',yonghu)
#     print('你输了')
# import random
# choice = ['石头','剪刀','布']
# ww = [['石头','剪刀'],['剪刀','布'],['布','石头']]
# pooo = """(0) 石头
# (1) 剪刀
# (2) 布
# 请猜拳(0/1/2)"""
# a = 0
# b = 0
# c = 0
# while a < 3:
#     a += 1
#     pc = random.choice(['石头', '剪刀', '布'])
#     index = int(input(pooo))
#     user2 = choice[index]
#     while user2 == pc:
#         break
#     if  [user2,pc] in ww :
#         print('电脑猜拳：', pc, '你的猜拳：', user2)
#         print ('\033[31;1m正确\033[0m')
#         b += 1
#         continue
#     else:
#         print('电脑猜拳：', pc, '你的猜拳：', user2)
#         print ('\033[31;1m错误\033[0m')
#         c += 1
#         continue
# while b == 1:
#     print('\033[31;1mYOUWIN!!!!\033[0m')
#     break
# while c == 1:
#     print('\033[31;1mYOULOSE!!!!\033[0m')
#     break
# import random
# all_choice=['石头','剪刀','布']
# win_list=[['石头','剪刀'],['剪刀','布'],['布','石头']]
# po="""(0) 石头
# (1) 剪刀
# (2) 布
# 请输入(0/1/2)"""
import random
all_choice=['石头','剪刀','布']
win_list=[['石头','剪刀'],['剪刀','布'],['布','石头']]
po="""(0) 石头
(1) 剪刀
(2) 布
请输入(0/1/2)"""
c=0
p=0
while c <2 and p<2:
    pc=random.choice(all_choice)
    ind=int(input(po))
    u = all_choice[ind]
    print('ni:  %s,pc: %s'%(u,pc))
    if u == pc:
        print ('平局！！！')
    elif [u ,pc]in win_list:
        p+=1
        print('你赢了！！！！！')
    else:
        c+=1
        print('你输了！！！！！！！！！！！！！！！！！！')

