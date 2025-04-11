import numpy as np
import matplotlib.pyplot as plt

#Inicializar los datos
x = np.arange(-4, 5)
y = 2*x
w = -3

#Y estimada 
yp = w*x
m = len(x)

#Calcular el error cuadrático medio en función de w
e = np.power(y - yp, 2)

print("El error es: ", e)

#Calcular la sumatoria del error cuadrático medio
sum = np.sum(np.power(y - yp, 2))
error = sum/(2*m)

print("La sumatoria del error es: ", error)

# #Graficar w vs error y 
# plt.plot(w, error, 'ro')
# plt.title('Error vs w')
# plt.xlabel('w')
# plt.ylabel('Error')
# plt.grid()
# plt.show()

# #Graficar la curva de la sumatoria de np.power(y - yp, 2)
# plt.plot(x, e, 'ro')
# plt.title('Error vs x')
# plt.xlabel('x')
# plt.ylabel('Error')
# plt.grid()
# plt.show()


#Graficar w vs error y, ademas Graficar la curva de la sumatoria de np.power(y - yp, 2)
plt.plot(w, error, 'ro', label='Error vs w')
plt.plot(x, e, 'bo', label='Error vs x')
plt.title('Error vs w y Error vs x')
plt.xlabel('w y x')
plt.ylabel('Error')
plt.legend()
plt.grid()
plt.show()



