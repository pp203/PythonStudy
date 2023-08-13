while True:
    try:
        num = input('数値を入力')
        print('1.5 倍にすると...', float(num) * 1.5)
    except ValueError:
        print('入力エラー')
    else:
        break