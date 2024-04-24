with open("col1.txt", "r") as input1, open("col2.txt", "r") as input2, open("100-13.txt", "w") as output:
    for line1, line2 in zip(input1, input2):
        merge = line1.strip() + "\t" + line2.strip() + "\n"
        output.write(merge)
#unix: paste col1.txt col2.txt