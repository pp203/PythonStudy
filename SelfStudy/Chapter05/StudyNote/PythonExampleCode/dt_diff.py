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