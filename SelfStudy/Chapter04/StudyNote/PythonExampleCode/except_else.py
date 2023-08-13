while True:
    try:
        num = input('数字を入力')
        print('2 倍すると...', float(num) * 2)
    except ValueError:
        print('入力値エラー')
    else:
        break