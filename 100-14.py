with open("popular-names.txt", "r") as file:
    n = int(input()) #前n行
    for i, line in enumerate(file):
        if i < n:
            print(line.rstrip())
#unix: head -n 数 popular-names.txt