import os

import jieba

jieba.set_dictionary("custom_dict.txt")
jieba.initialize()
files_path = list()
books = './txt'
[files_path.append(os.path.join(books, file)) for file in os.listdir(books) if file.endswith('.txt')]
sum = 0
with open("./corpus/train.txt", "w", encoding="utf-8") as output:
    for file_path in files_path:
        lines = list()
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file.readlines():
                line = line.strip()
                if line == "":
                    continue
                text_cut: list = jieba.lcut(line)
                lines.append(" ".join(text_cut) + "\n")
        output.writelines(lines)
        print(sum)
        sum += 1
print("e")
