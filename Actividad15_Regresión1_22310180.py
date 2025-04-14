import numpy as np
import matplotlib.pyplot as plt

#Inicializar los datos
x = np.arange(-4, 5)
y = 2*x
w = -4

yp = w*x
m = len(x)

#Error cuadrático medio
e = np.power(y - yp, 2)

print("Error: ", e)

#Sumatoria del error cuadrático medio
sum = np.sum(np.power(y - yp, 2))
error = sum/(2*m)

print("Sumatoria: ", error)

#Grafica
plt.plot(w, error, 'ro', label='Error vs w')
plt.plot(x, e, 'bo', label='Error vs x')
plt.title('Error vs w y Error vs x')
plt.xlabel('w y x')
plt.ylabel('Error')
plt.legend()
plt.grid()
plt.show()
