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


## 月は 1 ~ 12 であり、繰り上がり「2024 年 01 月」ということにはならない。
print(datetime.datetime(2023, 13, 1, 13, 30, 35, 500))


## combine メソッドで既存の date / time / tz オブジェクトを組み合わせて datetime オブジェクトの生成も可能
d = datetime.date(2023, 9, 1)
t = datetime.time(13, 30, 35, 500)
tz = datetime.timezone(datetime.timedelta(hours = 9))

print(datetime.datetime.combine(d, t, tz))