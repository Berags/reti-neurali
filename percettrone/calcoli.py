import grafico as gr
import numpy as np

VROWS = 2 # Numero neuroni di input

def load(file_name):
    '''
    Legge una matrice o un vettore dal file (file_name).
    Ritorna una matrice o un vettore con gli elementi
    appena letti.
    '''
    with open(file_name) as f:
        array = []
        for line in f:  # read rest of lines
            array.append([int(x) for x in line.split()])

        return array

def calcola_attivazione(w, x):              # Somma pesata
    res = 0
    for i in range(VROWS + 1):
        res = res + x[i] * w[i]
    return res

def viene_attivato(a):
    if a > 0:
        return 1
    else:
        return 0


data_input = load('data_percettrone.txt')
data_out = np.array(load('out_percettrone.txt'))
x = [1 for i in range(VROWS + 1)]           # Input cognitrone
out = 0                                     # Valore di output
w = [0.2, 0.5, -2.5]                        # Pesi cognitrone
r = 0.05                                    # Velocità apprendimento
da_stamparex = []
da_stamparey = []
markers = []

# Addestramento
for i in range(len(data_input)):
    x = [1, data_input[i][0], data_input[i][1]]
    a = calcola_attivazione(w, x)
    attivazione = viene_attivato(a)
    markers.append("*")
    out = data_out[i].item()
    for j in range(VROWS + 1):
        w[j] = w[j] + r * ((out - attivazione) * x[j])
    da_stamparex.append(x[1])
    da_stamparey.append(x[2])

# Test
data_test = load('test.txt')
for i in range(len(data_test)):
    x = [1, data_test[i][0], data_test[i][1]]
    a = calcola_attivazione(w, x)
    attivazione = viene_attivato(a)
    markers.append("o")
    da_stamparex.append(x[1])
    da_stamparey.append(x[2])
gr.stampa_grafico(da_stamparex, da_stamparey, markers, w, "\n* = valori di addestramento\no = valori di test")