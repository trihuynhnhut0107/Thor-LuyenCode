m = int(input())
hour = m // 3600
minute = (m - hour * 3600) // 60
second = m - hour * 3600 - minute * 60
if hour < 10 and hour >= 0:
    print(f"0{hour}:", end="")
else:
    print(f"{hour}:", end="")
if minute < 10 and minute >= 0:
    print(f"0{minute}:", end="")
else:
    print(f"{minute}:", end="")
if second < 10 and second >= 0:
    print(f"0{second}", end="")
else:
    print(f"{second}", end="")
