import math
import csv

with open('data.csv', newline='') as f:
    reader=csv.reader(f)
    file_data = list(reader)
  
data = file_data[0]

def mean(data):
    total_marks = 0
    total_entries = len(data)

    for x in data:
        total_marks = total_marks + int(x)

    mean = total_marks/total_entries
    
    return mean
    
#squaring the v
sq = []
for number in data:
    a = int(number) - mean(data)
    a = a**2
    sq.append(a)
 
sum = 0
for i in sq:
    sum  += i
    
result = sum/ (len(data) -1)

sd = math.sqrt(result)
print(sd)
