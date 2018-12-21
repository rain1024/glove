from os import remove
from os.path import exists
from datetime import datetime
from underthesea.word_tokenize import tokenize

input_filepath = "/media/anhv/data/nlp-data/vncorpus 18GB/corpus-full.txt"
output_filepath = "/home/anhv/PycharmProjects/undertheseanlp/word_embeddings/egs/word2vec/data/corpus_18G.normalized.txt"
if exists(output_filepath):
    remove(output_filepath)
output = open(output_filepath, "a")
for i, text in enumerate(open(input)):
    if i % 100000 == 0:
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), i)
    text = text.strip()
    text = tokenize(text) + "\n"
    output.write(text)
