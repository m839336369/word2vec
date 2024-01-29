import multiprocessing
import os.path

import numpy as np
from gensim import corpora
from gensim.corpora import TextCorpus
from gensim.models import Word2Vec

get_dict = False
get_model = True
get_vector = False

sentences = []
file_name = "train"
with open(f"corpus/{file_name}.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        sentence = line.split(" ")
        sentences.append(sentence)
print(len(sentences))
if get_dict:
    # 生成词典
    dictionary = corpora.Dictionary(sentences)
    dictionary.filter_extremes(no_above=0.3)
    dictionary.save(f"dict/{file_name}.dict")
if get_model:
    # 创建Word2Vec模型
    if os.path.exists(f"model/{file_name}.model"):
        print("已存在模型，将继续训练。")
        model = Word2Vec.load(f"model/{file_name}.model")
    else:
        model = Word2Vec(corpus_file=f"corpus/{file_name}.txt", vector_size=500, window=5, min_count=0.3, sg=0, epochs=1,
                         workers=multiprocessing.cpu_count() * 2)
    for i in range(10):
        model.train(sentences, total_examples=len(sentences), epochs=10)
        model.save(f"model/{file_name}-{i}.model")
        model.wv.save(f"vector/{file_name}.kv")
        model.wv.save_word2vec_format(f"vector/{file_name}.txt")
