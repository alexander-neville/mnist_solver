import handle_data
import network
import os
import matplotlib.pyplot as plt
import numpy as np

def invert_numbers(samples):
    threshold = np.full((784,1), 1.0)
    for i in range(len(samples)):
        samples[i][0] = np.subtract(threshold, samples[i][0])

def display_numbers(characters):
    for i in range(60):
        plt.subplot(10,6,i+1, frame_on=False)
        plt.axis("off")
        current_char = characters[i][0].reshape(28, 28)
        plt.imshow(current_char, cmap=plt.get_cmap('gray'))
    plt.show()

def main():

    training_data, validation_data, test_data = handle_data.load_data()

    invert_numbers(training_data)
    invert_numbers(validation_data)
    invert_numbers(test_data)

    if os.path.exists("./data/config.json"):

        nn = network.load("./data/config.json")

    else:

        nn = network.Network([784, 30, 10], cost=network.CrossEntropyCost)
        nn.SGD(training_data, 5, 10, 0.1, lmbda = 5.0)
        nn.save("./data/config.json")

    predictions = nn.predict([example[0] for example in test_data[:60]])
    print(predictions)
    display_numbers(test_data)

    print(f"{nn.evaluate(training_data)} / 50000")
    print(f"{nn.evaluate(validation_data)} / 10000")
    print(f"{nn.evaluate(test_data)} / 10000")

if __name__ == "__main__":
    main()
