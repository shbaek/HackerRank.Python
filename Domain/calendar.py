import datetime

a = input().strip().split(' ')
result = datetime.date(int(a[2]), int(a[0]), int(a[1]))
print(result.strftime("%A").upper())
