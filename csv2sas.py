import pandas as pd

# 准备词汇表
with open("./words/med_word.txt", "r", encoding='utf-8') as words_file:
    words = list()
    for word in words_file.readlines():
        word = word.strip()
        if word == '证':
            continue
        words.append(word)


# 提取词汇
def get_words(input: str, prefixs=None) -> set:
    row_sas = set()
    if pd.isna(input):
        return row_sas
    for word in words:
        if input.find(word) != -1:
            row_sas.add(word)
        if prefixs is not None:
            for prefix in prefixs:
                if input.find(prefix + word) != -1:
                    row_sas.add(prefix + word)
    return row_sas


data = pd.read_csv("bingan.csv")
with open("sas.csv", 'w',encoding="utf-8") as sasFile:
    sasFile.write(f"symptom and sign,analysis\n")
    for index, row in data.iterrows():
        # [row_sas.add(item) for item in get_words(row['既往史'])]
        # [row_sas.add(item) for item in get_words(row['现病史'])]
        # [row_sas.add(item) for item in get_words(row['主诉'])]
        # [row_sas.add(item) for item in get_words(row['症状'])]
        # [row_sas.add(item) for item in get_words(row['舌诊'], ["舌", "苔", "舌苔", "舌色"])]
        # [row_sas.add(item) for item in get_words(row['脉诊'], ["脉"])]
        # [row_result.add(item) for item in get_words(row['辩证分析'])]
        sas = str(row['既往史']) + "," + str(row['现病史']) + "," + str(row['主诉']) + "," + str(row['症状']) + "," + str(get_words(row['舌诊'], ["舌", "苔", "舌苔", "舌色"])) + "," + "脉" + str(get_words(row['脉诊'], ["脉"])) + "&" + str(row['辩证分析']) + "\n"
        sasFile.write(sas)
    print("Success!")
