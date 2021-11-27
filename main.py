import dataset
import network
import os
# import matplotlib.pyplot as plt
# import numpy as np


def main():

    training_data, validation_data, test_data = dataset.load_data()

#    dataset.invert_numbers(training_data)
#    dataset.invert_numbers(validation_data)
#    dataset.invert_numbers(test_data)

    dataset.display_characters(training_data)

    if os.path.exists("./data/config.json"):

        nn = network.load("./data/config.json")

    else:

        nn = network.Network([784, 30, 10], cost=network.CrossEntropyCost)
        nn.SGD(training_data, 3, 10, 0.1, lmbda = 5.0)
        nn.save("./data/config.json")

    # predictions = nn.predict([example[0] for example in test_data[:60]])
    # print(predictions)
    # dataset.display_characters(test_data)

    print(f"{nn.evaluate(training_data)} / 50000")
    print(f"{nn.evaluate(validation_data)} / 10000")
    print(f"{nn.evaluate(test_data)} / 10000")

if __name__ == "__main__":
    main()
