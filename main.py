import handle_data
import network
import os

training_data, validation_data, test_data = handle_data.load_processed_data()
training_data = list(training_data)

print(type(training_data[0]))

if not os.path.exists("./data/config.json"):
    nn = network.Network([784, 30, 10], cost=network.CrossEntropyCost)
    nn.SGD(training_data, 5, 10, 0.1, lmbda = 5.0,
            evaluation_data=validation_data,
            monitor_evaluation_accuracy=True)
    nn.save("./data/config.json")
