from __future__ import print_function
import pickle
import gzip
import os.path
import random
import numpy as np
import matplotlib.pyplot as plt

def vectorized_result(j):
    """Output vector for an integer label"""
    e = np.zeros((10, 1))
    e[j] = 1.0
    return e

def integer_result(j):
    """Integer label for output vector"""
    e = np.argmax(j)
    return e

def display_one_character(character):
    plt.subplot(1, 1, 1)
    plt.imshow(character, cmap=plt.get_cmap('gray'))
    plt.show()

def invert_numbers(samples):
    threshold = np.full((784,1), 1.0)
    for i in range(len(samples)):
        samples[i][0] = np.subtract(threshold, samples[i][0])

def display_characters(characters):
    for i in range(60):
        plt.subplot(10,6,i+1, frame_on=False)
        plt.axis("off")
        current_char = characters[i][0].reshape(28, 28)
        plt.imshow(current_char, cmap=plt.get_cmap('gray'))
    plt.show()

def load_data():

    if os.path.exists("./data/mnist_expanded.pkl.gz"):
        f = gzip.open('./data/mnist_expanded.pkl.gz', 'rb')
    elif os.path.exists("./data/mnist.pkl.gz"):
        f = gzip.open('./data/mnist.pkl.gz', 'rb')
    else:
        exit()

    datasets = pickle.load(f, encoding="latin1")
    f.close()
    return datasets

def expand_dataset():
    if not os.path.exists("./data/mnist_expanded.pkl.gz"):
        f = gzip.open("./data/mnist.pkl.gz", 'rb')
        training_data, validation_data, test_data = pickle.load(f, encoding="latin1")
        f.close()
        expanded_training_data = []
        j = 0 # counter
        for sample in training_data:
            expanded_training_data.append(sample)
            image = np.reshape(sample[0], (-1, 28))
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
                expanded_training_data.append([np.reshape(new_img, (784, 1)), sample[1]])
        random.shuffle(expanded_training_data)
        print("Saving expanded data. This may take a few minutes.")
        f = gzip.open("./data/mnist_expanded.pkl.gz", "w")
        pickle.dump((expanded_training_data, validation_data, test_data), f)
        f.close()
        print("done!")

def multiply_examples(dataset):
    expanded_dataset = []
    for sample in dataset:
        expanded_dataset.append(sample)
        image = np.reshape(sample[0], (-1, 28))
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
            expanded_dataset.append([np.reshape(new_img, (784, 1)), sample[1]])
    random.shuffle(expanded_dataset)
    return expanded_dataset
