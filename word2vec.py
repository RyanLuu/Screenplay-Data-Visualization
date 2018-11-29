import gensim
import numpy as np
import parser

def load():
  global model
  model = gensim.models.KeyedVectors.load_word2vec_format('./models/GoogleNews-vectors-negative300.bin', binary=True)

def is_valid(word):
  return word in model.wv

def word_vector(word):
  return model.wv[word]

def sentence_vector(words):
  if isinstance(words, str):
    words = parser.line_to_words(words)
  word_vectors = np.array([word_vector(word) for word in words if is_valid(word)])
  if (len(word_vectors)):
    return np.array([sum(i) for i in zip(*word_vectors)])
  print(words)
  return np.zeros(model.vector_size)
