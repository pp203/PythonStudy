import unicodedata

data = 'WINGS プロジェクト 2020'
count = 0

for i in data:
    if unicodedata.east_asian_width(i) in 'FWA':
        count += 2
    else:
        count += 1

print(count)