import cv2
import numpy as np
preimagen = cv2.imread("perritos3.jpg")  
imagen = cv2.resize(preimagen, (325, 230))

#función para cambiar de color la imagen
def cambiar_color(img, tipo):
    img = img.astype(np.float32) #convertir la imagen a float
    #cambiar los valores de los canales de color
    if tipo == "rosita":
        img[:, :, 0] *= 0.56  #azul Cambio en B
        img[:, :, 1] *= 0.2  #rojo Cambio en G
    elif tipo == "verde":
        img[:, :, 0] *= 0.5  #azul Cambio en B
        img[:, :, 2] *= 0.2  #verde Cambio en R
    img = np.clip(img, 0, 255).astype(np.uint8) #rango de 0-255
    return img

#aplicar cambio de color a imagen
color_rosita = cambiar_color(imagen, "rosita") #llamar a la función cambiar_color
color_verde = cambiar_color(imagen, "verde") #llamar a la función cambiar_color

#función clasificador para imagen original y de color
def clasificador1(imagen):
    m,n,c=imagen.shape
    imagenb=np.zeros((m,n))
    for x in range(m):
        for y in range(n):
            if 10<imagen[x,y,0]<119 and 4<imagen[x,y,1]<166 and 0<imagen[x,y,2]<197:
                imagenb[x,y]=255
    return imagenb

#aplicar el primer clasificador a la imagen original y a las de color
clas1_original = clasificador1(imagen)
clas1_rosita = clasificador1(color_rosita)
clas1_verde = clasificador1(color_verde)

#función white patch
def white_patch(img): #normalizar la imagen
    img = img.astype(np.float32) #convertir la imagen a float
    max_vals = np.max(img, axis=(0, 1), keepdims=True)  #max valor de BGR
    max_vals[max_vals == 0] = 1  #reemplazar 0 por 1
    img = img / max_vals * 255  #formual white patch
    img = np.clip(img, 0, 255).astype(np.uint8)  #rango de 0-255
    return img

#aplicar el algoritmo white patch a las imagenes
wp_original = white_patch(imagen)
wp_rosita = white_patch(color_rosita)
wp_verde = white_patch(color_verde)

#función clasificador para imagen de white patch
def clasificador2(img):
    m, n, _ = img.shape
    img_binaria = np.ones((m, n), dtype=np.uint8) * 0
    img = img.astype(np.float32) 
    for x in range(m):
        for y in range(n):
            b, g, r = img[x, y]
            if 10 <= b <= 119 and 4 <= g <= 166 and 0 <= r <= 197:
                img_binaria[x, y] = 255
    return img_binaria

#aplicar el clasificador a las imagenes que dio el white patch
clas2_original = clasificador2(wp_original)
clas2_rosita = clasificador2(wp_rosita)
clas2_verde = clasificador2(wp_verde)


#mostrar imagenes
cv2.imshow("Original", imagen)
cv2.imshow("Color Rosita", color_rosita)
cv2.imshow("Color Verde", color_verde)
cv2.imshow("Clasificador Original", clas1_original)
cv2.imshow("Clasificador Rosita", clas1_rosita)
cv2.imshow("Clasificador Verde", clas1_verde)
cv2.imshow("White Patch Original", wp_original)
cv2.imshow("White Patch Rosita", wp_rosita)
cv2.imshow("White Patch Verde", wp_verde)
cv2.imshow("Clasificada WP Original", clas2_original)
cv2.imshow("Clasificada WP Rosita", clas2_rosita)
cv2.imshow("Clasificada WP Verde", clas2_verde)

cv2.waitKey(0)
cv2.destroyAllWindows()