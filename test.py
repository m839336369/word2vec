import jieba
# 导入词汇
jieba.set_dictionary("custom_dict.txt")
# jieba.set_dictionary("words/jieba.txt")
jieba.initialize()  # 手动初始化（可选）
# 获取内存中的词典
word_dict = jieba.dt.FREQ
print(jieba.dt.total)
# 将词典信息保存到文件
output_file_path = 'jieba_dictionary.txt'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for word, freq in word_dict.items():
        output_file.write(f"{word} {freq}\n")
print(f"jieba dictionary has been exported to {output_file_path}")