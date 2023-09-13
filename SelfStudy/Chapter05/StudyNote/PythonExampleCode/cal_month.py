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