import cv2
import numpy as np
preimagen=cv2.imread("perritos3.jpg")
imagen = cv2.resize(preimagen, (325,230))

# oscurecer la imagen 
osc1 = np.clip(imagen * 0.5, 0, 255).astype(np.uint8)  # 50% de brillo
osc2 = np.clip(imagen * 0.3, 0, 255).astype(np.uint8)  # 30% de brillo

# función de coordenadas cromáticas
def coordenadas_cromaticas(img):
    img = img.astype(np.float32)  # convertir a flotante
    suma = np.sum(img, axis=2, keepdims=True) + 1e-6  # sumar B+G+R, y que no de 0
    cromatica = img / suma  # transformación cromática
    cromatica = (cromatica * 255).astype(np.uint8)  # ranfo de 0-255
    return cromatica

# aplicar coordenadas cromáticas a cada imagen
cromatica_original = coordenadas_cromaticas(imagen)
cromatica_osc1 = coordenadas_cromaticas(osc1)
cromatica_osc2 = coordenadas_cromaticas(osc2)

#funcion clasificador
def clasificador(img_cromatica):
    m, n, _ = img_cromatica.shape
    imagenb = np.ones((m, n), dtype=np.uint8) * 255  #imagen binaria 

    for x in range(m):
        for y in range(n):
            b, g, r = img_cromatica[x, y]
            if 80 <= b <= 90 and 80 <= g <= 90 and 80 <= r <= 90: #rangos de BGR
                imagenb[x, y] = 0  # fondo en negro
            else:
                imagenb[x, y] = 255  # objeto en blanco

    return imagenb

# llamar función del clasificador en las img cromaticas
clasificada_original = clasificador(cromatica_original)
clasificada_osc1 = clasificador(cromatica_osc1)
clasificada_osc2 = clasificador(cromatica_osc2)

# mostrar imagenes
cv2.imshow("Imagen Original", imagen)
cv2.imshow("Oscurecida 1", osc1)
cv2.imshow("Oscurecida 2", osc2)
cv2.imshow("Coordenadas Cromáticas - Original", cromatica_original)
cv2.imshow("Coordenadas Cromáticas - Oscura 1", cromatica_osc1)
cv2.imshow("Coordenadas Cromáticas - Oscura 2", cromatica_osc2)
cv2.imshow("Clasificada - Original", clasificada_original)
cv2.imshow("Clasificada - Oscura 1", clasificada_osc1)
cv2.imshow("Clasificada - Oscura 2", clasificada_osc2)

cv2.waitKey(0)
cv2.destroyAllWindows()
