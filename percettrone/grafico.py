# importing the required module 
import matplotlib.pyplot as plt 

plt.ylabel('Asse y')  
plt.xlabel('Asse x') 

# Sistemare label il resto funziona

def stampa_grafico(x, y, cls, w, testo):
    plt.suptitle('Modello percettrone - Beragnoli Jacopo', fontsize=15, fontweight='bold')
    plt.title(testo)
    if w[2] == 0: return
    m = -w[1]/w[2]
    q = -w[0]/w[2]
    plt.plot([i for i in range(12)], [i*m + q for i in range(12)])
    for i in range(len(x)):
        plt.scatter(x[i], y[i], label= "stars", marker= cls[i], color= "black", s=100)  
    plt.show()