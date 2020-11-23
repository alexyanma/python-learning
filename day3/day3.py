"""
Day 3
"""
# if 循环
# age = 20
# if 18 < age <= 22:
#     print('我是一个大学生')
# print('开始为自己的梦想拼搏')

#if... elif ... else 循环
# score = 95.00
# if 90.00 <= score <= 100:
#     print('优等生')
# elif 60 <= score < 90.00:
#     print('一般学生')
# else:
#     print('坏学生')

# 断言
# age = 16
# assert 18 <= age < 50, 'age 变量处理结果错误'
# print('满足年龄条件， 你的年龄是 %d' % age)


# while 循环 1 ～ 100 的数字累加
# sum = 0
# num = 1
# while num <= 100:   # 设定循环判断
#     sum += num      # 执行数字的累加
#     num += 1        # 修改循环条件
# else:
#     print('数字累加计算结果：%d， 当前计数的值是 %d' % (sum, num))  # num的值是101， 不满足循环条件退出循环
# print('循环之外的代码, 打印累加的值 %d' % sum)

# 斐波那契数字数列， 1、1、2、3、5、8、13、21
# 实现1000以内的斐波那契数列打印
# num_1 = 0
# num_2 = 1
# while num_2 < 1000:
#     print(num_2, end='、')
#     num_1, num_2 = num_2, num_1 + num_2  # Python 特有的赋值语句， 把num_2的值赋值给num_1,
#                                          # [同时]修改num_2的值为num_1 + num_2
#     # 如果使用code
#     # num_1 = num_2
#     # num_2 = num_1 + num_2  # 在这步时， num_1的值已经被改变为当前num_2的值， 所以num_2 = num_2 ×２


# 进行两个变量之间的交换
# num_a = 10
# num_b = 5
# num_a, num_b = num_b, num_a
# print('num_a 的值是 %d' % num_a)
# print('num_b 的值是 %d' % num_b)


# for 循环
# for num in {1, 3, 5}:
#     print(num, end=', ')

# range()函数， 指定起始值
# for num in range(5, 10):   # range(max)
#     print(num, end=', ')
#
# # range()函数， 指定起始值， 和指定步长
# for num in range(5, 10, 2):   # range(max)
#     print(num, end=', ')

# 使用for 循环计算1 ～100的数字累加
# sum = 0
# for num in range(1, 101):
#     sum += num
# print('累加计算的结果是 %d' % sum)

# 使用for循环迭代一个字符串
# msg = 'alexyanma@gmail.com'
# for c in msg:
#     print(c, end=',')


# 使用for循环和编码进行一个字符串小写转大写的操作
# 编码函数ord(), 小写a的编码是97， 小写z的编码是122
# msg = 'alexyanma@gmail.com'
# for item in msg:
#     if 97 <= ord(item) <= 122:  # 如果是小写字符的编码
#         print((chr(ord(item) - 32)), end=',')    # 小写转大写编码-32
#     else:
#         print(item, end=',')    # 如果不是小写字符的编码， 直接输出


# continue 控制循环
# for num in range(1, 10):
#     if num == 3:    # 设定分支条件
#         continue    # 当满足分支条件时， 不再执行本次循环值中的下面代码， 循环没有被打断
#     print(num, end=', ')


# break 控制循环
# for num in range(1, 10):
#     if num == 3:    # 设定分支条件
#         break    # 当满足分支条件时， 打断循环， 执行跳出循环操作
#     print(num, end=', ')
# else:
#     print('跳出循环， 当前执行数字为 %d' % num)   # 当跳出循环时， else 循环语句也会一并跳出


# 简单的双层循环嵌套
# for x in range(1, 4):       # 设定x从1开始, 默认是0
#     for y in range(1, 4):   # 设定y从1开始, 默认是0
#         print('第 %d 次循环， y= %d' % (x, y))


# 打印9×9乘法表
# for x in range(1, 10):
#     for y in range(1, x+1):  # 如果终止范围不加1， range（1， 1） y=1 则不会循环， range（1， 9）也不会执行y=9
#         print('%d*%d=%d' % (x, y, x * y), end=' ')
#     print()     # 需要增加手动换行


# 打印三角形
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# 分析
# 第一行空格、空格、空格、空格、*              -- 4个空格 + 1个*
# 第二行空格、空格、空格、*、 空格、*           -- 3个空格 + (* + 空格） × 2
# 第三行空格、空格、*、 空格、*、 空格、*       -- 2个空格 +  (* + 空格） × 3
# 第四行空格、*、空格、*、空格、*、空格、*      -- 1个空格 + (* + 空格） × 4
# 第五行*、空格、*、空格、*、空格、*、空格、*    --   (* + 空格） × 5

# line = 5        # 定义总共打印的行数
# for x in range(0, line):
#     for z in range(0, line - x):    # 打印空格， x在增加的时候，它的循环输出就越小
#         print('', end=' ')
#     for y in range(0, x + 1):       # 打印*, x在增加的时候，它的循环输出就越大, 因为x开始为0，所以必须x+1， 是其循环第一次
#         print('*', end=' ')
#     print()                         # 手动换行


# 经典Python打印三角形
line = 10
for x in range(0, line):
    print(' ' * (line - x), end=' ')
    print('* ' * (x + 1))
