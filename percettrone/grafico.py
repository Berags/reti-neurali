# importing the required module 
import matplotlib.pyplot as plt 

# Nome degli assi
plt.ylabel('Asse y')
plt.xlabel('Asse x') 

def stampa_grafico(x, y, cls, w, testo):
    '''
    Stampa il grafico con i valori calcolati.
    '''
    # Titolo della finestra
    plt.suptitle('Modello percettrone - Beragnoli Jacopo', fontsize=15, fontweight='bold')
    plt.title(testo)
    # Titolo della finestra

    if w[2] == 0: return # Se w[2] ha valore 0 ritorna --> Non si può dividere per 0!

    # Calcolo dell'equazione della retta
    m = -w[1]/w[2]
    q = -w[0]/w[2]
    # Calcolo dell'equazione della retta

    # Stampiamo la retta mediante l'equazione appena trovata
    plt.plot([i for i in range(12)], [i*m + q for i in range(12)]) 
    for i in range(len(x)):
        # Stampa di tutti i punti calcolati dalla rete neurale
        plt.scatter(x[i], y[i], label= "stars", marker= cls[i], color= "black", s=100)  
    
    # Mostra la finestra del grafico
    plt.show()