import os
import re

import docx

root = "D:\\tes"
index = 0
is_paragraph = False
with open("data/raw.txt", "w+", encoding="utf-8") as raw_txt:
    for file in os.listdir(root):
        if not file.endswith(".docx"):
            continue
        # 打开.doc文件
        doc = docx.Document(os.path.join(root, file))
        index += 1
        print(f"{index}:{file}")
        # 逐段读取文本并输出
        for paragraph in doc.paragraphs:
            if is_paragraph:
                raw = re.sub(r'[^\u4e00-\u9fa5，。！【】\n]+', '', paragraph.text)
                raw_txt.write(raw)
            else:
                # 使用正则表达式匹配中文句子
                sentences = re.findall(r'[^。！？]+[。！？]', paragraph.text)
                for sentence in sentences:
                    raw = re.sub(r'[^\u4e00-\u9fa5，。！【】]+', '', sentence.strip())
                    if not raw:
                        continue
                    raw_txt.write(raw + "\n")
