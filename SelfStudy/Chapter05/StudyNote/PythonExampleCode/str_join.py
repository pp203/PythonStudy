data1 = ['いぬ', 'ねこ', 'たぬき']
print(','.join(data1))

data2 = [10, 103, 18]
# print('\t'.join(data2))
# TypeError: sequence item 0: expected str instance, int found
# 数値方リストを json メソッドでそのまま連結することはできない

print('\t'.join([str(i) for i in data2]))