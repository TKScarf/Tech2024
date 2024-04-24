with open("popular-names.txt", "r") as file, open("col1.txt", "w") as output1, open("col2.txt", "w") as output2:
    for line in file:
        columns = line.split("\t") #tab分割line
        output1.write(columns[0] + "\n")
        output2.write(columns[1] + "\n")
#unix: cut -f 1 popular-names.txt > col1_cut.txt
#unix: cut -f 2 popular-names.txt > col2_cut.txt