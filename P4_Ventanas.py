import cv2
import numpy as np
import matplotlib.pyplot as plt #graficar 
from skimage.measure import label, regionprops #etiquetar 

#Cargar imagen
imagen = cv2.imread("perritos1.jpg")
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)#convertir a RGB

#Función Clasificador
def clasificador(imagen):
    m, n, c = imagen.shape
    imagenb = np.zeros((m, n), dtype=np.uint8)
    
    for x in range(m):
        for y in range(n):
            if 11 < imagen[x, y, 0] < 227 and 0 < imagen[x, y, 1] < 235 and 1 < imagen[x, y, 2] < 234:
                imagenb[x, y] = 255
                
    return imagenb

#Usar el clasificador en la imagen
imagenb = clasificador(imagen)

#Separar los objetos por numero
etiquetas = label(imagenb, connectivity=2)

#filtrar errores de objetos 
eti_filtrada = np.zeros_like(etiquetas)
area_min = 500  #área minima para ser objeto
for region in regionprops(etiquetas):
    if region.area >= area_min:
        eti_filtrada[etiquetas == region.label] = region.label

#imagen con colores para ver etiquetas
img_etiquetada = np.uint8(plt.cm.plasma(eti_filtrada / eti_filtrada.max())[:, :, :3] * 255)
#para cambiar los colores de etiqueta, otras opciones son (plt.cm._):
    #jet,viridis,plasma,tab10,nimpy_spectral

#poner números en las etiquetas
for i, region in enumerate(regionprops(eti_filtrada), start=1):
    ymin, xmin, ymax, xmax = region.bbox  #obtener coordenadas del rectángulo alrededor de los objetos
    centro = (int((xmin + xmax) / 2), int((ymin + ymax) / 2))  #calcular el centro
    cv2.putText(img_etiquetada, str(i), centro, cv2.FONT_HERSHEY_SIMPLEX, 
                0.9, (255, 255, 255), 2, cv2.LINE_AA)#colocar no. de la etiqueta en el centro del objeto

#dibujar los rectangulos
img_ventana = imagen.copy()

for region in regionprops(eti_filtrada):
    ymin, xmin, ymax, xmax = region.bbox
    cv2.rectangle(img_ventana, (xmin, ymin), (xmax, ymax), (255, 0, 0), 2)

#mostrar imagenes
fig, axes = plt.subplots(1, 4, figsize=(15, 5))
axes[0].imshow(imagen)
axes[0].set_title("Imagen Entrada")
axes[1].imshow(imagenb, cmap='gray')
axes[1].set_title("Clasificación")
axes[2].imshow(img_etiquetada)
axes[2].set_title("Etiquetado")
axes[3].imshow(img_ventana)
axes[3].set_title("Localización")

for ax in axes:
    ax.axis("off")

plt.show()