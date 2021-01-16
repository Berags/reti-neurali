import numpy as np
from array import *

VROWS = 4
MROWS = 4
COLS = 4

# Metodo per la stampa della matrice
def print2darray(a):
    print("\n".join(["".join(["{:4}".format(item) for item in row]) for row in a]))
    return


# Carica un vettore o una matrice da file esterno
def load(file_name):
    with open(file_name) as f:
        array = []
        for line in f:  # read rest of lines
            array.append([int(x) for x in line.split()])

        return array


print("Lettura da file...")

# inizializzazione array m con tutti i valori a 0
m = np.array([[0 for x in range(VROWS)] for y in range(COLS)])

# lamb = float(input())  # Richiede lambda all'utente !!! INUTILIZZATO !!!
# Lettura valori da file
data_in = np.array(load("input_data.txt"))
data_out = np.array(load("output_data.txt"))

print("Fine lettura da file!")
print("Inizio creazione rete neurale...")

for i in range(len(data_in)):
    for j in range(len(data_in[i])):
        print(f"{data_in[i][j]} -> {data_out[i][j]}")
    # np.vstack --> da vettore orizzontale a verticale
    # Opposto di np.transpose
    deltam = np.vstack(data_out[i]) * data_in[i]
    m = deltam + m
print(f"\n\nMATRICE M: \n{m}")

print("Fine creazione rete neurale!")
print("Inizio addestramento rete neurale...")

test_in = np.array(load("input_test.txt"))

# Addestramento della rete neurale attraverso la regola di hebb
for f in test_in:
    out = [0 for x in range(4)]
    for i in range(MROWS):
        out[i] = 0
        for j in range(VROWS):
            out[i] = out[i] + m[i][j] * f[j]
    print(f"\nINPUT: {f}\nOUTPUT:{out}")

print("Rete neurale addestrata!")