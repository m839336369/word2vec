import os
import re
import easyocr
import pdfplumber
from matplotlib import pyplot as plt

reader = easyocr.Reader(['ch_sim','en'], gpu = False)
for file_name in os.listdir("D:\\中医图书库"):
    if not file_name.endswith(".pdf"):
        continue
    file_name = file_name.removesuffix(".pdf")
    with open(f"txt/{file_name}.txt","w+",encoding="utf-8") as output:
        print(file_name)
        try:
            with pdfplumber.open(f"D:\\中医图书库\\{file_name}.pdf") as pdf:
                for page in pdf.pages:
                    page.to_image(width=1920).save("a.jpg")
                    result = reader.readtext("a.jpg")
                    result = re.sub(r'[^(。.!?)]\n', '', result)
                    output.write(result)
        except Exception as e:
            print(e)
