import re

def CHUANHOA(str):
    normalized = re.sub(r'\s+', ' ', str.strip())
    return normalized
def main():
    case = int(input())
    for i in (0, case):
        str = input()
        print(CHUANHOA(str))
if __name__ == "__main__":
    main()


