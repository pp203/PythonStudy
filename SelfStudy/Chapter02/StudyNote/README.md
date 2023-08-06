# Chapter 02. Python の基礎

## 2.1. 変数
**変数**  
処理途中のデータを維持・運搬するための箱

### 変数を加える 

variable01.py
```
test = 'seina'
print(test)
```

実行結果
```
$ python3 variable01.py 

seina
```

<ins>変数を指定せず実行するとエラーが出力される

variable02_error.py
```
print(test)
```

実行結果
```
$ python3 variable02_error.py 

Traceback (most recent call last):
  File "/Users/seinay/VSCode/GitHub/PythonStudy/SelfStudy/Chapter02/variable02_error.py", line 1, in <module>
    print(test)
          ^^^^
NameError: name 'test' is not defined
```

### 変数を破棄する

del.py
```
test = 'seina'
print(test)

del test

print(test)
```

実行結果
```
$ python3 del.py

seina

Traceback (most recent call last):
  File "/Users/seinay/VSCode/GitHub/PythonStudy/SelfStudy/Chapter02/variable03.py", line 6, in <module>
    print(test)
          ^^^^
NameError: name 'test' is not defined　　# del で変数を削除して print() したからエラーが出力された。
```

### 代入  
変数に値を格納すること
```
msg = 'こんにちは'  # 右の値を左の変数に格納する
```

### 識別子
命名規則のこと
* Unicode 文字を利用できること (ただし、'_' 以外の記号、句読点、絵文字などは不可)
* 1 文字目は "数字以外" であること
* アルファベットの大文字・小文字は区別されること
* 予約後ではないこと
* 文字数の制限はないこと

### 予約語
* Python であらかじめ意味が決められた単語のこと
* and, as, assert, async, await, break, class, continue, def, del, elif, else, except, False, finally, for....

### 定数
入れ物と中身がセットで後から中身が変更できないもののこと

**定数なし**  

const01.py
```
price = 100
print(price * 1.1)
```

実行結果
```
$ python3 const01.py 

110.00000000000001
```

**定数あり**  

const02.py
```
price = 100
tax = 1.1   # 定数化する
print(prince * tax)
```

実行結果
```
$ python3 const02.py

110.00000000000001
```

## 2.2. データ型
* データの種類のこと
* 文字列型 = "abc"
* 数値型 = "123"
* 論理型 = "True/False"

### 静的型付け言語 vs. 動的型付け
* 静的型付け言語 = (e.g.) 文字列を格納するために用いられた変数に数値をセットできない。変数とデータ型とは常にワンセット。
* 動的型付け言語 = (e.g.) 最後に文字列を格納した変数にあとから数値をセットすることが可能。変数の方が中身に応じて自動的に形を変えてくれる。Python では動的型付け。

例  

overwrite.py
```
data = 'Python Code'
data = 123
print(data)
```

実行結果
```
$ python3 overwrite.py 

123
```

### 組み込み型  
Python のインタプリターに標準で組み込まれているデータ型のこと
* 数値
int = 整数型
float = 浮動小数点型
complex = 複素数型
* データ
str = 文字列型
bytes = バイナリデータ
* コンテナー
list = 順序を持つリスト
tuple = 順序を持つリスト (変更不可)
dict = キー/値の辞書
set = 順序を持たない値の集合
* その他
bool = 論理型 (True/False)
NoneType = 値がない

### リテラル  
変数に格納できる値そのもの
* mutable = 変更可能
* immutable = 変更不可
* iterable = 反復可能
* sequence = 順序を持つ (インデックスでのアクセスが可)
* container = 配下に複数の値を格納可能

### 組み込み型 - 論理型 (bool)
「正しい」か「間違い」かの状態しか持たない組み込み型

False とみなすとき
* 空欄 (None)
* 数値のゼロ (0, 0.0, 0j...etc) 
* 空文字列、空のリスト (()、[]、set()、range(0)...etc)

### 組み込み型 - 整数型 (int)
* 10 進数リテラル = 一般的な整数表現。(整数 (100)、負数 (-1)、ゼロ (0))
* 16 進数リテラル = 0-9 + a-f (A-F) で 10-15 の値で表す。
* 8 進数リテラル = 0-9 + a-f (A-F) で 0-7 の値で表す。
* 2 進数リテラル = 0-9 + a-f (A-F) で 0-1 の値で表す。

### 組み込み型 - 浮動小数点型 (float)
* 一般的な小数点だけではなく、指数表現も含まれる。
* <仮数部>e<符号><指数部>
* 例: 1.4142e10 = 1.4142x10(10 乗) = 14142000000.0

### 数値セパレーター  
数値リテラルの中に桁区切り文字 '_' を入れれる


value_separater01.py
```
value = 1_234_567
pi = 3.141_-592_653_59
num = 0.123_456e10

print(value, pi, num)
```

実行結果
```
$ python3 value_separater01.py

1234567 3.14159265359 1234560000.0
```

一般的には 3 桁で区切るが、以下のような数値リテラルでも可能  

value_separater02.py
```
value01 = 12_34_56 # 2 桁ごとでも区切ることができる
value02 = 1_23_456_7890 # 異なる桁で区切ることもできる
```

実行結果
```
$ python3 value_separater02.py

123456 1234567890
```

2、8、16 進数でも可能  

value_separater03.py
```
a = 0b01_01_01 # 10 進数で 21
b = 0xf4_240   # 10 進数で 1000000
c = 0o23_420   # 10 進数で 10000

print(a, b, c)
```

実行結果
```
$ python3 value_separater03.py 

21 1000000 10000
```

<ins>以下の場合はエラーが出力される  

value_separater_error.py
```
a = _123_456  # 先頭に '_'
b = 123_456_  # 末尾に '_'
c = 1._234    # 小数点扱いになる
d = 0_x99     # 数値プレフィックスの途中

print(a, b, c, d)
```

実行結果
```
$ python3 value_separater_error.py 

  File "/Users/seinay/VSCode/GitHub/PythonStudy/SelfStudy/Chapter02/value_separater_error.py", line 2
    b = 123_456_  # 末尾に '_'
               ^
SyntaxError: invalid decimal literal  # 最初のエラーが表示される
```

### 組み込み型 - 複素数型 (complex)
数学上の概念みたいな  
* j = 虚数単位
* 虚数単位 = -1 の平方根 
2 乗したらその値になる数
例: 3 の 2 乗 = 9
数学では 'i' だが、Python では 'j' を使う

complex01.py
```
a = 1.0 + 2.0j
b = 1.0j

print(a, b)
```

実行結果
```
$ python3 complex01.py 

(1+2j) 1j
```

四則演算することも可能

complex02.py
```
c1 = 1 + 2j
c2 = 3 + 4j

print(c1 + c2)
print(c1 * c2)
```

実行結果
```
$ python3 complex02.py 

(4+6j)
(-5+10j)
```

complex 関数を使って実数値から生成することも可能

complex03.py
```
a = complex(1,5)

print(a)
```

実行結果
```
$ python3 complex03.py 

(1+5j)
```

real/imag 属性を使って実部/虚部を取得することも可能  

complex04.py
```
a = complex(1,5)

print(a.real)
print(a.imag)
```

実行結果
```
$ python3 complex04.py 

1.0
5.0
```

### 組み込み型 - 文字列型 (str)  
文字列全体をシングルクォート '' / ダブルクォート "" でくくる

文字列に「"」/「'」そのものを含めることはできない。以下の場合はエラーが出力される。  

str_error01.py
```
print("You are "GREAT" teacher!")
```

実行結果
```
$ python3 str_error01.py 

  File "/Users/seinay/VSCode/GitHub/PythonStudy/SelfStudy/Chapter02/str_error01.py", line 1
    print("You are "GREAT" teacher!")
          ^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?  
```

(1) 文字列に ""/'' そのものを含める時には、文字列に含まれないほうのクォートでくくる必要がある  

str01.py
```
print("You are 'GREATE' teacher")
print('You are "GREATE" teacher')
```

実行結果
```
$ python3 str01.py

You are 'GREATE' teacher
You are "GREATE" teacher
```

(2) クォート文字をエスケープ処理する  

### エスケープシーケンス
* 「\' | ただの「'」として読まれる。文字列の開始/終了の扱いにはならない。
* 改行・タブ文字などの特殊な意味を持つ文字を表すために必要  

| エスケープシーケンス | 概要 |
| --- | --- |
| \\\ | バックスラッシュ
| \\' | シングルクォート
| \\" | ダブルクォート
| \\b | バックスペース
| \\f | フォームフィード (改ページ)
| \\r | 復帰 (キャリッジリターン)
| \\Enter | バックスラッシュと改行文字を無視する
| \\t | 水平タブ
| \\v | 垂直タブ
| \\XX | 8 進数の文字 XX
| \\xXX | 16 進数の文字 XX
| \\uXX | 16 bit (4 桁) の 16 進数の文字 XXXX
| \\UXXXXXXXX | 32 bit (8 桁) の 16 進数の文字 XXXXXXXX

str02.py
```
print("He\s 'GREATE' teacher")
```

実行結果
```
$ python3 str02.py

He\s 'GREATE' teacher
```

str03.py
```
print('こんにちは、\n赤ちゃん')
```

実行結果
```
$ python3 str03.py 

こんにちは、
赤ちゃん
```

<ins>以下だと改行で文の終わりとみなされるので、エラーが出力される。

str_error02.py
```
print('こんにちは
赤ちゃん')
```

実行結果
```
$ python3 str_error02.py 

  File "/Users/seinay/VSCode/GitHub/PythonStudy/SelfStudy/Chapter02/str_error02.py", line 1
    print('こんにちは
          ^
SyntaxError: unterminated string literal (detected at line 1)
```

以下だと長い文字列を折り返すことができる

str04.py
```
print('こんにちは、\
    赤ちゃん')
```

実行結果
```
$ python3 str04.py 

こんにちは、    赤ちゃん
```

「\」を表示する時は「\\\」を使用する

str05.py
```
data = 'エスケープシーケンスを表すのは \\'

# data = 'エスケースシーケンスを表すのは \' だと表示されない

print(data)
```

実行結果
```
$ python3 str05.py

エスケープシーケンスを表すのは \
```

### 特殊な文字を入れる表現  

(1) 複数行文字列  
'''...''' / """...""" で複数行の文字列をそのまま表現することが可能  
* この場合、「\n」が不要となる
* これを使えば何行でもそのまま表現することが可能
* 文字列の開始/終了は「'''」または「"""」なので、「'」や「""」を中に含めることも可能


special_str.py
```
print('''こんにちは、
赤ちゃん''')
```

実行結果
```
$ python3 special_str.py 

こんにちは、
赤ちゃん
```

補足: 複数の文字列を続けて書くと連結して 1 つの文字列になる

str06.py
```
test = (            # 丸カッコの中では自由に改行ができる
    'こんにちは、'  
    '赤ちゃん'       # 複数の文字列は自動で連結する
)

print(test)
```

実行結果
```
$ python3 str06.py 

こんにちは、赤ちゃん
```


(2) raw 文字列  
* 「\xx」をエスケープシーケンスとみなさずに表記のまま解釈できる
* 先頭に「r」または「R」をつける

raw01.py
```
print('C:\\Windows\\AppPatch\\en-US')

print(r'C:\Windows\AppPatch\en-US')
```

実行結果
```
$ python3 raw01.py

C:\Windows\AppPatch\en-US
C:\Windows\AppPatch\en-US
```

raw02.py
```
print(r'You are "GREAT" teacher')

print(r"""You are "GREAT" teacher""")
```

実行結果
```
$ python3 raw02.py 

You are "GREAT" teacher
You are "GREAT" teacher
```

(3) フォーマット文字列
先頭に「f」または「F」をつけることで文字列の {...} の形式で変数を埋め込むことができる

format01.py
```
print(f'こんにちは、{name} さん')
```

実行結果
```
$ python3 format01.py

こんにちは、seina さん
```

format02.py
```
name = 'seina'

print(fr''' おはよう、{name} さん
パスは「C:\Windows\AppPatch\en-US」です ''')
```

実行結果
```
$ python3 format02.py 

おはよう、seina さん
パスは「C:\Windows\AppPatch\en-US」です 
```

### リスト
* 複数の値を収めることができる
* 仕切りのある入れ物的な
* 要素 = 仕切りで区切られたスペース
* 0 から数える
* [] でリストは作成する
  * [] でくくられた部分は **インデックス番号** と呼ばれる  

list_basic.py
```
data = ['Toronto', 'Tokyo', 'Seattle', 'London']

print(data[2])  # 0 から数えるので Seattle が表示される
```

実行結果
```
$ python3 list_basic.py 

Seattle
```

リストの個々の要素に当たらな値を設定することも可能

list01.py
```
data = ['Toronto', 'Tokyo', 'Seattle', 'London']
data[2] = 'Dubai'

print(data[2])  
```

実行結果
```
$ python3 list01.py 

Dubai
```

<ins>ただし、要素を 追加することはできない

list_error.py
```
data = ['Toronto', 'Tokyo', 'Seattle', 'London']
data[4] = 'Dubai'

print(data[4])
```

実行結果
```
$ python3 list_error.py 

Traceback (most recent call last):
  File "/Users/seinay/VSCode/GitHub/PythonStudy/list_error.py", line 2, in <module>
    data[4] = 'Dubai'
    ~~~~^^^
IndexError: list assignment index out of range
```

リストを 1 行で表す時には最後に ',' は基本的には必要ない。

list02.py
```
data = ['Toronto', 'Tokyo', 'Seattle', 'London',]  # この場合は、あってもなくても問題ない

print(data[1])
```

実行結果
```
$ python3 list02.py 

Tokyo
```

リストに複数行で表す時には最後に ',' つけた方が見やすくなる

list03.py
```
data = ['Toronto', 
        'Tokyo', 
        'Seattle', 
        'London',
]  

print(data[1])
```

実行結果
```
$ python3 list03.py 

Tokyo
```

### 入れ子のリスト
* リストには数値や文字列だけではなく、リストそのものを格納することが可能
* 1 次元リスト = インデックスが 1 つだけのリスト
* 2 次元リスト/多次元リスト = リストのリスト

list04.py
```
data = [
    ['a', 'b', 'c'],
    ['A', 'B', 'C'],
    ['あ','い','う'],
]

print(data[1][0])  ## 最初のリスト [1] の中から次のリスト [0] 番目を表示する
```

実行結果
```
$ python3 list04.py 

A
```

3 x 3 x 3 の 3 次元リストの作成も可能

list05.py
```
data = [
    [
        ['a','b','c'],
        ['A','B','B'],
    ],
    [
        ['aa','bb','cc'],
        ['AA','BB','CC'],
    ],
    [
        ['aaa','bbb','ccc'],
        ['AAA','BBB','CCC'],
    ]
]

print(data[2][0][1])
```

実行結果
```
$ python list05.py 

bbb
```

**ジャグ配列**  
行によって異なるリストのこと

list06.py
```
data = [
    [
        ['a','b','c'],
        ['A','B','B'],
    ],
    [
        ['aa','bb','cc','dd'],
        ['AA','BB','CC'],
    ],
    [
        ['aaa','bbb','ccc','ddd','eee'],
        ['AAA','BBB','CCC','DDD'],
    ]
]

print(data[2][0][4])
```

実行結果
```
$ python3 list06.py 

eee
```

