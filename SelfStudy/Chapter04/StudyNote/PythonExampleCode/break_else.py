data = ['A','B','x','D','E']

for i in data:
    if i == 'x':  # 要素が「x」である時、ループを終了する
        break
    print(i)
else:
    print('終了')