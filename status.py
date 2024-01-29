import time

import gensim.similarities
import numpy as np
import matplotlib.pyplot as plt

from gensim.models import Word2Vec, KeyedVectors

file_name = "tcm_words_vector"
# model = Word2Vec.load(f"model/{file_name}.model")
word_vectors = KeyedVectors.load("vector/tcm_words_vector.kv")

# 使用Gensim加载词向量
# word_vectors = KeyedVectors.load_word2vec_format(f"vector/{file_name}.txt")

# # 选择要可视化的单词
# target_words = ["虚热", "虚寒", "热", "寒"]  # 请替换为你想要可视化的单词
#
# # 创建子图
# num_words = len(target_words)
# fig, axes = plt.subplots(1, 6, figsize=(15, 5))
# plt.rcParams["font.sans-serif"] = ["SimHei"]  # 使用中文黑体字体
# plt.rcParams["axes.unicode_minus"] = False  # 用于正常显示负号
# for i, word in enumerate(target_words):
#     if word in word_vectors:
#         word_vector = word_vectors[word]
#     else:
#         raise ValueError("Word not found in vocabulary")
#     # 在不同的子图上绘制柱状图
#     axes[i].bar(range(len(word_vector)), word_vector)
#     axes[i].set_title(f"{word}的词向量")
#     axes[i].set_xlabel("维度")
#     axes[i].set_ylabel("值")
#
# p1 = word_vectors[target_words[0]] - word_vectors[target_words[1]]
# p2 = word_vectors[target_words[2]] - word_vectors[target_words[3]]
# # 在不同的子图上绘制柱状图
# axes[4].bar(range(len(p1)), p1)
# axes[4].set_title(f"{target_words[0]}-{target_words[1]}的词向量")
# axes[4].set_xlabel("维度")
# axes[4].set_ylabel("值")
# # 在不同的子图上绘制柱状图
# axes[5].bar(range(len(p2)), p2)
# axes[5].set_title(f"{target_words[2]}-{target_words[3]}的词向量")
# axes[5].set_xlabel("维度")
# axes[5].set_ylabel("值")
# plt.show()
a = word_vectors['阳虚']
a = np.array(a)
a[1] = 4
print(word_vectors.vectors.shape[0])
now = time.time()
print([word_vectors.similar_by_vector(np.random.random([300]), 1) for item in range(10)])
end = time.time()
elapsed_time = end - now
print(f"计时结束！总时长: {elapsed_time:.2f} 秒")
print(word_vectors.index_to_key[2])