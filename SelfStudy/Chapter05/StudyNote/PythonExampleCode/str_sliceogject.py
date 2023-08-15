title = 'あいうえおかきくけこ'

print(slice(-5, None, -1).indices(len(title)))

# slice(-5, None, -1) = [-5::-1]
# 5 から -1 (先頭) まで前方向 (-1) にスライスするという意味