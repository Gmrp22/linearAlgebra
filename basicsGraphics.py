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

# plt.arrpw

# Vector 1: [2, 2], starting at (0,0)
start1 = np.array([0, 0])
vec1 = np.array([2, 2])

# Vector 2: [6, 12], starting at (1, -2)
start2 = np.array([1, -2])
vec2 = np.array([6, 12])

plt.figure()
# Dibujar vectores como flechas
plt.arrow(start1[0], start1[1], vec1[0], vec1[1], head_width=0.5, head_length=0.7, color='blue', length_includes_head=True)
plt.arrow(start2[0], start2[1], vec2[0], vec2[1], head_width=0.5, head_length=0.7, color='red', length_includes_head=True)

plt.xlim(-1, 10)
plt.ylim(-5, 15)
plt.grid(True)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Vectores con punto de inicio")
plt.show()