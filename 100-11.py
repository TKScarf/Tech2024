with open("popular-names.txt", "r") as file, open("100-11.txt", "w") as output:
    for line in file:
        line = line.replace('\t', ' ') #tab替换为空格
        output.write(line)
#unix: sed 's/\t/ /g' popular-names.txt > popular-names-space-sed.txt