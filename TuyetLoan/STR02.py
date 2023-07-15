import string
def ChuanHoa(s):
    s = s.lower()
    s = s.strip("!,?...")
    s = s.title()
    print(s)
def main():
    case = int(input())
    for i in range(0, case):
        n = input()
        ChuanHoa(n)
if __name__ == "__main__":
    main()
