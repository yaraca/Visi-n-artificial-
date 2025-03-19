import cv2
import numpy as np
import matplotlib.pyplot as plt
imagen = cv2.imread("perrito2.jpg")

#función para agregar ruido gaussiano
def ruido_gauss(imagen, mean=0, var=10):
    row, col, ch = imagen.shape #obtener filas, columnas y canales de color
    sigma = var ** 0.3 #desviación estándar
    gauss = np.random.normal(mean, sigma, (row, col, ch)).astype(np.uint8) #generar ruido gauss
    imagen_ruido = cv2.add(imagen, gauss) #imagen con ruido
    return imagen_ruido

#función para agregar ruido sal y pimienta
def ruido_sal_pimienta(imagen, prob=0.05): #prob=porcentaje de pixeles modificados
    imagen_ruido = imagen.copy()
    row, col, ch = imagen.shape
    num_salt = np.ceil(prob * row * col) #pixeles modificados
    
    #ruido de sal (pixeles blancos)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in imagen.shape[:2]]
    imagen_ruido[coords[0], coords[1], :] = 255 #asigna valor blanco
    
    #ruido de pimienta (pixeles negros)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in imagen.shape[:2]]
    imagen_ruido[coords[0], coords[1], :] = 0 #asigna valor negro
    
    return imagen_ruido

#aplicar ruido
imagen_gauss = ruido_gauss(imagen)
imagen_syp = ruido_sal_pimienta(imagen)

#aplicar filtro gaussiano
Fgauss_gauss = cv2.GaussianBlur(imagen_gauss, (3, 3), 0)
Fgauss_syp = cv2.GaussianBlur(imagen_syp, (3, 3), 0)

#aplicar filtro media
Fmedia_gauss = cv2.blur(imagen_gauss, (3, 3))
Fmedia_syp = cv2.blur(imagen_syp, (3, 3))

#aplicar filtro mediana
Fmediana_gauss = cv2.medianBlur(imagen_gauss, 3)
Fmediana_syp = cv2.medianBlur(imagen_syp, 3)

#aplicar filtro minimo (erosión)
Fmin_gauss = cv2.erode(imagen_gauss, np.ones((3, 3), np.uint8))
Fmin_syp = cv2.erode(imagen_syp, np.ones((3, 3), np.uint8))

#aplicar filtro máximo (dilatación)
Fmax_gauss = cv2.dilate(imagen_gauss, np.ones((1, 1), np.uint8))
Fmax_syp = cv2.dilate(imagen_syp, np.ones((1, 1), np.uint8))

#mostrar imagenes
fig, axes = plt.subplots(3, 4, figsize=(12, 9))
imagenes = [
    ("Ruido Gaussiano", imagen_gauss),
    ("Ruido Sal y Pimienta", imagen_syp),
    ("Filtro Gaussiano->Ruido Gauss", Fgauss_gauss),
    ("Filtro Gaussiano->Ruido S&P", Fgauss_syp),
    ("Filtro Media->Ruido Gauss", Fmedia_gauss),
    ("Filtro Media->Ruido S&P", Fmedia_syp),
    ("Filtro Mediana->Ruido Gauss", Fmediana_gauss),
    ("Filtro Mediana->Ruido S&P", Fmediana_syp),
    ("Filtro Mínimo->Ruido Gauss", Fmin_gauss),
    ("Filtro Mínimo->Ruido S&P", Fmin_syp),
    ("Filtro Máximo->Ruido Gauss", Fmax_gauss),
    ("Filtro Máximo->Ruido S&P", Fmax_syp),
]

for ax, (title, img) in zip(axes.flatten(), imagenes):
    ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    ax.set_title(title)
    ax.axis("off")

plt.tight_layout()
plt.show()