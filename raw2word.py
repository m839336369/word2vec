import os

import jieba
import jieba.analyse

file_name = "word"
with open(f"corpus/{file_name}.txt", "w+", encoding="utf-8") as fenci:
    for path in os.listdir('txt'):
        with open(f"txt/{raw}.txt", "r", encoding="utf-8") as file:
            for line in file.readlines():
                # 精准模式
                text_cut:list = jieba.cut(line)
                fenci.write(" ".join(text_cut))

