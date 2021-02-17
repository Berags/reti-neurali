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

def calcola_attivazione(w, x):
    '''
    Calcola la somma pesata seguendo la formula:
    s = bias + w * x
    '''
    res = 0
    for i in range(VROWS + 1):
        res = res + x[i] * w[i]
    return res

def viene_attivato(a):
    '''
    Restituisce 1 se il valore della somma pesata è maggiore di 0,
    altrimenti restituisce 0.
    '''
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
da_stamparex = []                           # Array dei valori della X utilizzato per la stampa
da_stamparey = []                           # Array dei valori della Y utilizzato per la stampa
markers = []                                # Stile della stampa

# Addestriamo la rete neurale
for i in range(len(data_input)):
    # Inizializziamo i valori di x con i dati letti da file
    x = [1, data_input[i][0], data_input[i][1]] 
    # Calcoliamo la somma pesata
    a = calcola_attivazione(w, x)
    # Verifichiamo il valore della somma pesata
    attivazione = viene_attivato(a)
    markers.append("*")
    out = data_out[i].item()
    for j in range(VROWS + 1):
        w[j] = w[j] + r * ((out - attivazione) * x[j]) # Utilizziamo la formula w(t + 1) = w(t) + (d - y) * x
    da_stamparex.append(x[1])
    da_stamparey.append(x[2])

# Testiamo la rete neurale
data_test = load('test.txt')
for i in range(len(data_test)):
    x = [1, data_test[i][0], data_test[i][1]]
    a = calcola_attivazione(w, x)
    attivazione = viene_attivato(a)
    markers.append("o")
    da_stamparex.append(x[1])
    da_stamparey.append(x[2])

gr.stampa_grafico(da_stamparex, da_stamparey, markers, w, "\n* = valori di addestramento\no = valori di test")
