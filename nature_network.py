from numpy import exp, array, random, dot


def cal_output(inputs, weights):
    ret = 1 / (1 + exp(-(dot(inputs, weights))))
    return ret


training_set_inputs = array([[0, 0, 1],
                             [1, 1, 1],
                             [1, 0, 1],
                             [0, 1, 1]])

training_set_outputs = array([[0, 1, 1, 1]]).T

random.seed(1)

synaptic_weights = 2 * random.random((3, 1)) - 1

for i in xrange(10000):
    output = cal_output(training_set_inputs, synaptic_weights)
    synaptic_weights += dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))

print synaptic_weights
print cal_output(array([[1, 0, 0],
                        [1, 1, 1],
                        [1, 1, 0],
                        [0, 1, 0]]),
                 synaptic_weights)
