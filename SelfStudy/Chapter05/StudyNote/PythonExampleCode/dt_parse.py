import datetime
from datetime import datetime

dt1 = datetime.strptime('2023/9/1 13:30:35', '%Y/%m/%d %H:%M:%S')
print(dt1)


## fromisoformat メソッド
### 年月日は必須であり、桁数もそれぞれ指定の桁で 0 埋めする必要がある
dt2 = datetime.fromisoformat('2023-09-01 13:30:35+09:00')
print(dt2)