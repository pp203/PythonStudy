# Chapter 03. 演算子

* 演算子：与えられた変数やリテラルに対して、あらかじめ決められた処理を行うための記号  
* 非演算子：演算子によって処理される変数やリテラルのこと

## 3.1. 算術演算子
代数演算子ともいう。

| 演算子 | 概要 | 例 |
| --- | --- | --- |
| + | 加算 | 2 + 3 (= 5)
| - | 減算 | 3 - 2 (= 1)
| * | 乗算 | 2 * 3 (= 6)
| / | 除算 | 7 / 3 (= 2.33...)
| // | 除算 (切り捨て) | 7 // 3 (= 2)
| % | 剰余 (割った余り) | 10 % 3 (= 1)

### *3.1.1. データ型によって挙動は変化する*

文字列同士の「+」演算は、加算ではなく **連結** とみなす。

alg_op01.py
```py
print('10' + '3')

print('こんにちは' + '赤ちゃん')
```

実行結果
```
$ python3 alg_op01.py

103
こんにちは赤ちゃん
```

「*」演算もできる。  
「文字列 * n」=「文字列を n 回繰り返した文字列」

alg_op02.py
```py
print('こんにちは' * 3)
```

実行結果
```
$ python3 alg_op02.py 

こんにちはこんにちはこんにちは
```

→ <ins>演算子の役割はオペランドのデータ型によって変化する


### *3.1.2. 文字列と数値との演算*

<ins>Python では数値と文字列の組み合わせはできない。

alg_op_error01.py
```py
print(15 + '30')
```

実行結果
```
$ python3 alg_op_error01.py 

Traceback (most recent call last):
  File "/Users/seinay/VSCode/GitHub/PythonStudy/SelfStudy/Chapter03/StudyNote/alg_op_error01.py", line 1, in <module>
    print(15 + '30')
          ~~~^~~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

「int」や「str」などの関数で型を変換することで演算可能。

alg_op03.py
```py
print(15 + int('30'))

print(str(15) + '30')
```

実行結果
```
$ python3 alg_op03.py 

45
1530
```

### *3.1.3. 除算を表す演算子「/」「//」*
* 「/」= 一般的な除算。int 同士の除算でも float になる可能性がある。
* 「//」= float 同士の除算でも整数を返す。

alg_op04.py
```py
print(5 / 3)
print(5 // 3)
```

実行結果
```
$ python3 alg_op04.py 

1.6666666666666667
1
```

divmod  
整数部の商と剰余をまとめて表示できる

alg_op05.py
```py
print(divmod(5,3))  
# 5 / 3 して「1」が商で、「2」が余りになる。
```

実行結果
```
$ python3 alg_op05.py 

(1, 2)
```

### *3.1.4. 浮動小数点数の演算には要注意*
浮動小数点数を含んだ演算子の場合、想定とは違う結果が表示されることがある。  
Python が内部的に数値を 10 進数ではなく、2 進数で演算してしまっているから。  

alg_op06.py
```py
print(0.2 * 3)

print(0.2 * 3 == 0.6)
```

実行結果
```
$ python3 alg_op06.py

0.6000000000000001
False
```

上記の問題を解決するには、 Decimal 型を使う必要がある。  
**Decimal 型**：10 進数の浮動小数点数をサポートする型。
* 「decimal.Decila(数値)」で生成できる
* int/float 型と同じく、「+」「-」「==」の演算子を利用できる
* Decimal の値は、文字列リテラルとして指定することが原則

alg_op07.py
```py
import decimal

d1 = decimal.Decimal('0.2')
d2 = decimal.Decimal('3')
d3 = decimal.Decimal('0.6')

print(d1 * d2)
print(d1 * d2 == d3)
```

実行結果
```
$ python3 alg_op07.py

0.6
True
```

## 3.2. 代入演算子
左側で指定した変数に対して、右側の値を代入するるための演算子  
**複合代入演算子**：算術演算子やビット演算しなどを合わせた機能のこと

| 演算子 | 概要 | 例 |
| --- | --- | --- |
| = | 変数などに値を代入 | x = 10 |
| += | 左辺と右辺を合算した結果を左辺に代入 | x = 5; x += 2 (x = 7) |
| -= | 左辺と右辺を減算した結果を左辺に代入 | x = 5; x -= 2 (x = 3) |
| *= | 左辺と右辺を乗算した結果を左辺に代入 | x = 5; x *= 2 (x = 10) |
| /= | 左辺を右辺で除算した結果を左辺に代入 | x = 5; x /= 2 (x = 2.5) |
| //= | 左辺を右辺で除算した結果 (整数) を左辺に代入 | x = 5; x //= 2 (x = 2) |
| %= | 左辺を右辺で除算した余りを左辺に代入 | x = 5; x %= 2 (x = 1) ※ 整数までで割り算をするので余りが 1 になる |
| **= | 左辺を右辺でべき乗した結果を左辺に代入 | x = 5; x **= 2 (x = 25) |
| &= | 左辺と右辺をビット論理積した結果を左辺に代入 | x = 10; x &= 2 (x =2) |
| ^= | 左辺と右辺をビット排他論理和した結果を左辺に代入 | x = 10; x ^= 2 (x = 8) |
| \|= | 左辺と右辺をビット論理和した結果を左辺に代入 | x = 10; x \|= 2 (x = 10) |
| >>= | 左辺を右辺の値だけ右シフトした結果を左辺に代入 | x = 10; x >>= 2 (x = 2) |
| <<= | 左辺を右辺の値だけ左シフトした結果を左辺に代入 | x = 10; x <<= 2 (x = 40)

**ビット論理積**
* AND
* 2 進数で見た時に 2 つの値が「1」である時のみ「1」と表示する。
* 片方だけ「1」の場合は、「0」と表示する。
* 両方とも「0」の場合も、「0」と表示する。

10 &= 2
10 を 2 進数で表すと、「1010」。  
2 を 2 進数で表すと、「10」。  
両方の値を足した時、両方とも「1」である場合は「1」、片方でも「0」の場合は「0」とする。

0010  
1010

→ 0010 = 2

**ビット論理和**
* OR
* 2 進数で見た時に 片方でも「1」である時、「1」と表示する。
* 両方とも「0」である時は「0」

0010  
1010

→ 1010 = 10

**ビット排他論理和**
* 2 進数で見た時に 2 つの値が「1」または「0」である時、「1」と表示する。
* 両方とも「0」だったり、「1」である時は「0」と表示する。

0010  
1010

→ 1000 = 8

**右シフト**  
「10」を 2 進数とした時、全ビットを右にずらす。

10 >>= 2  
1010 (00001010)  
0010 (00000010)

**左シフト**  
「10」を 2 進数とした時、全ビットを左にずらす。

10 <<= 2  
1010 (00001010)  
101000 (00101000)

### *3.2.1. 数値のインクリメント/デクリメント*
* インクリメント演算子：与えられたオペランドに対して 1 を加算すること
* デクリメント演算子：与えられたオペランドに対して 1 を減算すること
* ただし、「++」「--」演算子は <ins>Python には存在しない。
* その代わり、「+=」「-=」演算子を利用する。

inc_op01.py
```py
# i++ ←→ i = i + 1
# i-- ←→ i = i - 1

i = 1

i += 1
print(i)

i -= 1
print(i)
```

実行結果
```
$ python3 inc_op01.py

2
1
```

5 ずつ増やす/減らすこともできる
```
i += 5
i -= 5
```

### *3.2.2. 「=」演算子による代入は参照の引き渡し*
* 参照/識別値：格納場所を表す情報のこと
* 変数には値の格納場所を表す情報を格納する。
* → 実際の値は、別の場所に格納されているということ。

ref_id.py
```py
num1 = 10
num2 = num1

print(id(num1))
print(id(num2))
```

実行結果
```
$ python3 ref_id.py 

4309034152
4309034152
```

### *3.2.3. ミュータブルとイミュータブル*
* ミュータブル：変更可能な型。オブジェクトをそのまま中身だけを変更できる。
* イミュータブル：変更不可な型。一度作成したオブジェクトの中身を書き換えることはできない。値を変更するにはオブジェクトそのものを入れ替えなければならない。

assign01.py
```py
# ミュータブル型
data1 = [1,2,3]
data2 = data1
data1[0] = 100

print(data1)
print(data2)

# イミュータブル型
x = 1
y = x
x += 10

print(x)
print(y)
```

実行結果
```
$ python3 assign01.py 

[100, 2, 3]
[100, 2, 3]
11
1
```

ミュータブルな型であっても、値そのものを差し替えた場合は異なるオブジェクトとなる。

assign02.py
```py
data1 = [1,2,3]
data2 = data1
data1 = [4,5,6]  # 別のオブジェクトで置き換え

print(data1)
print(data2)
```

実行結果
```
$ python3 assign02.py 

[4, 5, 6]
[1, 2, 3]
```

### *3.2.4. アンパック代入*
リスト/辞書などを分解し、配下の要素を個々の変数に分解するための構文  
左辺に要素の数だけ変数を列挙する

右辺のリッストがここの要素に分解され、それぞれ対応する変数 a - e に代入される  

unpack01.py
```py
data = [1,2,3,4,5]
a,b,c,d,e = data

print(a)
print(b)
print(c)
print(d)
print(e)
```

実行結果
```
$ python unpack01.py

1
2
3
4
5
```

上記の場合、左辺の変数と右辺 (リスト) の要素数は一致していなければいけない。  
以下の場合はエラーが出力される。

unpack_error01.py
```py
data = [1,2,3,4,5]
a,b,c = data  # リスト要素が変数よりも多い
```

実行結果
```
$ python unpack_error01.py

Traceback (most recent call last):
  File "/Users/seinay/VSCode/GitHub/PythonStudy/SelfStudy/Chapter02/StudyNote/unpack_error01.py", line 2, in <module>
    a,b,c = data  # リスト要素が変数よりも多い
    ^^^^^
ValueError: too many values to unpack (expected 3)
```

unpack_error02.py
```py
data = [1,2,3,4,5]
a,b,c,d,e,f = data  # リスト要素が変数よりも少ない
```

実行結果
```
$ python3 unpack_error02.py

Traceback (most recent call last):
  File "/Users/seinay/VSCode/GitHub/PythonStudy/SelfStudy/Chapter02/StudyNote/unpack_error02.py", line 2, in <module>
    a,b,c,d,e,f = data  # リスト要素が変数よりも少ない
    ^^^^^^^^^^^
ValueError: not enough values to unpack (expected 6, got 5)
```

### 残りの要素をまとめて代入する
変数に * を付与することで個々の変数に分解されなかった残りの要素をまとめてリストとして切り出すことができる

unpack02.py
```py
data = [1,2,3,4,5]
m,n,*o = data

print(m)
print(n)
print(0)

r,*s,t = data

print(r)
print(s)
print(t)

*x,y,z, = data

print(x)
print(y)
print(z)
```

実行結果
```
$  python3 unpack02.py 

1
2
0
1
[2, 3, 4]
5
[1, 2, 3]
4
5
```

\* 付き変数で該当する要素がない時、空のリストが生成される

unpack03.py
```py
data = [1,2]
a,b,*c = data

print(c)
```

実行結果
```
$ python3 unpack03.py 

[]
```

### 一部の要素を切り捨てる
* _ を利用してアンパック代入で一部の要素を除外することができる
* ただし、変数 '_' に代入しているというだけなので最後の値が表示される

unpack04.py
```py
data = [1,2,3,4,5]
a,_,b,_,c = data

print(a)
print(b)
print(c)
print(_)
```

実行結果
```
$ python3 unpack04.py

1
3
5
4
```

### 入れ子のリストをアンパックする

unpack05.py
```py
data = [1,2,[31,32,33]]

a,b,c = data

print(a)
print(b)
print(c)

x,y, (z1, z2, z3) = data

print(x)
print(y)
print(z1)
print(z2)
print(z3)
```

実行結果
```
$ python3 unpack05.py 

1
2
[31, 32, 33]
1
2
31
32
33
```

---
### 変数のスワッピング　　
アンパック代入を利用して、変数の値を入れ替えることもできる  
アンパック代入を利用しない場合は、いずれかの変数を一旦別の変数に対比させる必要がある。

unpack06.py
```py
x = 15
y = 38
x,y = y,x

print(x,y)
```

実行結果
```
$ python unpack06.py 

38 15
```

### *3.2.5. 新しい代入演算子「:=」*

他の言語では以下は正しいコードだが、Python ではエラーが出力される。  
これは、Python の代入は式ではなく文だから。  
なので「x = 20」という文を 10 で割ることができないから。

substi_op_error.py
```py
y = (x = 20) / 10

print(y)
```

実行結果
```
$ python3 substi_op_error.py 

  File "/Users/seinay/VSCode/GitHub/PythonStudy/SelfStudy/Chapter03/StudyNote/substi_op_error.py", line 1
    y = (x = 20) / 10
         ^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

なので、Python の場合は以下となる。

substi_op.py
```py
y = (x := 20) / 10

print(y)
```

実行結果
```
$ python3 substi_op.py 

2.0
```

## 3.3. 比較演算子
左辺と右辺の値を比較して、その結果を True/False で返すもの  
「関係演算子」とも言う。

| 演算子 | 概要 | 例 |
| --- | --- | --- |
| < | 左辺が右辺より小さい場合に True | 5 < 10 (True) |
| > | 左辺が右辺より大きい場合に True | 5 > 10 (False) |
| == | 左辺と右辺の値が等しい場合に True | 5 == 5 (True) |
| <= | 左辺が右辺以下の場合 True | 5 <= 10 (True) |
| >= | 左辺が右辺以上の場合 True | 5 >= 10 (False) |
| != | 左辺と右辺の値が等しくない場合に True | 5 ~= 10 (True) |
| is [not] | 左辺と右辺のオブジェクトが等しい場合に True | [1, 2] is [1, 2] (False) |
| [not] in | 左辺が右辺に含まれている場合に True | 3 in [1, 2, 3] (True) |

is [not] について  
* 同じ値でも別のオブジェクトを生成しているので上記の場合 False となる。

compare_op01.py
```py
x = [1, 2]
y = [1, 2]

print(id(x))
print(id(y))

print(x is y)


a = 3
b = a

print(a is b)
```

実行結果
```
$ python compare_op01.py

4304164224
4304264000
False
True
```


### *3.3.1. 異なる型での比較*
* 「<」や「>」などの大小比較の場合、異なる型での比較はできない。
* 「==」や「!=」演算子の場合、異なる方での比較はできる。ただし、基本的には False を返す。
* 数値同士の場合は例外。int 型と float 型とは数値として正しく等価/大小を判定できる。

compare_op02.py
```py
print(1 == '1')
print(False == None)

print(1 == 1.0)
print(1.5 < 1)
```

実行結果
```
$ python3 compare_op02.py 

False
False
True
False
```

* 文字列/数値同士などの同じデータ型であっても意図しないデータ型での比較は意図しない結果となることもある。
* 例01：「15 < 131」の場合、数値の場合は True であるが、文字列の場合は False となる。
* 例02：「'15' < '131'」の場合、str 型として認識するので、先頭の「1」は同じ、次の「5 > 3」を比較するので答えは False と確実な答えが出る。

compare_op03.py
```py
print(15 < 131)
print('15' < '131')
```

実行結果
```
$ python3 compare_op03.py 

True
False
```

---
### *3.3.2. リストの比較*
* リスト同士の比較もできる
* 先頭から要素を比較して、最初に異なる要素が見つかった場合に、その大小でリスト全体の大小を決定する

[1,2,2,3] vs. [1,2,3]  
* 最初の [1,2,] までは同じなのでスキップ
* 3 番目の [2] と [3] を比較する
* 2 < 3 なので、[1,2,2,3] < [1,2,3] となる。
* メモ：存在する要素が全て等しい場合は、要素数が少ないほうが小さいとみなされる。
* メモ：「辞書」については大小比較はできない。

compare_op04.py
```py
data1 = [1, 2, 3]
data2 = [1, 5]
data3 = [1, 2]

print(data1 < data2)
print(data1 < data3)
```

実行結果
```
$ python3 compare_op04.py 

True
False
```

---
### *3.3.3. 浮動小数点数の比較*
(1) Decimal 型  
(2) 丸め単位による比較  
* 定義 EPSILON は誤差の許容範囲を表す。
* 「計算機イプシロン」、「丸め単位」とも呼ばれる。

「EPSILON = 0.0001」 の場合
* 浮動小数点数の誤差の許容範囲を 0.0001 とするということ
* 以下の場合、0.2 * 3 は 0.6 と全く等しくはならない
* なので x - y としたときの誤差をどれだけ許容するかという話
* < EPSILON なので「0.00001 未満」ということ
* <= EPSILON とかもできる

compare_op05.py
```py
EPSILON = 0.00001
x = 0.2 * 3
y = 0.6

print(abs(x - y) < EPSILON)
```

実行結果
```
$ python compare_op05.py 

True
```

(3) isclose 関数
* 厳密に等しくなくとも近似であれば True を返す
* 許容誤差は rel_tol/abs_tol で変更も可能。
  * rel_tol: 相対誤差。2 つの値のうち、絶対値の大きい値に対する割合で指定。
  * abs_tol: 絶対誤差。許容する誤差を絶対値で指定。


実行結果
```
$ python compare_op05.py 

True
```

## 3.4. 論理演算子
* 複数の条件式を論理的に結合してその結果を True/False で表す。

| 演算子 | 概要 | 例 |
| --- | --- | --- |
| and | 論理積。左右の式がともに True の場合に True | x and y (False) |
| or | 論理和。左右の式いずれかが True の場合に True | x or y (True) |
| ^ | 排他的論理和。左右の指揮いずれかが True で、尚且つ、ともに True 出ない場合に True | x ^ y (True) |
| not | 否定。式が True の場合は False、False の場合は True | not x (False) |

論理演算子による評価結果
| 左式 | 右式 | and | or | ^ |
| --- | --- | --- | --- | --- |
| True | True | True | True | False |
| True | False | False | True | True |
| False | True | False | True | True |
| False | False | False | False | False |


### *3.4.1. ショートカット演算 (短絡演算)*
* 「ある条件のもとでは、左式だけが評価されて右式だけ評価されない」場合のこと
* 左式が結果を出した時に、右式の結果が既に関係ない場合は右式の評価はスキップされるということ

例：論理演算子 (and) である場合  
* i = 10
* i == 5 and j == 100
* → 「i == 5」が False なので、「j == 100」が True/False 関係なく結果は False になる

例：論理和演算子 (or) である場合
* i = 10
* i == 5 or j == 100
* → 「i = 10」が True なので、「j == 100」が True/False 関係なく結果は True になる

shortcut01.py の場合、同じ意味になる。  
1) 条件式 (「x != 2」)が True である場合、メッセージを表示するという意味。
2) 左式が False である場合のみ、メッセージを表示するという意味。

shortcut01.py
```py
x = 1

if x != 2:
    print('実行されました。')

x == 2 or print('実行されました。')
```

実行結果
```
$ python3 shortcut01.py 

実行されました。
実行されました。
```

Python の論理演算子
* 左式/右式と最後に評価された値を返す特徴がある。
* → 左式で評価された場合には左式の値が、出なければ右式の値が返される

例：hoge 関数が値を返さない場合、または False であるばあ、既定値として 「default」を返す  
```
print(hoge() or 'default')
```

### *3.4.2. 比較演算の連結*
50 ~ 100 の範囲を表現するためには以下のように Python では表す。

```
50 <= x <= 100
```

## 3.5. ビット演算子

## 3.6. 演算子の優先順位と結合則
