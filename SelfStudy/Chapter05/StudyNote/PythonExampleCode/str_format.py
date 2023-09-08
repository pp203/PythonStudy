# 1. 基本例
print('{}は{}、{}歳です。'.format('サクラ', '女の子', 2))

# 2. 番号付けをし、それぞれ x 番目の引数が埋め込まれるようにする
print('{0}は{2}歳、{1}です。'.format('サクラ', '女の子', 2))

# 3. 置き換えフィールドに名前付けする
print('{name}は{age}歳、{sex}です。'.format(
    name = 'サクラ', sex = '女の子', age = 2
))


name = 'サクラ'
sex = '女の子'
age = 2

# 4. format メソッドの簡易構文 (= フォーマット文字列)
print(f'{name}は{sex}、{age}歳です。')

# 5. {xx=} で評価前の式そのものを合わせて出力する
print(f'{name=}は{sex=}、{age=}歳です。')