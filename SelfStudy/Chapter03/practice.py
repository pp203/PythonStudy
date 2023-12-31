# 練習問題 3.1

## 1. Python で以下の演算の実行結果を答えよ。エラーとなる場合は、エラーと記入せよ。
### 1-1. '4' + '5'

#### 45?
#### >>> print('4' + '5')
#### 45

### 1-2. 2 ** 4

#### エラー？
#### >>> print(2 ** 4)
#### 16  → 2 の 4 乗ということ。

### 1-3. 10 // 6

#### 1?
#### >>> print(10 // 6)
#### 1

### 1-4. 2.0 / 0

#### 0?
#### >>> print(2.0 / 0)
#### Traceback (most recent call last):
####   File "<stdin>", line 1, in <module>
#### ZeroDivisionError: float division by zero

### 1-5. 10 % 4

#### 2?
#### >>> print(10 % 4)
#### 2


## 2. Python では「0.1 * 3 == 0.3」の結果が True にならない場合がある。その理由と対処方法を述べよ。

### 理由：0.1 を 2 進数で読んでしまうから？
### 対処：

### import decimal
### a = decimal.Decimal('0.1')
### print(a * 3)


# この章の理解度をチェック
## 1. 空欄を埋めよ。
### 算術演算子 | +、-、*、**、/、//、% など
### 代入演算子 | =、:=、複合代入演算子 (+=、-=、*=、/=)
### 比較演算子 | >、<、==、>=、<=、!= など
### 論理演算子 | and、or、not など
### ビット演算子 | 

## 2. 以下の代理演算子の値を答えよ
x = 50
y = x
x -= 10 # x = 40, y = 50

data1 = [10,20,30]
data2 = data1
data[1] = 15 # data1 = [10,15,30], data2 = [10,15,30]

## 3. 

## 4. 
### 4-1. 変数 i を 2 減らす
i -= 2

### 4-2. decimal 型の変数 d (値は 0.5) を生成
d = decimal.Decimal('0.5')

### 4-3. リストの内容を変数に分割して代入
list = [2,4,6,8,10]
x,y,*z = list

### 4-4. m、n の変数の中身を入れ替え
n,m = m,n

### 4-5. 条件式「x が 10 以上 50 未満」を論理演算子を使わずに表す
10 <= x < 50
