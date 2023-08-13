sum = 0

for i in range(1,101):
    if i % 2 != 0:  # i を 2 で割り切れない時はスキップする
        continue
    sum += i  # i を 2 で割り切れる数だけの合計値
print(sum)