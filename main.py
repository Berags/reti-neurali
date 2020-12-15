"""
    Trasposizione del programma in C
    Calcolo matriciale applicato alle reti neurali

    Beragnoli Jacopo - 5°IC
"""
import numpy as np
# Impostazioni per la formattazione della stampa su schermo
np.set_printoptions(formatter={'float': '{: 0.1f}'.format}) # Impostiamo la stampa in floating point con precisione ad 0.1

""" Funzione che stampa il valore della matrice o del vettore """
def stampa(nome, arr):
    print(f"{nome}: \n{arr}\n\n")

""" Funzione che rende il vettore trasposto """
def trasposto(v):    
    f1t = [] # vettore contentente il vettore trasposto 
    for i in range(len(v)):         # for che controlla ogni valore nel vettore
        f1t = np.append(f1t, v[i])  # funzione che crea un nuovo vettore con i valori del precedente
    return f1t                      # ritorna il vettore trasposto

""" Inizializzazione Vettori """
f1 = np.array([[1],
               [0],
               [1]])   #Vettore F1
g1 = np.array([[1], 
               [1], 
               [0]])   #Vettore G1
  
f2 = np.array([[1], [0], [-1]])  #Vettore F2
g2 = np.array([[1], [0], [1]])   #Vettore G2
  
f3 = np.array([[0], [1], [0]])   #Vettore F3
g3 = np.array([[0], [0], [1]])   #Vettore G3

""" Inizializzazione Vettori """

deltaA1 = g1 * trasposto(f1) # Calcoliamo ΔA(1) = g(1) * f(1)T
deltaA2 = g2 * trasposto(f2) # Calcoliamo ΔA(2) = g(2) * f(2)T
deltaA3 = g3 * trasposto(f3) # Calcoliamo ΔA(3) = g(3) * f(3)T

stampa("ΔA(1) = g(1) * f(1)T", deltaA1) # Stampiamo i valori del vettore ΔA(1)
stampa("ΔA(2) = g(2) * f(2)T", deltaA2) # Stampiamo i valori del vettore ΔA(2)
stampa("ΔA(3) = g(3) * f(3)T", deltaA3) # Stampiamo i valori del vettore ΔA(3)

print("\nAdesso calcoliamo A...\n")

a = deltaA1 + deltaA2 + deltaA3 # Sommiamo i tre vettori ΔA(1), ΔA(2) e ΔA(3)

stampa("A", a)