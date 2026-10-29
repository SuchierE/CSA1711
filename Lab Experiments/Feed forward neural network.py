import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


inputs = [1, 0]

w1 = [[0.5, 0.4],
      [0.3, 0.7]]

w2 = [0.6, 0.8]

hidden = []

for weights in w1:
    total = sum(inputs[i] * weights[i] for i in range(2))
    hidden.append(sigmoid(total))

output_sum = sum(hidden[i] * w2[i] for i in range(2))
output = sigmoid(output_sum)

print("Input Layer:", inputs)
print("Hidden Layer:", [round(x, 4) for x in hidden])
print("Output Layer:", round(output, 4))
