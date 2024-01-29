from gensim import corpora
from gensim.models import KeyedVectors

file_name = "train"
sentences = []
with open(f"corpus/{file_name}.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        sentence = line.strip('\n').split(" ")
        sentences.append(sentence)
print(len(sentences))
# 生成词典
dictionary = corpora.Dictionary(sentences)
dictionary.filter_extremes(no_above=1.0, no_below=0)
dictionary.save_as_text(f"dict/{file_name}.txt")
total_vectors = KeyedVectors.load("vector/train.kv")
train_vectors = KeyedVectors(total_vectors.vector_size)
keys = list()
weights = list()
for id, token in dictionary.items():
    if token == '':
        continue
    keys.append(token)
    weights.append(total_vectors[token])
train_vectors.add_vectors(keys,weights)
train_vectors.save(f"vector/{file_name}.kv")
train_vectors.save_word2vec_format(f"vector/{file_name}.txt")
