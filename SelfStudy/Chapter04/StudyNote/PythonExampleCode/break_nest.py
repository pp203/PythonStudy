for i in range(1,10):
    for j in range(1,10):
        result1 = i * j
        if result1 > 30:  # 50 より大きい場合はループを終了
            break
        print(result1, end = " ")
    print()


for x in range(1,10):
    for y in range(1,10):
        result2 = x * y
        if result2 > 30:
            break  # 次の break に行く
        print(result2, end = " ")  # 50 未満の値はここにくる
    else:
        print()  # 50 未満の値は改行されて x ループに戻る
        continue
    print()
    break        


flag = False

for a in range(1,10):
    for b in range(1,10):
        result3 = a * b
        if result3 > 30:
            flag = True  # break する時 flag も True にする
            break
        print(result3, end = " ")
    print()
    if flag:  # flag が True の時、外側のループも終了
        break