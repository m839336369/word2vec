# 開啟第一個文件並讀取其內容
with open('C:/Users/Ether/PycharmProjects/pythonProject2/corpus/raw.txt', 'r', encoding="utf-8") as f1:
    content1 = f1.read()

# 開啟第二個文件並讀取其內容
with open('C:/Users/Ether/PycharmProjects/pythonProject2/tej/train.txt', 'r', encoding="utf-8") as f2:
    content2 = f2.read()

# 把兩個文件的內容寫入到新的文件
with open('C:/Users/Ether/PycharmProjects/pythonProject2/corpus/train.txt', 'w', encoding="utf-8") as outfile:
    outfile.write(content1)
    outfile.write(content2)