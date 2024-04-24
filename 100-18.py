with open("popular-names.txt", "r") as file:
    lines = []
    for line in file:
        columns = line.strip().split("\t")
        lines.append(columns)
sortedlines = sorted(lines, key=lambda x:int(x[2]), reverse=True) #从第三行开始

with open("100-18.txt", "w") as output:
    for line in sortedlines:
        output.write("\t".join(line) + "\n")
#unix: sort -k3nr 100-18.txt (第三列按照数值倒序)