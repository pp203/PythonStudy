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