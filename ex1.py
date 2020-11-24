seri = '123456789'
result = []

# index go to the last element with total = 100 -> found num
def sum_to_100(index, num, total):
  if index == len(seri):
    if total == 100:
      result.append(num)

# Back track every possible result until get the right number total =100
  for i in range(index+1, len(seri)+1):
    sum_to_100(
      i,
      num+'+'+seri[index:i] if num else seri[index:i],
      total+int(seri[index:i]))
    sum_to_100(
      i,
      num+'-'+seri[index:i],
      total-int(seri[index:i])
                 )

sum_to_100(0, '', 0)

# print result from list
for i in result:
  print(i)