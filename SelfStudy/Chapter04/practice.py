# 練習問題 4.1.
## 1. 条件分岐構文を使って、90 点以上であれば「A」、70 点以上 90 点未満であれば「B」、50 点以上 70 点未満であれば「C」、50 点未満であれば「D」と表示するコードを作成せよ。点数は 75 点。

grade = 75

if grade >= 90:
    print('A')
elif 70 <= grade < 90:
    print('B')
elif 50 <= grade < 70:
    print('C')
else:
    print('D')


# 練習問題 4.2.
# 1. for 命令を利用して九九表を作成せよ

# data1 = [1,2,3,4,5,6,7,8,9]
# data2 = [i * 2 for i in data1]
# data3 = [i * 3 for i in data1]
# data4 = [i * 4 for i in data1]
# data5 = [i * 5 for i in data1]
# data6 = [i * 6 for i in data1]
# data7 = [i * 7 for i in data1]
# data8 = [i * 8 for i in data1]
# data9 = [i * 9 for i in data1]

# print(data1)
# print(data2)
# print(data3)
# print(data4)
# print(data5)
# print(data6)
# print(data7)
# print(data8)
# print(data9)

for i in range(1,10):
    for j in range(1,10):
        a = i * j
        print(a, end=" ")
    print()


# 練習問題 4.3.
## 1. 現在のループをスキップする命令、現在のループを脱出する命令を答えよ。
### 現在のループをスキップする命令：contiune
### 現在のループを脱出する命令：break

## 2. リスト 4.16 を while 命令文に書き換えよ。
sum = 0
i = 0

while i < 101:
    if i % 2 != 0:
        i += 1
        continue
    sum += i
    i += 1

print(sum)


# この章の理解度チェック
## 1. 空欄を埋めよ。
### 複合文は、配下に複数の文を持ち、それらを実行するかどうかを決めるための文です。
### 条件分岐を表す <if 文> をはじめ、繰り返しを表す <while 文>、for なども複合文です。
### 複合文は、1 つ以上の <節> から構成されます。
### <節> は、さらに、<ヘッダー> と <ブロック> とに分類できます。
### <ヘッダー> は配下の <ブロック> をどのように実行するのかを決める情報を表します。
### 末尾は <コロン> で終えます。
### <ブロック> は <コロン> によって表します。
### <コロン> は、一般的には半角スペース 4 個とします。

## 2. コードを作成せよ。
### 2-1. リスト data の内容を順に出力する。

data = [1,2,3,4,5]

for i in data:
    print(i, end = " ")

### 2-2. 1 ~ 100 の値を順に出力する。

for i in range(0,101):
    print(i, end = " ")

### 2-3. 数値が格納されたリスト data1 の内容を全て 10 倍した結果を変数 data2 に格納する

data1 = [1,2,3,4,5]
data2 = [i * 10 for i in data1]

print(data2)

### 2-4. 数値が格納されたリスト data から値 0 以上のものだけを取り出し、合計値を求める

data = [-1,0,5,6]
result = sum([i for i in data if i >= 0])

print(result)

### 2-5. 変数 num が 10 以上 50 未満の時、num の値を表示する

num = [5,9,13,60]

for i in num:
    if 10 <= i < 50:
        print(i)

## 3. コード内容：ユーザーから入力された数値を受け取ってその値を 1.5 倍にする。因数に数値以外が渡された時はエラーメッセージを表示した上でループする。このコードを作成せよ。

while True:
    try:
        num = input('数値を入力')
        print('1.5 倍にすると...', float(num) * 1.5)
    except ValueError:
        print('入力エラー')
    else:
        break

## 4. for 命令と continue 命令を使い、100 ~ 200 の範囲

