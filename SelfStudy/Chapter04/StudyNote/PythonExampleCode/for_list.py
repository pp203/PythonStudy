data1 = [15,20,25,30]
data2 = [i * 2 for i in data1]

print(data2)


data3 = [15,20,25,30]
data4 = []

for i in data3:
    data4.append(i * 2)  # append = リストに要素を追加する命令  

print(data4)


data5 = [str(i) for i in data4]  # リストの数値を文字列に変更する
print(data5)