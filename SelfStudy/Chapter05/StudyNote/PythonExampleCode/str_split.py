msg1 = 'ねこ いぬ たぬき'
msg2 = 'さくら|もも|うめ|ききょう'

# 引数 sep を省略したバターン
print(msg1.split()) 

# 任意の区切り文字として文字列を分割
print(msg2.split('|')) 
print(msg2.rsplit('|'))

# 引数 maxsplit を指定した場合
# split/rsplit メソッドは指定された分割数を上限に、文字列を分割
print(msg2.split('|', 2))
print(msg2.rsplit('|', 2))