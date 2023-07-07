a, d, b = input().split()
a = float(a)
b = float(b)
match d:
    case '+':
        print ("{0:.2f}".format(a + b))
    case '-':
        print ("{0:.2f}".format(a-b))
    case '*':
        print ("{0:.2f}".format(a*b))
    case '/':
        if b != 0:
            print ("{0:.2f}".format(a/b))
        else:
            print ('Math Error')