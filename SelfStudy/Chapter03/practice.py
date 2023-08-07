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




