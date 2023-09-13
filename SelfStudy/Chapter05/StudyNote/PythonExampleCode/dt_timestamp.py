import datetime
from datetime import datetime, timezone, date

dt = datetime.now(timezone.utc)
ts = dt.timestamp()

print(datetime.fromtimestamp(ts))

print(datetime.fromtimestamp(ts, timezone.utc))

print(date.fromtimestamp(ts))