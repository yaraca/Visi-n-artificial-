
import cv2
import numpy as np
import matplotlib.pyplot as plt

imagen = cv2.imread("bordes1.jpg")

#definir el filtro de sobel (bordes verticales y horizontales)
kernel_x = np.array([[-1, 0, 1], #cambios en horizontal-> da bordes verticales
                     [-2, 0, 2], 
                     [-1, 0, 1]])

kernel_y = np.array([[-1, -2, -1], #cambios en vertical-> da bordes horizontales
                     [ 0,  0,  0], 
                     [ 1,  2,  1]])

#aplicar el filtro en cada canal (BGR)
Gx_b = cv2.filter2D(imagen[:, :, 0], -1, kernel_x)
Gx_g = cv2.filter2D(imagen[:, :, 1], -1, kernel_x)
Gx_r = cv2.filter2D(imagen[:, :, 2], -1, kernel_x)

Gy_b = cv2.filter2D(imagen[:, :, 0], -1, kernel_y)
Gy_g = cv2.filter2D(imagen[:, :, 1], -1, kernel_y)
Gy_r = cv2.filter2D(imagen[:, :, 2], -1, kernel_y)

#fusionar los resultados en una imagen 
Gx = cv2.merge([Gx_b, Gx_g, Gx_r]) #imagen bordes x
Gy = cv2.merge([Gy_b, Gy_g, Gy_r]) #imagen bordes y

#calcular magnitud del gradiente en cada canal y luego fusionarlos
G = np.sqrt(Gx.astype(np.float64) ** 2 + Gy.astype(np.float64) ** 2)
G = np.uint8(G * 255 / np.max(G))  # normalización para que queden en 0-255

#mostrar las imagenes 
fig, axes = plt.subplots(1, 4, figsize=(15, 5))
axes[0].imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))  #convertir de BGR a RGB para visualizar img
axes[0].set_title("Imagen Original")
axes[1].imshow(cv2.cvtColor(Gx, cv2.COLOR_BGR2RGB))
axes[1].set_title("Bordes Verticales")
axes[2].imshow(cv2.cvtColor(Gy, cv2.COLOR_BGR2RGB))
axes[2].set_title("Bordes Horizontales")
axes[3].imshow(cv2.cvtColor(G, cv2.COLOR_BGR2RGB))
axes[3].set_title("Magnitud del Gradiente")

for ax in axes:
    ax.axis("off")

plt.show()
