try:
    num = input('数字を入力してください')
    print('2 倍にすると...', float(num) * 2)
except ValueError as ex:
    print('エラー発生：', ex)