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
print(datetime.datetime.utcnow())  ## あくまで値が UTC 時刻なので、内部的には native 型 (tz を持たない)
print(datetime.datetime.now(datetime.timezone.utc))  ## aware 型の UTC 時刻


