#Ejercicio 1
#Filtro 1
#A) Leer una imagen con un solo canal
#B) Duplicar el borde de la imagen adjunta
#C) Aplicar el filtro de operador Laplaciano
#D) Mostrar la imagen original y la imagen con el filtro aplicada

import cv2
import numpy as np

#Función que define el kernel del filtro Laplaciano
def kernel_laplaciano():
    #matriz de la segunda derivada en x
    derivada2_x = np.array ([[0, 0, 0], 
                            [1, -2, 1], 
                            [0, 0, 0]], dtype=np.float32)
    #matriz de la segunda derivada en y 
    derivada2_y = np.array([[0, 1, 0], 
                            [0, -2, 0], 
                            [0, 1, 0]],dtype=np.float32)    
    kernel_laplaciano = derivada2_x + derivada2_y #suma de las matrices de las derivadas en x y y
    return kernel_laplaciano

#Cargar Imagen
img = cv2.imread("bones.jpg")
imagenb = cv2.resize(img, (456,680)) #redimensionar la imagen 
imagen=cv2.cvtColor(imagenb, cv2.COLOR_BGR2GRAY) #convertir la imagen a un solo canal (escala de grises)

#Duplicar el borde de la imagen
imagen_borde = cv2.copyMakeBorder(imagen, 1, 1, 1, 1, cv2.BORDER_REPLICATE) #agregar un borde de 1 pixel a la imagen

#Aplicar el filtro Laplaciano
filtro_laplaciano = kernel_laplaciano() #llamar a la función que define el kernel del filtro Laplaciano
print (kernel_laplaciano) #mostrar que es el kernel correcto para el filtro laplaciano que obtuvimos
imagen_filtrada = cv2.filter2D(imagen_borde, -1, filtro_laplaciano)#aplicar el filtro Laplaciano a la imagen con borde
filtro_sin_borde = imagen_filtrada[1:-1, 1:-1] #quitar el borde de la imagen filtrada

#Guardar las imágenes en un archivo .npy
np.save("22310266_filtro1_original.npy", [imagen])
np.save("22310266_filtro1_filtrada.npy", [filtro_sin_borde])

#Mostrar las imágenes
cv2.imshow("Imagen Original", imagenb)
cv2.imshow("Imagen Filtrada (Laplaciano)", filtro_sin_borde)

#Para checar que sí sean de la misma dimensión
# cv2.imwrite("22310266filtro1_original.jpg", imagenb)
# cv2.imwrite("22310266filtro1_filtrada.jpg", filtro_sin_borde)

cv2.waitKey(0)
cv2.destroyAllWindows()