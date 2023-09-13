import datetime
from datetime import datetime, timedelta

dt = datetime(2023, 9, 1, 15, 30, 35, 500)
dt_p = dt + timedelta(days = 10, hours = 20)
dt_m = dt - timedelta(weeks = 3)

print(dt)
print(dt_p)
print(dt_m)