#Ejercicio 2
#Filtro 2
#A) Leer una imagen con un solo canal
#B) Duplicar el borde de la imagen adjunta
#C) Aplicar el filtro dado
#D) Mostrar la imagen original y la imagen con el filtro aplicada

import cv2
import numpy as np

#Cargar Imagen
img = cv2.imread("bones.jpg")
imagenb = cv2.resize(img, (456,680)) #redimensionar la imagen 
imagen=cv2.cvtColor(imagenb, cv2.COLOR_BGR2GRAY) #convertir la imagen a un solo canal (escala de grises)

#Duplicar el borde de la imagen
imagen_borde = cv2.copyMakeBorder(imagen, 1, 1, 1, 1, cv2.BORDER_REPLICATE) #agregar un borde de 1 pixel a la imagen

#Aplicar el filtro Laplaciano
kernel_laplaciano = np.array([[1, 1, 1], 
                              [1, -8, 1], 
                              [1, 1, 1]], dtype=np.float32) #definir el kernel del filtro Laplaciano que se nos indica
imagen_filtrada = cv2.filter2D(imagen_borde, -1, kernel_laplaciano) #aplicar el filtro Laplaciano a la imagen con borde
filtro_sin_borde = imagen_filtrada[1:-1, 1:-1] #quitar el borde de la imagen filtrada

#Guardar las imágenes en un archivo .npy
np.save("22310266_filtro2_original.npy", [imagen])
np.save("22310266_filtro2_filtrada.npy", [filtro_sin_borde])

#Mostrar las imágenes
cv2.imshow("Imagen Original", imagenb)
cv2.imshow("Imagen Filtrada (Laplaciano)", filtro_sin_borde)

#Para checar que sí sean de la misma dimensión
# cv2.imwrite("22310266filtro1_original.jpg", imagenb)
# cv2.imwrite("22310266filtro1_filtrada.jpg", filtro_sin_borde)

cv2.waitKey(0)
cv2.destroyAllWindows()