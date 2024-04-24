from collections import Counter

with open("popular-names.txt", "r") as file:
    stringcount = Counter()
    for line in file:
        columns = line.strip().split("\t")
        firstcol = columns[0]
        stringcount[firstcol] = stringcount[firstcol] + 1
sortedstr = sorted(stringcount.items(), key=lambda x: x[1], reverse=True) #Counter

with open("100-19.txt", "w") as output:
    for string, frequency in sortedstr:
        output.write(f"{string}: {frequency}\n")
#unix: cut -d: -f1 100-19.txt