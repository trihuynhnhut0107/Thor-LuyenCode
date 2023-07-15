from collections import defaultdict

str = input()
dic_str = defaultdict(int)
str = str.lower()
for i in str:
    if (i >= 'a' and i <= 'z') or (i >= '0' and i <= '9'):
        dic_str[i] += 1
sorted_items = sorted(dic_str.items(), key=lambda x: x[0])
for key, value in sorted_items:
    if value != 0:
        print(key, value)


