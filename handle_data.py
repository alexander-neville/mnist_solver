from __future__ import print_function
import pickle
import gzip
import os.path
import random
import numpy as np

def load_data():

    f = gzip.open('./data/mnist.pkl.gz', 'rb')
    tr_d, va_d, te_d = pickle.load(f, encoding="latin1")
    f.close()

    training_inputs = [np.reshape(x, (784, 1)) for x in tr_d[0]]
    training_results = [vectorized_result(y) for y in tr_d[1]]
    training_data = [[x, y] for (x, y) in zip(training_inputs, training_results)]

    validation_inputs = [np.reshape(x, (784, 1)) for x in va_d[0]]
    validation_results = [vectorized_result(y) for y in va_d[1]]
    validation_data = [[x, y] for (x, y) in zip(validation_inputs, validation_results)]

    test_inputs = [np.reshape(x, (784, 1)) for x in te_d[0]]
    test_results = [vectorized_result(y) for y in te_d[1]]
    test_data = [[x, y] for (x, y) in zip(test_inputs, test_results)]

    return (training_data, validation_data, test_data)

def vectorized_result(j):
    e = np.zeros((10, 1))
    e[j] = 1.0
    return e

def integer_result(j):
    e = np.argmax(j)
    return e

def expand_dataset():
    if not os.path.exists("./data/mnist_expanded.pkl.gz"):
        f = gzip.open("./data/mnist.pkl.gz", 'rb')
        training_data, validation_data, test_data = pickle.load(f, encoding="latin1")
        f.close()
        expanded_training_pairs = []
        j = 0 # counter
        for x, y in zip(training_data[0], training_data[1]):
            expanded_training_pairs.append((x, y))
            image = np.reshape(x, (-1, 28))
            j += 1
            if j % 1000 == 0: print("Expanding image number", j)
            for d, axis, index_position, index in [
                    (1,  0, "first", 0),
                    (-1, 0, "first", 27),
                    (1,  1, "last",  0),
                    (-1, 1, "last",  27)]:
                new_img = np.roll(image, d, axis)
                if index_position == "first": 
                    new_img[index, :] = np.zeros(28)
                else: 
                    new_img[:, index] = np.zeros(28)
                expanded_training_pairs.append((np.reshape(new_img, 784), y))
        random.shuffle(expanded_training_pairs)
        expanded_training_data = [list(d) for d in zip(*expanded_training_pairs)]
        print("Saving expanded data. This may take a few minutes.")
        f = gzip.open("./data/mnist_expanded.pkl.gz", "w")
        pickle.dump((expanded_training_data, validation_data, test_data), f)
        f.close()
