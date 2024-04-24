with open("popular-names.txt", "r") as file:
    n = int(input()) #后n行
    lines = file.readlines()
    total = len(lines)
    start = total - n  #从总数-n开始
    for i in range(start, total):
        print(lines[i].rstrip())
#unix: tail -n 数 popular-names.txt