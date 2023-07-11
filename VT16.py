a = input().split()
i = int(0)
dem = int(0)
while True:
    if int(a[i]) == 0:
        break
    if int(a[i]) < 0:
        print(a[i], end =' ')
        i+=1
        dem +=1
    else:
        i+=1
if dem == 0:
    print("NOT FOUND")

            
