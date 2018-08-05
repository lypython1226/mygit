import random
import math

def save():
    str_num =''
    for i in range(4):
        num = random.randrange(97,123)
        str_s = chr(num)
        str_num = str_num + str_s
    for i in range(8):
        num = random.randrange(0,10)
        str_num += str(num)
    return  str_num
source = 0
total = 0
while 1:
    num = input("请输入一个三位数的数字(输入-1结束):")
    random_num = random.randrange(100,1000)
    if num == '-1':
        break
    if num.isdigit() and 100 <= int(num) <= 999:
        num = int(num)
        random_num = int(random_num)
        total += 1
        print('你现在输入的次数为%d：'%total)
        if num > random_num:
            bai = num // 100
            shi = num%100 // 10
            ge = num%10
            print("这个函数的个位是{},十位是{},百位数是{}".format(bai,shi,ge))
        if num == random_num:
            source += 100
            print('你中奖了目前分数为:',source)
        if num<random_num:
            for i in range(10):
                line = save()
                with open('str_num.txt','a') as f:
                    f.write(line + '\n')
    else:
        print("你他妈会不会打的,我日你哥")


