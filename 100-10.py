with open("popular-names.txt", "r") as file:
    print(sum(1 for line in file)) #不涉及内容本身 仅遍历行数
#unix: wc -l popular-names.txt