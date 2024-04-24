with open("popular-names.txt", "r") as file:
    diststr = set() #过滤重复元素
    for line in file:
        columns = line.strip().split("\t") #tab分割
        firstcol = columns[0]
        diststr.add(firstcol)
sortedstr = sorted(diststr)
for string in sortedstr:
    print(string)
#unix: cut -f1 popular-names.txt | sort | uniq