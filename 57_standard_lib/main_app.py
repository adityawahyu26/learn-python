# standard library di dalam python

# library datetime
import datetime

today = datetime.datetime.now()
year = today.year
month = today.month
day = today.day
hari = today.strftime('%A')

print(f"hari ini adalah hari {hari}, tanggal {day}-{month}-{year}")

# library Counter
from collections import Counter

data = [1,3,4,2,1,2,3,5,6,3,7,8,3,2,4,6,5,2,4,7,3,4,1,5,6,3]
data_count = Counter(data)
print(f"ada berapa angka 3 = {data_count[3]}")
print(f"ada berapa angka 2 = {data_count[2]}")

# library io / input output
import io
data = io.open('hello.txt','r')
print(data.read())



