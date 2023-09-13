# Chapter 05. 標準ライブラリ
ライブラリ：コードから自在に呼び出せる命令

### [ 目次 ]
5.1. [ライブラリの分類](https://github.com/pp203/PythonStudy/tree/main/SelfStudy/Chapter05/StudyNote#51-%E3%83%A9%E3%82%A4%E3%83%96%E3%83%A9%E3%83%AA%E3%81%AE%E5%88%86%E9%A1%9E)

- 5.1.1. [関数](https://github.com/pp203/PythonStudy/tree/main/SelfStudy/Chapter05/StudyNote#511-%E9%96%A2%E6%95%B0)
- 5.1.2. [型](https://github.com/pp203/PythonStudy/tree/main/SelfStudy/Chapter05/StudyNote#512-%E5%9E%8B)
- 5.1.3. [組み込み型/関数とモジュール](https://github.com/pp203/PythonStudy/tree/main/SelfStudy/Chapter05/StudyNote#513-%E7%B5%84%E3%81%BF%E8%BE%BC%E3%81%BF%E5%9E%8B%E9%96%A2%E6%95%B0%E3%81%A8%E3%83%A2%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AB)

5.2. [文字列の操作](https://github.com/pp203/PythonStudy/tree/main/SelfStudy/Chapter05/StudyNote#52-%E6%96%87%E5%AD%97%E5%88%97%E3%81%AE%E6%93%8D%E4%BD%9C)

- 5.2.1. [文字列の長さを取得する](https://github.com/pp203/PythonStudy/tree/main/SelfStudy/Chapter05/StudyNote#521-%E6%96%87%E5%AD%97%E5%88%97%E3%81%AE%E9%95%B7%E3%81%95%E3%82%92%E5%8F%96%E5%BE%97%E3%81%99%E3%82%8B)
- 5.2.2. [文字列を大文字小文字で変換する](https://github.com/pp203/PythonStudy/tree/main/SelfStudy/Chapter05/StudyNote#522-%E6%96%87%E5%AD%97%E5%88%97%E3%82%92%E5%A4%A7%E6%96%87%E5%AD%97%E5%B0%8F%E6%96%87%E5%AD%97%E3%81%A7%E5%A4%89%E6%8F%9B%E3%81%99%E3%82%8B)
- 5.2.3. [部分文字列を取得する](https://github.com/pp203/PythonStudy/tree/main/SelfStudy/Chapter05/StudyNote#523-%E9%83%A8%E5%88%86%E6%96%87%E5%AD%97%E5%88%97%E3%82%92%E5%8F%96%E5%BE%97%E3%81%99%E3%82%8B)
- 5.2.4. [文字の種類を判定する](https://github.com/pp203/PythonStudy/tree/main/SelfStudy/Chapter05/StudyNote#524-%E6%96%87%E5%AD%97%E3%81%AE%E7%A8%AE%E9%A1%9E%E3%82%92%E5%88%A4%E5%AE%9A%E3%81%99%E3%82%8B)
- 5.2.5. [文字列を検索する](https://github.com/pp203/PythonStudy/tree/main/SelfStudy/Chapter05/StudyNote#525-%E6%96%87%E5%AD%97%E5%88%97%E3%82%92%E6%A4%9C%E7%B4%A2%E3%81%99%E3%82%8B)
- 5.2.6. [文字列の前後から空白を除去する](https://github.com/pp203/PythonStudy/tree/main/SelfStudy/Chapter05/StudyNote#526-%E6%96%87%E5%AD%97%E5%88%97%E3%81%AE%E5%89%8D%E5%BE%8C%E3%81%8B%E3%82%89%E7%A9%BA%E7%99%BD%E3%82%92%E9%99%A4%E5%8E%BB%E3%81%99%E3%82%8B)
- 5.2.7. [文字列に特定の文字列が含まれるかを判定する](https://github.com/pp203/PythonStudy/tree/main/SelfStudy/Chapter05/StudyNote#527-%E6%96%87%E5%AD%97%E5%88%97%E3%81%AB%E7%89%B9%E5%AE%9A%E3%81%AE%E6%96%87%E5%AD%97%E5%88%97%E3%81%8C%E5%90%AB%E3%81%BE%E3%82%8C%E3%82%8B%E3%81%8B%E3%82%92%E5%88%A4%E5%AE%9A%E3%81%99%E3%82%8B)
- 5.2.8. [文字列を特定の区切り文字で分割する](https://github.com/pp203/PythonStudy/tree/main/SelfStudy/Chapter05/StudyNote#528-%E6%96%87%E5%AD%97%E5%88%97%E3%82%92%E7%89%B9%E5%AE%9A%E3%81%AE%E5%8C%BA%E5%88%87%E3%82%8A%E6%96%87%E5%AD%97%E3%81%A7%E5%88%86%E5%89%B2%E3%81%99%E3%82%8B)
- 5.2.9. [リストを結合する](https://github.com/pp203/PythonStudy/tree/main/SelfStudy/Chapter05/StudyNote#529-%E3%83%AA%E3%82%B9%E3%83%88%E3%82%92%E7%B5%90%E5%90%88%E3%81%99%E3%82%8B)
- 5.2.10. [文字列を置き換える](https://github.com/pp203/PythonStudy/tree/main/SelfStudy/Chapter05/StudyNote#5210-%E6%96%87%E5%AD%97%E5%88%97%E3%82%92%E7%BD%AE%E3%81%8D%E6%8F%9B%E3%81%88%E3%82%8B)
- 5.2.11. [文字を整形する](https://github.com/pp203/PythonStudy/tree/main/SelfStudy/Chapter05/StudyNote#5211-%E6%96%87%E5%AD%97%E3%82%92%E6%95%B4%E5%BD%A2%E3%81%99%E3%82%8B)
- 5.2.12. [str型bytes型を変換する](https://github.com/pp203/PythonStudy/tree/main/SelfStudy/Chapter05/StudyNote#5212-str-%E5%9E%8B-bytes-%E5%9E%8B%E3%82%92%E5%A4%89%E6%8F%9B%E3%81%99%E3%82%8B)

5.3. [日付/時刻の操作](https://github.com/pp203/PythonStudy/tree/main/SelfStudy/Chapter05/StudyNote#53-%E6%97%A5%E4%BB%98%E6%99%82%E5%88%BB%E3%81%AE%E6%93%8D%E4%BD%9C)

- 5.3.1. [日付/時刻値を生成する](https://github.com/pp203/PythonStudy/tree/main/SelfStudy/Chapter05/StudyNote#531-%E6%97%A5%E4%BB%98%E6%99%82%E5%88%BB%E5%80%A4%E3%82%92%E7%94%9F%E6%88%90%E3%81%99%E3%82%8B)
- 5.3.2. [年月日、時分秒などの時刻要素を取得する](https://github.com/pp203/PythonStudy/tree/main/SelfStudy/Chapter05/StudyNote#532-%E5%B9%B4%E6%9C%88%E6%97%A5%E6%99%82%E5%88%86%E7%A7%92%E3%81%AA%E3%81%A9%E3%81%AE%E6%99%82%E5%88%BB%E8%A6%81%E7%B4%A0%E3%82%92%E5%8F%96%E5%BE%97%E3%81%99%E3%82%8B)
- 5.3.3. [日付/時刻を加算/減算する](https://github.com/pp203/PythonStudy/tree/main/SelfStudy/Chapter05/StudyNote#533-%E6%97%A5%E4%BB%98%E6%99%82%E5%88%BB%E3%82%92%E5%8A%A0%E7%AE%97%E6%B8%9B%E7%AE%97%E3%81%99%E3%82%8B)
- 5.3.4. [日付/時刻値の差分を求める](https://github.com/pp203/PythonStudy/tree/main/SelfStudy/Chapter05/StudyNote#534-%E6%97%A5%E4%BB%98%E6%99%82%E5%88%BB%E5%80%A4%E3%81%AE%E5%B7%AE%E5%88%86%E3%82%92%E6%B1%82%E3%82%81%E3%82%8B)
- 5.3.5. [日付/時刻値を比較する](https://github.com/pp203/PythonStudy/tree/main/SelfStudy/Chapter05/StudyNote#535-%E6%97%A5%E4%BB%98%E6%99%82%E5%88%BB%E5%80%A4%E3%82%92%E6%AF%94%E8%BC%83%E3%81%99%E3%82%8B)
- 5.3.6. [日付/時刻値を整形する](https://github.com/pp203/PythonStudy/tree/main/SelfStudy/Chapter05/StudyNote#536-%E6%97%A5%E4%BB%98%E6%99%82%E5%88%BB%E5%80%A4%E3%82%92%E6%95%B4%E5%BD%A2%E3%81%99%E3%82%8B)
- 5.3.7. [カレンダーを生成する](https://github.com/pp203/PythonStudy/tree/main/SelfStudy/Chapter05/StudyNote#537-%E3%82%AB%E3%83%AC%E3%83%B3%E3%83%80%E3%83%BC%E3%82%92%E7%94%9F%E6%88%90%E3%81%99%E3%82%8B)

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

### [ 区切り文字で文字列を 2 分割する ]
* split メソッド：全ての区切りで文字列を分割する
* partition メソッド：区切り文字が最初に見つかった位置で文字列を分割する
* rpartition メソッド：区切り文字が最後に見つかった位置で文字列を分割する
* partition/rpartition メソッドの戻り値は「区切り前の文字列, 区切り文字, 区切り後の文字列」

str_split_part.py
```py
msg = 'example.com/index/html'

print(msg.partition('.'))
print(msg.rpartition('.'))
print(msg.partition('|'))
```

実行結果
```
$ python3 str_split_part.py 

('example', '.', 'com/index/html')
('example', '.', 'com/index/html')
('example.com/index/html', '', '')
```

---

### *5.2.9. リストを結合する*
join メソッド構文例
```py
s.join(iterable)

# s：区切り文字
# iterable：連結対象のリスト
```

str_join.py
```py
data1 = ['いぬ', 'ねこ', 'たぬき']
print(','.join(data1))

data2 = [10, 103, 18]
# print('\t'.join(data2))
# TypeError: sequence item 0: expected str instance, int found
# 数値方リストを json メソッドでそのまま連結することはできない

print('\t'.join([str(i) for i in data2]))
```

実行結果
```
$ python3 str_join.py

いぬ,ねこ,たぬき
10      103     18
```

---

### *5.2.10. 文字列を置き換える*

replace メソッド構文例
```py
s.replace(old, new [,count])

# s：元の文字列
# old：置き換える部分の文字列
# new：置き換え後の文字列
# count：置き換える個数
```

str_replace.py
```py
msg = 'にわにはにわにわとりがいる'

print(msg.replace('にわ', 'ニワ'))
print(msg.replace('にわ', 'ニワ', 2)) 
```

実行結果
```
$ python3 str_replace.py 

ニワにはニワニワとりがいる
ニワにはニワにわとりがいる
```

### [ 特定の文字を変換/削除する ]
translate メソッド：文字列に含まれる特定の文字を変換/削除

maketrans メソッド構文例
```py
str.maketrans(dict)
str.maketrans(old, new[, no])

# dict: 「変換前: 変換後」の辞書
# old: 変換前の文字群
# new: 変換後の文字群
# no: 削除する文字群
```

str_translate.py
```py
msg = '今日の,あなたの運勢は,●良い感じ●です.'

# 変換前後の文字を辞書として定義
print(msg.translate(str.maketrans({
    ',': '、',
    '.': '。',
    '●': ''
})))

# 変換すべき文字群を文字列として定義
print(msg.translate(str.maketrans(',.', '、。', '●')))
```

実行結果
```
$ python3 str_translate.py 

今日の、あなたの運勢は、良い感じです。
今日の、あなたの運勢は、良い感じです。
```


---

### *5.2.11. 文字を整形する*
format メソッド: 指定された書式文字列に基づいて文字列を整形する

format メソッド構文例
```py
txt.format(*argas, **kwargs)

# txt: 書式文字列
# args: 書式に割り当てる値 (可変長引数)
# kwargs: 書式に割り当てる値 (キーワード可変長引数)
```

str_format.py
```py
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
```

実行結果
```py
$ python3 str_format.py
サクラは女の子、2歳です。 # 1.
サクラは2歳、女の子です。 # 2.
サクラは2歳、女の子です。 # 3.
サクラは女の子、2歳です。 # 4.
name='サクラ'はsex='女の子'、age=2歳です。 # 5.
```


### [ 書式の指定 ]
書式指定子
```
[[fill]align][sign][#][0][width][group_opt][.prec][type]

# fill: 桁数不足時に埋め込む文字 (規定または空白)
# align: 配置指定
# sign: 符号
# width: 最小の表示幅 (省略時はその値の幅)
# group_opt: 桁区切り文字
# prec: 有効桁数
# type: データ型

{<インデックス番号>:<文字寄せ><符号><最小幅><桁区切り><有効桁数><型>}
{1:>+12,.2f}  # 例
```

| 分類 | 書式 | 概要 |
| --- | --- | --- |
| fill |  | 桁数が不足した時に埋め込む文字。埋め込み場所は align によって変化する。(規定は空白)
| align | > | 右寄せ |
| align | < | 左寄せ |
| algin | ^ | 中央寄せ |
| align | = | 符号の後方を埋める |
| sign | + | 正負の符号を付与 |
| sign | - | 負数の場合 - を付与 |
| sign | 空白 | 正数には空白、負数には - を付与 |
| 定数 | # | type が b、o、x の場合に「0b」「0o「0x」を付与 |
| 定数 | 0 | 符号の後方を「0」で埋め (fill/align が「0=」と同じ意味) |
| width |  | 最小の表示幅 (省略時はその値の幅) |
| group_opt | . | 3 桁ごとに「.」で区切り |
| group_opt | - | 10 進数では 3 桁ごと、2/8/16 進数では 4 桁ごとに「_」で区切り |
| prec | | type が f の場合は小数点以下の桁数、g の場合は小数点前後の桁数 | 
| type | % | パーセント | 
| type | d | 整数 (10 進数表記) |
| type | b | 2 進数表記 |
| type | o | 8 進数表記 |
| type | x, X | 16 進数表記 (x の場合はアルファベット文字、X の場合は大文字) |
| type | e, E | 浮動小数点 (指数表記。e の場合小文字、E の場合大文字) |
| type | f, F | 浮動小数点 (小数点表記。f の場合は nan/inf, F の場合は NAN/INF と表示) |
| type | g, G | 汎用フォーマット (桁に応じて固定小数点、または指数表記で表示) |
| type | s | 文字列 (規定) |

str_format2.py
```py
# 表示桁数と文字寄せ
## align と width を指定した場合
## aligh は値の表示幅が width よりも小さい場合、値を指定の方向に寄せるため、必ず width とセットで使う
print('{0:>10}'.format('wings'))

## 文字寄せの時、指定文字で不足桁を埋める場合
## 今回の場合、"*" で埋めているが、無指定の場合は半角空白で埋めることも可能
print('{0:*>10}'.format('wings'))

## "=" 指定で符号の後方を埋めることも可能
## {0:010} と同じ
## この場合の "0" は fill ではなく、定数の 0
print('{0:0=10}'.format(-12345))


# 桁区切り文字
## group_opt を指定した場合
print('{0:,}'.format(9876543210))  # 一般的なカンマ表記。3 桁ごとに数値を区切る。
print('{0:#_x}'.format(0x5f5bce1aa))  # "_" = 2/8/16 進数向けの区切り文字。 4 桁ごとに数値を区切る。10 進数では、3 桁ごとに区切る。


# 有効桁数
## ".prec" 形式で有効桁数を指定可能
## 後方の "type" 型指定によって挙動が変化する
print('{0:.1f}cm'.format(5))  # 浮動小数点 {0:.1f} = 小数点以下の桁数を意味する
print('{0:.4g}'.format(22.567))  # 汎用フォーマット {0:.4g} = 小数点前後の桁数を意味する


# 型変換
## 10 進数値 → 16 進数に変換する
## x/X の違い: 10 ~ 15 (A ~ F) を大文字/小文字 で表記するかどうか
## 定数 "#" を指定した場合でも影響する
print('{0:x}'.format(255))
print('{0:X}'.format(255))

## 小数点数を 100 倍にし、 % を付与する
## 数値の扱いは f 指定と同じであるため、小数点以下を 2 桁で丸める
print('{0:.2%}'.format(0.12345))
```

実行結果
```
$ python3 str_format2.py

     wings
*****wings
-000012345
9,876,543,210
0x5_f5bc_e1aa
5.0cm
22.57
ff
FF
12.35%
```

---

### *5.2.12. str 型 bytes 型を変換する*
* 前提: 文字列 (str 型) は、文字列情報を Unicode データとして保存する。
* 情報に基づいて、文字列をエンコード変換する
* 例: Shift-JIS ←→ UTF-8 など
* encode メソッドは、エンコードした結果を bytes 型として返す。バイト列を受け取った場合でも、その値を決められた形式で変換すれば、元の文字列を復元できる。
* バイト列: 0 ~ 255 の値の連なりのこと
* エンコード: bytes 型に変換すること
* デコード: bytes 型から str 型に戻すこと

encode メソッド 
```py
txt.encode(encoding = "utf-8", errors = "strict")

## txt: 任意の文字列
## encoding: 変換に利用する文字エンコーディング (shift-jis、euc-jp、iso-2022-jp...etc)
## errors: エラー時の挙動
```

decode メソッド
```py
bs.decode(encoding= "utf-8", errors = "strict")

## bs: 任意のバイト列
## encoding: 変換に利用する文字エンコーディング
## errors: エラー時の挙動
```

エンコード時と異なる文字エンコーディングでデコードした場合、変換に失敗する。  
その場合は、以下の引数 errors で指定できる。
| 設定値 | 概要 |
| --- | --- |
| stric | エラー (例外) を発生して処理を中止 |
| ignore | 変換できない文字は除去して、そのまま処理を継続 |
| replace | 変換できない文字は "?" などに置き換える |

str_encode.py
```py
data = 'こんにちは'

## エンコードした場合
encoded = data.encode('sjis')
print(encoded)


## 上記をデコードした場合
print(encoded.decode('sjis'))


## エンコード時とは異なる文字エンコードでデコードした場合
print(encoded.decode('euc-jp','replace'))
```

実行結果
```
$ python3 str_encode.py

b'\x82\xb1\x82\xf1\x82\xc9\x82\xbf\x82\xcd'
こんにちは
����������
```

---

## 5.3. 日付/時刻の操作

datatime モジュール
* naive 型: タイムゾーンの情報を持たない
* aware 型: タイムゾーンの情報を持つ

| 型 | 概要 | naive 型か aware 型か |
| --- | --- | --- |
| datatime | 日付/時刻値 | タイムゾーン (tzinfo) を設定するかどうかよって naive か aware か決まる |
| date | 日付値 | 常に naive |
| time | 時刻値 | タイムゾーン (tzinfo) を設定するかどうかよって naive か aware か決まる |
| timezone | タイムゾーン情報 | - |
| timedata | 時刻間隔 | - |


--- 

### *5.3.1. 日付/時刻値を生成する*
### [ 現在の日付/時刻から生成する ]

now / today メソッド
| メソッド | 概要 |
| --- | --- |
| datetime.today() | 現在の日時 |
| date.today() | 今日の日付 |
| datetime.now(tz=None) | 現在の日時 (タイムゾーン付き) |
| datetime.utcnow() | 現在の UTC 日時 |

dt_now.py
```py
import datetime

## today メソッド
### 現在の日時を返す
print(datetime.datetime.today())  
print(datetime.date.today())  ## date.today メソッドは日付のみを返す


## now メソッド
###　datetime 型の now メソッドは、 today メソッドと似ている
print(datetime.datetime.now())  ## 引数がない場合は today メソッドと同じ値を返す
print(datetime.datetime.now(
    datetime.timezone(datetime.timedelta(hours = 9))
))  ## tz (datetime.timezone) を指定することで aware 型を返すことが可能


## UTC
print(datetime.datetime.utcnow())  ## あくまで値が UTC 時刻なので、内部的には naive 型 (tz を持たない)
print(datetime.datetime.now(datetime.timezone.utc))  ## aware 型の UTC 時刻


## datetime.datetime.<> と 2 つの datetime が必要な理由
### datetime というモジュールの中に datetime オブジェクトがあり、その中にメソッドがあるから
### from datetime import datetime で 1 つで済む
```

実行結果
```
$ python3 dt_now.py 

2023-09-08 12:49:19.191362
2023-09-08
2023-09-08 12:49:19.191391
2023-09-08 12:49:19.191396+09:00
2023-09-08 03:49:19.191548
2023-09-08 03:49:19.191552+00:00
```


### [ 指定された年月日、時分秒から生成する ]

datetime / date / time コンストラクター
```py
## メモ: fold = 夏時間を加味するか

## datetime
datetime(
  year,
  month,
  day,
  hour = 0,
  minute = 0,
  second = 0,
  microsecond = 0,
  tzinfo = None,
  *,
  fold = 0
)

## date
date(
  year,
  month,
  day
)

## time
time(
  hour = 0,
  minute = 0,
  second = 0,
  microsecond = 0,
  tzinfo = None,
  *,
  fold = 0
)
```

dt_construct.py
```py
import datetime

## datetime / time のみが aware 型を生成できる

print(datetime.datetime(2023, 9, 1, 13, 30, 35, 500))

## aware 型の生成が可能
print(datetime.datetime(2023, 9, 1, 13, 30, 35, 500,
datetime.timezone(datetime.timedelta(hours = 9))))

print(datetime.date(2023, 9, 1))

print(datetime.time(13, 30, 35, 500))

## aware 型の生成が可能
print(datetime.time(13, 30, 35, 500,
datetime.timezone(datetime.timedelta(hours = 9))))


## エラーになる。
## 月は 1 ~ 12 であり、繰り上がり「2024 年 01 月」ということにはならない。
print(datetime.datetime(2023, 13, 1, 13, 30, 35, 500))


## combine メソッドで既存の date / time / tz オブジェクトを組み合わせて datetime オブジェクトの生成も可能
d = datetime.date(2023, 9, 1)
t = datetime.time(13, 30, 35, 500)
tz = datetime.timezone(datetime.timedelta(hours = 9))

print(datetime.datetime.combine(d, t, tz))
```

実行結果
```
$ python3 dt_construct.py

2023-09-01 13:30:35.000500
2023-09-01 13:30:35.000500+09:00
2023-09-01
13:30:35.000500
13:30:35.000500+09:00

Traceback (most recent call last):
  File "dt_construct.py", line 21, in <module>
    print(datetime.datetime(2023, 13, 1, 13, 30, 35, 500))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: month must be in 1..12

2023-09-01 13:30:35.000500+09:00
```


### [ 日付/時刻文字列から変換する ]
strptime メソッド：日付 / 時刻文字列を指定の形式で解析し、datetime オブジェクトを生成する

```py
datetime.strptime(date_string, format)

## date_string：日付文字列
## format：解析に利用する書式
```

dt_parse.py
```py
import datetime
from datetime import datetime

dt1 = datetime.strptime('2023/9/1 13:30:35', '%Y/%m/%d %H:%M:%S')
print(dt1)


## fromisoformat メソッド
### 年月日は必須であり、桁数もそれぞれ指定の桁で 0 埋めする必要がある
dt2 = datetime.fromisoformat('2023-09-01 13:30:35+09:00')
print(dt2)
```

実行結果
```
$ python3 dt_parse.py

2023-09-01 13:30:35
2023-09-01 13:30:35+09:00
```


### [ タイムスタンプ値から生成する ]
fromtimestamp メソッド：タイムスタンプ値から日付 / 時刻値を生成できる

```py
datetime.fromtimestamp(timestammp, tz = None)
datetime.fromtimestamp(timestamp)

## timestamp：タイムスタンプ値
## tz：タイムゾーン
```

dt_timestamp.py
```py
import datetime
from datetime import datetime, timezone, date

dt = datetime.now(timezone.utc)
ts = dt.timestamp()

## tz なしで呼び出しているので datetime オブジェクトは naive
print(datetime.fromtimestamp(ts))
print(datetime.fromtimestamp(ts, timezone.utc))

print(date.fromtimestamp(ts))  ## date オブジェクトでは tz は指定できない
```


### [ 一部の要素を置くかえた日付を生成する ]
replace メソッド：既存の datetime / date / time オブジェクトから特定の要素をかく変えて新しい datetime / date / time オブジェクトが可能

```py
## dt
dt.replace(
  year = self.year,
  month = self.month,
  day = self.day,
  hour = self.hour,
  minute = self.minute,
  second = self.second,
  microsecond = self.micsrosecond,
  tzinfo = self.tzinfo,
  *,
  fold = 0
)


## dat
dat.replace(
  year = self.year,
  month = self.month,
  day = self.day,
)


## tim
tim.replace(
  year = self.year,
  month = self.month,
  day = self.day,
  hour = self.hour,
  minute = self.minute,
  second = self.second,
  microsecond = self.micsrosecond,
  tzinfo = self.tzinfo,
  *,
  fold = 0
)
```

dt_replace.py
```py
import datetime
from datetime import datetime

dt1 = datetime(2023, 9, 1, 13, 30, 35, 500)
dt2 = dt1.replace(day =11, minute = 40)  ## 引数名 = 値

print(dt1)
print(dt2)
```

実行結果
```
$ python3 dt_replace.py

2023-09-01 13:30:35.000500
2023-09-11 13:40:35.000500
```

---

### *5.3.2. 年月日、時分秒などの時刻要素を取得する*

日付 / 時刻要素を取得するための属性
| 属性 | 概要 |
| --- | --- |
| year | 年 |
| month | 月 (1 ~ 12) |
| day | 日 (1 ~ 31) |
| hour | 時 (0 ~ 23) |
| minute | 分 (0 ~ 59) |
| second | 秒 (0 ~ 59) |
| microsecond | マイクロ秒 (0 ~ 999999) |
| tzinfo | タイムゾーン (timezone 型) |

dt_get.py
```py
import datetime
from datetime import datetime, timezone

dt = datetime.now(timezone.utc)

print(dt)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)
```

実行結果
```
$ python3 dt_get.py

2023-09-11 02:33:24.110898+00:00
2023
9
11
2
33
24
110898
UTC
```

日付 / 時刻要素を取得するためのメソッド
| メソッド | 概要 |
| --- | --- |
| date() | 日付部分を取得 |
| time() | 時刻部分を取得 (naive) |
| timetz() | 時刻部分を取得 (aware) | 
| timestamp() | タイムスタンプ値を取得 |
| toordinal() | 西暦 1 年 1 月 1 日から通算日 |
| weekday() | 曜日を取得 (0：月~6：日) |
| isoweekday() | 曜日を取得 (1：月~7：日) |
| isocalendar() | 「ISO 年、ISO 週番号、ISO 曜日」のタプルを取得 |

dt_get2.py
```py
import datetime
from datetime import datetime, timezone

dt = datetime.now(timezone.utc)

print(dt)
print(dt.date())
print(dt.time())
print(dt.timetz())
print(dt.timestamp())
print(dt.toordinal())
print(dt.weekday())
print(dt.isoweekday())
print(dt.isocalendar())
```

実行結果
```
$ python dt_get2.py

2023-09-11 03:39:15.256976+00:00
2023-09-11
03:39:15.256976
03:39:15.256976+00:00
1694403555.256976
738774
0
1
datetime.IsoCalendarDate(year=2023, week=37, weekday=1)
```

---

### *5.3.3. 日付/時刻を加算/減算する*

datetime モジュールの「+」「-」で加算 / 減算できる
```py
dt + delta
dt - delta

## dt：日付 / 時刻値 (datetime/date/time)
## delta：加算 / 減算する (timedelta)
```

dt_plus.py
```py
import datetime
from datetime import datetime, timedelta

dt = datetime(2023, 9, 1, 15, 30, 35, 500)
dt_p = dt + timedelta(days = 10, hours = 20)
dt_m = dt - timedelta(weeks = 3)

print(dt)    ## 結果：2023-09-01 15:30:35.000500
print(dt_p)  ## 結果：2023-09-12 11:30:35.000500
print(dt_m)  ## 結果：2023-08-31 15:30:35.00050
```

timedelta コンストラクター
```py
timedelta(days = 0, weeks = 0, hours = 0, minutes = 0, seconds = 0, microseconds = 0, milliseconds = 0)
```

→ replace メソッドと同じで「日時要素 = 値」形式のキーワード引数として表す。

---

### *5.3.4. 日付/時刻値の差分を求める*

datetime/date/time は「-」演算で互いの差を求めることが可能
```py
dt1 - dt2

## dt1/dt2：日付 / 時刻値 (datetime/date/time)
```

dt_diff.py
```py
import datetime
from datetime import datetime

dt1 = datetime(2023, 9, 1, 15, 30, 35, 500)
dt2 = datetime(2023, 11, 23, 20, 00, 20, 300)

delta = dt2 - dt1


# 文字列化した差分
print(delta)  ## 結果：83 days, 4:29:44.999800


# 日数、秒数のみを取り出すこともできる
print(delta.days)     ## 結果：83
print(delta.seconds)  ## 結果：16184
```

---

### *5.3.5. 日付/時刻値を比較する*

「<」「>」などの比較演算子から日付 / 時刻のいずれかが過去 / 未来かを判定できる

dt_compare.py
```py
import datetime
from datetime import datetime

dt1 = datetime(2023, 9, 15, 20, 30, 50, 500)
dt2 = datetime(2020, 5, 13, 3, 15, 50, 500)


# dt1 は dt2 より大きい = dt1 は dt2 よりも未来である
print(dt1 > dt2)  ## 結果：True
```

---

### *5.3.6. 日付/時刻値を整形する*

strftime メソッドで日付 / 時刻値を整形する
```py
dt.strftime(format)

## dt：日付 / 時刻値 (datetime/date/time)
## format：書式文字列
```

日付を整形するための指定子 (2020-02-09 16:24:39.000351+00:00 の場合)
| 分類 | 指定子 | 概要 | 例 |
| --- | --- | --- | --- |
| 標準 | %c | 日時 | Sun Feb 9 16:24:39 2020 |
| 標準 | %x | 日付 | 02/09/20 |
| 標準 | %X | 時間 | 16:24:39 |
| カスタム | %y | 西暦 (2 桁) | 20 |
| カスタム | %Y | 西暦 (4 桁) | 2020 |
| カスタム | %b | 月名 (短縮形) | Feb |
| カスタム | %B | 月名 | Febrary |
| カスタム | %m | 月 (0 埋め。01 ~ 12) | 02 |
| カスタム | %d | 日 (0 埋め。01 ~ 31) | 09 |
| カスタム | %a | 曜日名 (短縮形) | Sun |
| カスタム | %A | 曜日名 | Sunday |
| カスタム | %w | 曜日 (0：日 ~ 6：土) | 0 |
| カスタム | %H | 時間 (24 時間。0 埋め。00 ~ 23) | 16 |
| カスタム | %U | 時間 (12 時間。0 埋め。01 ~ 12) | 04 |
| カスタム | %p | 午前 / 午後 | PM |
| カスタム | %M | 分 (0 埋め。00 ~ 59) | 24 |
| カスタム | %S | 秒 (0 埋め。00 ~ 59) | 39 |
| カスタム | %f | マイクロ秒 (0 埋め。000000 ~ 999999) | 000351 |
| カスタム | %z | タイムゾーン (オフセット値) | +0000 |
| カスタム | %Z | タイムゾーンの名前 | UTC |
| カスタム | %j | 年内の通算日 (001 ~ 366) | 040 |
| カスタム | %U | 年内の週番号 (週の始めは日曜。00 ~ 53) | 06 |
| カスタム | %W | 年内の週番号 (週の始めは月曜。00 ~ 53) | 05 |
| カスタム | %% | 文字 '%' | % |

dt_format.py
```py
import datetime
import locale


# setlocale メソッドで明示的にロケールを設定
locale.setlocale(locale.LC_ALL, 'ja_JP.UTF-8')

dt = datetime.datetime(2023, 9, 1, 15, 30, 35, 500)

print(dt)  ## 結果：2023-09-01 15:30:35.000500


# 単体でまとまった日付 / 時刻を表現できる
print(dt.strftime('%c'))  ## 結果：金  9/ 1 15:30:35 2023
print(dt.strftime('%x'))  ## 結果：2023/09/01
print(dt.strftime('%X'))  ## 結果：15時30分35秒


# 標準スタイルで対応できない場合は、指定子を組み合わせて独自の書式を組み合わせることもできる
print(dt.strftime('%Y 年 %m 月 %d 日 %I 時 %M 分'))  ## 結果：2023 年 09 月 01 日 03 時 30 分
```

setlocale メソッド
```py
setlocale(category, locale = None)

## category：設定する対象 (設定値は以下)
## locale：ロケール値 (地域値.文字コード)
```

引数 category の設定値
| 分類 | 概要 |
| --- | --- |
| LC_ALL | すべて |
| LC_CTYPE | 文字タイプ (string などに影響) |
| LC_TIME | 時刻 (strftime などに影響) |
| LC_NUMERIC | 数値 (format などに影響) |
| LC_MONETARY | 通貨 |
| LC_MESSAGE | メッセージ |

---

### *5.3.7. カレンダーを生成する*

cal_month.py
```py
import calendar


# 2023, 9, 1 = 年, 月, 1 日を表す文字幅
print(calendar.month(2023, 9, 1))

##    September 2023
## Mo Tu We Th Fr Sa Su
##              1  2  3
##  4  5  6  7  8  9 10
## 11 12 13 14 15 16 17
## 18 19 20 21 22 23 24
## 25 26 27 28 29 30


print(calendar.month(2023, 9, 5))

##               September 2023
##  Mon   Tue   Wed   Thu   Fri   Sat   Sun
##                            1     2     3
##    4     5     6     7     8     9    10
##   11    12    13    14    15    16    17
##   18    19    20    21    22    23    24
##   25    26    27    28    29    30


print(calendar.monthcalendar(2023,9))

## [[0, 0, 0, 0, 1, 2, 3], [4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30, 0]]
```