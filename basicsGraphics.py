import numpy as np
import matplotlib.pyplot as plt

# Vector columna
vector = np.array([1, 1])
vector1 = np.array([-1,1])  # <-- convertir a 1D

# Crear gráfico con colores
plt.plot(vector1, marker='o', color='red')   # línea roja con puntos
plt.plot(vector, marker='o', color='blue')   # línea azul con puntos
plt.title("Vector columna simple")
plt.xlabel("Índice")
plt.ylabel("Valor")
plt.grid(True)
plt.show()
