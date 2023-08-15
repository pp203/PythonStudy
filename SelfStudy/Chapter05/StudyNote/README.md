# Chapter 05. 標準ライブラリ
ライブラリ：コードから自在に呼び出せる命令


## 5.1. ライブラリの分類
1. 型と関数
* 関数：あらかじめ決められた機能を持つ道具
  * 値を表示する
  * 合計値を求める
  * 型を変換する
* 型：値の種類/範囲を表す情報
  * リスト
    * 値を挿入
    * 値を排除
  * 文字列
    * 検索
    * 置換
  * 日付/時刻
    * 比較
    * 加算

2. 組み込みライブラリとモジュール
* 組み込み関数/組み込み型：Python インタプリター (本体) に組み込まれている関数/型
* モジュール：builtin でない関数/型
  * 例 1. math モジュール： 数学関連の関数/型
  * 例 2. datatime モジュール：日付/時刻関連の関数/型

---

### *5.1.1. 関数*
関数：何かしらのパラメーターを与えることにより、あらかじめ決められた処理を行い、その結果を返す仕組み
* 引数：関数への入力
* 戻り値：出力

関数によっては以下の場合がある
1. 引数も戻り値もない：決められた処理を実行するのみ
2. 引数はないが、戻り値はある：決められた処理を実行し、結果を返すのみ
3. 引数はあるが、戻り値はない：与えられた値を処理するのみ
4. 引数も戻り値もある：与えられた値を処理し、結果も返す

構文例
```py
関数名(引数,...,引数名 = 値,...)

# 引数：「値...」と「名前 = 値,...」という場合がある
# 位置引数：「値...」
# キーワード引数：「名前 = 値,...」
```

```py
print('Hello', name, 'さん', sep = '+', end = '')

# 'Hello', name, 'さん' = 値をそのまま返す
# sep = '+', end = '' = 名前付きの値を渡す
```

---

### *5.1.2. 型*
型 (データ型)：コードの中で扱える値の種類を決めるための仕組み
* クラス：型をより専用的な用語 (設計図)
* インスタンス：クラスをもとに作られたオブジェクトのこと
* インスタンス化：型に対して具体的な値を与えて、コードの中で利用できるようにすること (クラスをインスタンス化してインスタンスを作成すること)

### [ 一般的なインスタンス化 ]
構文例
```py
型名(引数, ...)

# コンストラクター：型名を関数のように呼び出すことで、インスタンスを作成できる
```

datetimemodule.py 
```py
import datetime

today = datetime.date.today()
print(today)
```

実行結果
```
$ python3 datetimemodule.py 

2023-08-13
```


### [ 型に属する関数 ]
メソッド：型に属さない関数

構文例
```
インスタンス.メソッド(引数, ...)
```

sort_method.py
```py
data1 = [25, 3, 49, 67, 14]

data1.sort(reverse = True)  # sort メソッドを使う
print(data1)


data2 = [25, 3, 49, 67, 14]

print(sorted(data2, reverse = True))  # sorted 関数を使う
```

実行結果
```shell
$ python3 sort_method.py

[67, 49, 25, 14, 3]
[67, 49, 25, 14, 3]

# 結果は同じ
```

---

### *5.1.3. 組み込み型/関数とモジュール*
インポート：対象のモジュールを読み込むこと

構文例
```py
import モジュール名
```

import.py
```py
import math

print(math.floor(1.34))
```

実行結果
```shell
$ python3 import.py

1
```


## 5.2. 文字列の操作
### *5.2.1. 文字列の長さを取得する*

str_len.py
```py
title1 = 'プロジェクト'
print(len(title1))


title2 = 'testtitle'
print(len(title2))


import unicodedata
print(unicodedata.east_asian_width('あ'))
```

実行結果
```shell
$ python3 str_len.py

6
9
W  # W = 全角かな
<class 'str'>

# 日本語を正しく 1 文字としてカウントする
```

east_asian_width 関数の戻り値
| 分類 | 戻り値 | 意味 |
| --- | --- | --- |
| 全角 | F | Fullwidth (全角英数など) |
| 全角 | W | Wide (漢字や全角かななど) |
| 全角 | A | Ambiguous (特殊文字) |
| 半角 | Na | Narrow (半角英数など) |
| 半角 | H | Halfwidth (半角カタカナなど) |
| 半角 | N | Neutral (中立：いずれにも属さない) |

str_len_width.py
```py
import unicodedata

data = 'WINGS プロジェクト 2020'
count = 0

for i in data:
    if unicodedata.east_asian_width(i) in 'FWA':
        count += 2  # 戻り値が「F」「W」「A」の場合は文字幅を 2 としてカウント
    else:
        count += 1  # それ以外は文字幅を 1 としてカウント

print(count)
```

実行結果
```shell
$ python3 str_len_width.py 

23

# WINGS = 5
# プロジェクト = 12
# 2020 = 4
# スペース * 2 = 2
```

---

### *5.2.2. 文字列を大文字小文字で変換する*
大文字/小文字の変換メソッド
| メソッド | 概要 |
| --- | --- |
| lower() | 大文字 → 小文字に変換 |
| upper() | 小文字 → 大文字に変換 |
| swapcase() | 大文字と小文字を反転 |
| capitalize() | 先頭文字を大文字に、以降を小文字に変換 |
| title() | 単語の先頭文字を大文字に、それ以外を小文字に変換 |
| casefold() | 大文字小文字の区別を除去 |


str_lower.py
```py
data1 = 'Wings Project'
data2 = 'self learn python'
data3 = 'FuBball'

print(data1.lower())
print(data1.upper())
print(data1.swapcase())
print(data2.capitalize())
print(data2.title())
print(data3.lower())
print(data3.casefold())
```

実行結果
```
$ python3 str_lower.py 

wings project
WINGS PROJECT
wINGS pROJECT
Self learn python
Self Learn Python
fubball
fubball
```

---

### *5.2.3. 部分文字列を取得する*

構文例
```py
txt[index]
txt[start:end:step]

# txt: 文字列
# index: インデックス番号
# start: 開始位置
# end: 終了位置
# step: ステップ (増減)
```

str_slice.py
```py
title = 'あいうえおかきくけこ'

print(title[2])
print(title[2:5])
print(title[2:])
print(title[:5])
print(title[:])
print(title[-7:])
print(title[-7:-5])
print(title[::2])  # 2 ずつ
print(title[1::2])  # 「い」から 2 ずつ
print(title[::-1])
```

実行結果
```
$ python3 str_slice.py 

う
うえお
うえおかきくけこ
あいうえお
あいうえおかきくけこ
えおかきくけこ
えお
あうおきけ
いえかくこ
こけくきかおえういあ
```

### [ slice オブジェクト ]
slice オブジェクト：組み込み関数 slice で生成でき、indices メソッドでインデックス表現に変換できる

str_sliceogject.py
```py
title = 'あいうえおかきくけこ'

print(slice(-5, None, -1).indices(len(title)))

# slice(-5, None, -1) = [-5::-1]
# 5 から -1 (先頭) まで前方向 (-1) にスライスするという意味
```

実行結果
```
$ python3 str_sliceogject.py 

(5, -1, -1)
```

---

### *5.2.4. 文字の種類を判定する*
| メソッド | 概要 |
| --- | --- |
| isalnum() | 英数字であるか |
| isalpha() | 英字であるか |
| isascii() | ASCII 文字であるか |
| isdecimal() | 10 進数値であるか |
| isdigit() | 数値であるか |
| isnumeric() | 数値も時であるか |
| isidentifier() | 有効な識別子であるか |
| islower() | 小文字であるか |
| isupper() | 大文字であるか | 
| istitle() | 単語の先頭文字だけが大文字であるか |
| isprintable() | 印字可能な文字であるか |
| isspace() | 空白文字であるか |

str_istype.py
```py
print('abc123'.isalnum())
print('abc++'.isalnum())
print('abcde'.isalpha())
print('abc123'.isalpha())
print('あいう'.isascii())
print('100'.isdecimal())
print('0x64'.isdecimal())
print('1234'.isdigit())
print('1234.56'.isdigit())
print('百万'.isnumeric())
print('million'.isnumeric())
print('abc_123'.isidentifier())
```

実行結果
```
$ python3 str_istype.py 

True
False
True
False
False
True
False
True
False
True
False
True
```

文字種による結果の比較
| 文字種 | isdigit | isdecimal | isnumeric |
| --- | --- | --- | --- |
| 半角数字 ('15') | True | True | True |
| 上付き数字 ('\u2078') | True | False | True |
| 全角数字 ('１５') | True | True | True |
| ローマ数字 ('XV') | False | False | True |
| 漢数字 ('一参億') | False | エラー | エラー |

* isdecimal：アラビア数字だけを認める
* isdigit：アラビア数字 + 上付き数字のような文字を認める
* isnumeric：アラビア数字 + 上付き数字 + 漢数字やローマ数字を認める


### [ 文字列を数値に変換する ]
* digit：int 値
* numeric：float 値
* 漢数字/ローマ数字を変換できるのは numeric 関数

str_num.py
```py
import unicodedata

print(unicodedata.digit('5'))
print(unicodedata.numeric('参'))
```

実行結果
```
$ python3 str_num.py

5
3.0
```


### [ 予約済みの識別子を確認する ]
str_keyword.py
```py
import keyword

id1 = 'tiff'
id2 = 'if'

print(id1.isidentifier())
print(id2.isidentifier())
print(keyword.iskeyword(id1))
print(keyword.iskeyword(id2))
```

isidentifier メソッド：与えられた文字列が識別子として認められている文字のみで構成されるかを判定するだけ
* keyword モジュールの iskeyword 関数を利用する

---

### *5.2.5. 文字列を検索する*
find/rfind メソッド構文例
```py
s.find(sub[, start[, end]])
s.rfind(sub[, start[, end]])

# s：元の文字列
# sub：検索文字列
# start：検索開始位置
# end：検索終了位置

# find メソッド：検索を前方から開始
# rfind メソッド：検索を後方から開始
```

str_find.py
```py
msg = 'にわにはにわにわとりがいる'

print(msg.find('にわ'))  # 文字列を先頭から順に検索し、見つかった場合にその文字位置を返す
print(msg.find('にも'))  # 引数 sub で見つからない場合は -1
print(msg.rfind('にわ'))  # 文字列を後方から検索し、先頭からの文字位置を返す
print(msg.find('にわ', 3))  # 開始位置 3
print(msg.find('にわ', 3, 5))  # 開始位置 3、終了位置 5
print(msg.find('にわ', -7, -1))  # 開始位置 -7、終了位置 -1
```

実行結果
```
$ python3 str_find.py 
0
-1
6
4
-1
6
```


### [ 例外を返す index/rindex メソッド ]
* index/rindex メソッド：例外を返す
* 文字列が見つからない場合に、条件分岐 (if)、例外 (try) いずれかで処理するかによって find/index いずれを利用するか判断する

index メソッド構文例
```py
msg = 'にわにはにわにわとりがいる'

print(msg.index('にも'))
```

実行結果
```
$ python3 str_index.py 

PythonExampleCode/str_index.py", line 3, in <module>
    print(msg.index('にも'))
          ^^^^^^^^^^^^^^^
ValueError: substring not found
```


### [ 部分文字列の登場回数をカウントする ]
count メソッド構文例
```py
s.count(sub[, start[, end]])

# s：元の文字列
# sub：検索文字列
# start：検索開始位置
# end：検索終了位置
```

str_count.py
```py
msg = 'にわにはにわにわとりがいる'

print(msg.count('にわ'))
print(msg.count('にわ', 3))
print(msg.count('にわ', 3, 6))

msg = 'いちいちいちばにいち'
print(msg.count('いちいち'))  # count メソッドは寿福のない出現数をカウントするので、出現数は 1 回
```

実行結果
```
$ python3 str_count.py 

3
2
1
1
```

---

### *5.2.6. 文字列の前後から空白を除去する*
strip/isstrip/rstrip メソッド構文例
```py
s.strip([chars])
s.istrip([chars])
s.rstrip([chars])

# s：元の文字列
# chars：除去する文字群 (規定は空白文字)

# strp メソッド：前後双方の空白を除去
# istrip メソッド：前方だけの空白を除去
# rstrip メソッド：後方だけの空白を除去
```

str_strip.py
```py
msg = ' 　こんにちは \t\n\r'

print('「' + msg.strip() + '」')
print('「' + msg.lstrip() + '」')
print('「' + msg.rstrip() + '」')


msg2 = msg2 = '!======［独習Python］======!'
print('「' + msg2.strip('!=［］') + '」')
```

実行結果
```
$ python3 str_strip.py 

「こんにちは」
「こんにちは 
」
「 　こんにちは」
「独習Python」
```

除去するべき空白
* 全角空白
* タブ文字 (\t, \v)
* 改行文字 (\r, \n)
* フォームフィード (\f)

---

### *5.2.7. 文字列に特定の文字列が含まれるかを判定する*
startswith/endswith メソッド構文
```py
substr in s 
s.starts(prefix[, start[, end]])
s.endswith(suffix[, start[, end]])

# s：元の文字列
# substr/prefix/suffix：検索文字列
# start：検索開始位置
# end：検索終了位置

# startswith メソッド：ある文字列が先頭に位置するか
# endswith メソッド：ある文字が末尾に位置するか
```

str_in.py
```py
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
```

実行結果
```
$ python3 str_in.py

True
False
False
False
True
False
False
False
False
```

---

### *5.2.8. 文字列を特定の区切り文字で分割する*

spit/rsplit メソッド
```py
s.split(sep = None, maxsplit = -1)
s.rsplit(sep = None, maxsplit = -1)

# s：元の文字列
# sep：区切り文字
# maxsplit：最大分割数

# split メソッド：文字列を前方から分割
# rsplit メソッド：文字列を後方から分割
```

str_split.py
```py
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
```

実行結果
```
$ python3 str_split.py 

['ねこ', 'いぬ', 'たぬき']
['さくら', 'もも', 'うめ', 'ききょう']
['さくら', 'もも', 'うめ', 'ききょう']
['さくら', 'もも', 'うめ|ききょう']
['さくら|もも', 'うめ', 'ききょう']
```

### [ 改行文字で文字列を分割する - splitlines メソッド ]
splitlines メソッドで認識する改行
| 改行文字 | 概要 |
| --- | --- |
| \n | 改行 (ラインフィード) |
| \r | 復帰 (キャリッジリターン) |
| \r\n | 改行 + 復帰  |
| \x85 | 改行 (C1 制御コード) |
| \v, \x0b | 垂直タブ |
| \f, \x0c | 改ページ |
| \x1c | ファイル区切り |
| \x1d | グループ区切り |
| \x1e | レコード区切り |
| \u2028 | 行区切り |
| \u2029 | 段落区切り |

str_split_lines.py
```py
msg = '''\
こんにちは
こんばんは
さようなら    
'''

print(msg.splitlines())
print(msg.splitlines(True))
```

実行結果
```
$ python3 str_split_lines.py

['こんにちは', 'こんばんは', 'さようなら    ']
['こんにちは\n', 'こんばんは\n', 'さようなら    \n']
```

---

### *5.2.9. リストを結合する*

---

### *5.2.10. 文字列を置き換える*

---

### *5.2.11. 文字を整形する*

---

### *5.2.12. str 型 bytes 型を変換する*

---

## 5.3. 日付/時刻の操作