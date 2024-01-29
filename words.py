import re

with open("./words/rawwords.txt", "r", encoding='ansi') as file:
    text = ''.join(file.readlines())
    regex = r".画  〔.〕  (.*)"
    matches = re.finditer(regex, text, re.MULTILINE)
    words = list()
    with open("./words/words.txt", "w", encoding='ansi') as out:
        for matchNum, match in enumerate(matches, start=1):
            for groupNum in range(0, len(match.groups())):
                try:
                    out.write(match.group(1) + '\n')
                except:
                    continue
