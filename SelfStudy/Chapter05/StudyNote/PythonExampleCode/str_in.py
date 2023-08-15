msg = 'WINGプロジェクト'

# in 演算子例
print('プロ' in msg)
print('プロ' not in msg)

# startswith/endswith メソッド例
print(msg.startswith('WINGS'))
print(msg.endswith('WINGS'))
print(not msg.startswith('WINGS'))
print(msg.startswith('WINGS', 1))

# in 演算子で部分検索
print('プロ' in msg[6:])

# in 演算子で大文字/小文字が揃っていない例
print('wings' in msg)
print('wings' in msg.casefold())