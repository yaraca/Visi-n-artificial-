import cv2
import numpy as np #importar biblioteca numpy como np
preimagen=cv2.imread("perritos3.jpg")
imagen = cv2.resize(preimagen, (456,289)) #redimensionar la imagen 


def clasificador(imagen):
    m,n,c=imagen.shape #obtener las dimensiones de la imagen y almacenarlas en m,n,c
    imagenb=np.zeros((m,n)) #crear matriz de ceros 
    for x in range(m):
        for y in range(n):
            if 20<imagen[x,y,0]<202 and 0<imagen[x,y,1]<220 and 92<imagen[x,y,2]<244:
                imagenb[x,y]=255 #si el pixel cumple con la condición del clasificador se le asigna 255 en la matriz
    cv2.imshow("perritos",imagenb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

clasificador(imagen)