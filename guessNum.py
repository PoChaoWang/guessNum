import random
start = input('請決定一個隨機數字的開始值： ')
if start.isdigit():
    start = int(start)
    end = input('請決定一個隨機數字的結束值： ')
    if end.isdigit():
        end = int(end)
        r = random.randint(start, end)
        count = 0
        while True:
            count += 1
            num = input('請猜一個其中的數字：')
            if num.isdigit():
                num = int(num)
                if num == r:
                    print('答對了！')
                    print('這是你猜的第', count, '次')
                    break
                elif num > r:
                    print('比答案大')
                elif num < r:
                    print('比答案小')
                print('這是你猜的第', count, '次')
            else:
                print('請輸入數字')
    else:
        print('請輸入整數的數字')
else:
    print('請輸入整數的數字')
