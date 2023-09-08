data = 'こんにちは'

## エンコードした場合
encoded = data.encode('sjis')
print(encoded)


## 上記をデコードした場合
print(encoded.decode('sjis'))


## エンコード時とは異なる文字エンコードでデコードした場合
print(encoded.decode('euc-jp','replace'))