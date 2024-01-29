import os  # 用于获取目标文件所在路径
from win32com import client as wc  # 导入模块

root = "D:\\电子书"  # 文件夹绝对路径
files = []
for file in os.listdir(root):
    if file.endswith(".doc"):  # 排除文件夹内的其它干扰文件，只获取".doc"后缀的word文件
        path = root + f"\\{file}"
        files.append(path)
print(files)
word = wc.Dispatch("Word.Application")  # 打开word应用程序
print("2")
for file in files:
    print(file)
    doc = word.Documents.Open(file)  # 打开word文件
    doc.SaveAs("{}x".format(file), 12)  # 另存为后缀为".docx"的文件，其中参数12指docx文件
    print(file + "结束")
    # doc.Close() #关闭原来word文件
word.Quit()
print("完成！")
