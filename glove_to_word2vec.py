from gensim.test.utils import datapath, get_tmpfile
from gensim.models import KeyedVectors

glove_file = './output/vectors.txt'
tmp_file = "./output/glove.tmp"
vector_file = './output/glove.bin'

# call glove2word2vec script
# default way (through CLI): python -m gensim.scripts.glove2word2vec --input <glove_file> --output <w2v_file>
from gensim.scripts.glove2word2vec import glove2word2vec
glove2word2vec(glove_file, tmp_file)

model = KeyedVectors.load_word2vec_format(tmp_file)
model.save(vector_file)