import re
from tabnanny import check
def check_space(string):
     
    # counter
    count = 0
     
    # loop for search each index
    for i in range(0, len(string)):
         
        # Check each char
        # is blank or not
        if string[i] == " ":
            count += 1
         
    return count
a = []
n = int(input())
for i in range(n):
    my_str = input()
    result = re.sub(r'\s+', ' ', my_str)
    kq = check_space(result)
    a.append(kq)
print(*a, sep = '\n')
