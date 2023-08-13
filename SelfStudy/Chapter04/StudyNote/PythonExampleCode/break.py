sum = 0

for i in range(1,101):
    sum += i
    if sum > 1000:
        break  # sum が 1000 より大きい時、終了する。
    print(sum)