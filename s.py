import os
import chardet
sum=0
def detect_encoding(file_path):
    # 读取文件内容进行编码检测
    with open(file_path, 'rb') as file:
        detector = chardet.universaldetector.UniversalDetector()
        for line in file:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        result = detector.result

    return result['encoding']


def convert_to_utf8(file_path, original_encoding):
    global sum
    sum += 1
    print(sum)
    try:
        try:
            # 读取文件内容，使用原始编码
            with open(file_path, 'r', encoding='ansi') as file:
                content = file.read()
        except:
            # 读取文件内容，使用原始编码
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
        # 将内容以 UTF-8 格式保存
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Converted {file_path} to UTF-8")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")


def convert_folder_to_utf8(folder_path):
    # 遍历文件夹下的所有文件
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # 判断是否为文本文件
        if filename.endswith('.txt'):
            # 自动检测文件编码
            detected_encoding = detect_encoding(file_path)
            if detected_encoding:
                print(f"{filename} has detected encoding: {detected_encoding}")
                convert_to_utf8(file_path, detected_encoding)
            else:
                print(f"Cannot detect encoding for {filename}")

    print("Conversion completed.")


# 指定文件夹路径
folder_path = './txt'

# 执行转换
convert_folder_to_utf8(folder_path)
