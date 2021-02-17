import numpy as np
from keras.models import Sequential
from keras.layers.core import Activation, Dense
from keras.optimizers import SGD

#  -- 0 --
# |        |
# 6        1
# |        |
#  -- 2 --
# |        |
# 5        3
# |        |
#  -- 4 --

x = np.zeros((10, 7), dtype="uint8")
y = np.zeros((10, 10), dtype="uint8")

# x = input, y = output

x[0] = [1, 1, 0, 1, 1, 1, 1]
x[1] = [0, 1, 0, 1, 0, 1, 0]
x[2] = [1, 1, 1, 0, 1, 1, 0]
x[3] = [1, 1, 1, 1, 1, 0, 0]
x[4] = [1, 1, 1, 0, 0, 0, 1]
x[5] = [1, 0, 1, 1, 0, 1, 1]
x[6] = [1, 0, 1, 1, 1, 1, 1]
x[7] = [1, 1, 0, 1, 0, 0, 0]
x[8] = [1, 1, 1, 1, 1, 1, 1]
x[9] = [1, 1, 1, 1, 1, 0, 1]

# output desiderato, in "1-hot encoding"
y[0] = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
y[1] = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
y[2] = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
y[3] = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
y[4] = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
y[5] = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
y[6] = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
y[7] = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
y[8] = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
y[9] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

model = Sequential()
model.add(Dense(4, input_dim=7))
model.add(Activation("sigmoid"))

model.add(Dense(10))
model.add(Activation("sigmoid"))

sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss="mean_squared_error", optimizer=sgd)

weight_formatter = lambda x: "%.1f" % x
np.set_printoptions(formatter={"float_kind": weight_formatter})

print("Pesi delle singole interconnessioni prima dell'addestramento:")
for layer in model.layers:
    pesi = layer.get_weights()
    print(pesi)


print("Addestramento...")
addestramento = model.fit(x, y, epochs=1000, verbose=0)


print("Pesi delle singole interconnessioni dopo l'addestramento:")
np.set_printoptions(formatter={"float_kind": weight_formatter})

for layer in model.layers:
    pesi = layer.get_weights()
    print(pesi)
