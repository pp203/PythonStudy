【 変数 】
処理途中のデータを維持・運搬するための箱

## 変数を加える
test = 'seina'
print(test)

## 変数を破棄する
del test
print(test) ## NameError: name 'test' is not defined

【 代入 】
変数に値を格納すること
```
msg = 'こんにちは'  # 右の値を左の変数に格納する
```

【 識別子 】
命名規則のこと
・　Unicode 文字を利用できること (ただし、'_' 以外の記号、句読点、絵文字などは不可)
・　1 文字目は "数字以外" であること
・　アルファベットの大文字・小文字は区別されること
・　予約後ではないこと
・　文字数の制限はないこと

【 予約語 】
・　Python であらかじめ意味が決められた単語のこと
・　and, as, assert, async, await, break, class, continue, def, del, elif, else, except, False, finally, for....

【 定数 】
入れ物と中身がセットで後から中身が変更できないもののこと

## 定数なし
price = 100
print(price * 1.1)

## 定数あり
price = 100
tax = 1.1   # 定数化する
print(prince * tax)

【 データ型 】
・　データの種類のこと
・　文字列型 = "abc"
・　数値型 = "123"
・　論理型 = "True/False"

【 静的型付け言語 vs. 動的型付け 】
・　静的型付け言語 = (e.g.) 文字列を格納するために用いられた変数に数値をセットできない。変数とデータ型とは常にワンセット。
・　動的型付け言語 = (e.g.) 最後に文字列を格納した変数にあとから数値をセットすることが可能。変数の方が中身に応じて自動的に形を変えてくれる。Python では動的型付け。

## 例
data = 'Python Code'
data = 123

【 組み込み型 】
Python のインタプリターに標準で組み込まれているデータ型のこと
・　数値
    ・　int = 整数型
    ・　float = 浮動小数点型
    ・　complex = 複素数型
・　データ
    ・　str = 文字列型
    ・　bytes = バイナリデータ
・　コンテナー
    ・　list = 順序を持つリスト
    ・　tuple = 順序を持つリスト (変更不可)
    ・　dict = キー/値の辞書
    ・　set = 順序を持たない値の集合
・　その他
    ・　bool = 論理型 (True/False)
    ・　NoneType = 値がない

【 リテラル 】
変数に格納できる値そのもの
・　mutable = 変更可能
・　immutable = 変更不可
・　iterable = 反復可能
・　sequence = 順序を持つ (インデックスでのアクセスが可)
・　container = 配下に複数の値を格納可能

【 埋め込み型 - 論理型 (bool) 】
「正しい」か「間違い」かの状態しか持たない埋め込み型

False とみなすとき
・　空欄 (None)
・　数値のゼロ (0, 0.0, 0j...etc) 
・　空文字列、空のリスト (()、[]、set()、range(0)...etc)

【 埋め込み型 - 整数型 (int) 】
・　10 進数リテラル = 一般的な整数表現。(整数 (100)、負数 (-1)、ゼロ (0))
・　16 進数リテラル = 0-9 + a-f (A-F) で 10-15 の値で表す。
・　8 進数リテラル = 0-9 + a-f (A-F) で 0-7 の値で表す。
・　2 進数リテラル = 0-9 + a-f (A-F) で 0-1 の値で表す。

【 埋め込み型 - 浮動小数点型 (float) 】
・　一般的な小数点だけではなく、指数表現も含まれる。
・　<仮数部>e<符号><指数部>
・　例: 1.4142e10 = 1.4142x10(10 乗) = 14142000000.0

【 リテラル 】