import random
r = random.randint(1, 10)

while True:
    num = input('請猜一個1~100的數字： ')
    if num.isdigit():
        num = int(num)
        if num == r:
            print('答對了！')
            break
        elif num > r:
            print('比答案大')
        elif num < r:
            print('比答案小')
    else:
        print('請輸入數字')
