import re

content1 = '2019-01-01 12:00'
content2 = '2019-01-02 12:30'
content3 = '2019-01-03 13:00'
pattern = re.compile('(\d+)-(\d+)-(\d+)\s.*')
result_1 = re.match(pattern, content1)
result_2 = re.match(pattern, content2)
result_3 = re.match(pattern, content3)
# Year:2019  Month:01  Day:01
# Year:2019  Month:01  Day:02
# Year:2019  Month:01  Day:03
print('Year:' + result_1.group(1) + '  Month:' + result_1.group(2) + '  Day:' + result_1.group(3))
print('Year:' + result_2.group(1) + '  Month:' + result_2.group(2) + '  Day:' + result_2.group(3))
print('Year:' + result_3.group(1) + '  Month:' + result_3.group(2) + '  Day:' + result_3.group(3))



