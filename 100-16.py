with open("popular-names.txt", "r") as file:
    lines = file.readlines()
n = int(input()) #N份
total = len(lines)
perchunk = total // n #每份的最大数量

for i in range(n):
    start = i * perchunk
    stop = (i + 1) * perchunk
    if i == n - 1: #未满最大数量
        end = total
    chunk = lines[start:stop]
    outputpath = f"00{i + 1}.txt"
    with open(outputpath, "w") as outputfile:
        for line in chunk:
            outputfile.write(line)
#unix: split -n 数 -d --additional-suffix=.txt popular-names.txt part
#-l参考https://qiita.com/tanaka-qtaro/items/ff08798baeb6411b030b