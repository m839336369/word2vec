import os
import logging
import time

logging.basicConfig(filename='my_log.log', level=logging.INFO)


raw_segment_paths = list()
books = 'E:\\tcm_books'
[raw_segment_paths.append(os.path.join('E:\\txt', file)) for file in os.listdir('E:\\txt') if file.endswith('.txt')]
[raw_segment_paths.append(os.path.join('E:\\txt1', file)) for file in os.listdir('E:\\txt1') if file.endswith('.txt')]
[raw_segment_paths.append(os.path.join('E:\\txt2', file)) for file in os.listdir('E:\\txt2') if file.endswith('.txt')]

count = 0
start_time = time.time()
for path in raw_segment_paths:
    count += 1
    print(f'{time.time()-start_time:.4f}:{count}:{path}')
    slots = path.split()
    for slot in slots:
        if any(char.isdigit() for char in slot):
            continue
        with open(path, 'r', encoding='ansi') as segment:
            raw_segment = ''.join(segment.readlines())
            if '摘要：摘要' in raw_segment:
                raw_segment = raw_segment[raw_segment.index('摘要：摘要') + len('摘要：摘要') + 5:]
        with open(os.path.join(books, slot) + ".txt", 'a', encoding='ansi') as file:
            segment_name = '\n' + path[path.index(slot) + len(slot) + 2:].removesuffix('.txt') + '\n'
            file.write(segment_name)
            file.writelines(raw_segment)
        break
