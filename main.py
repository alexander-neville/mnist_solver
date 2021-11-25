import handle_data
import network
import os

training_data, validation_data, test_data = handle_data.load_data()

if os.path.exists("./data/config.json"):
    nn = network.load("./data/config.json")
else:
    nn = network.Network([784, 30, 10], cost=network.CrossEntropyCost)
    nn.SGD(training_data, 5, 10, 0.1, lmbda = 5.0)
    nn.save("./data/config.json")

print(f"{nn.evaluate(test_data)} / 10000")
