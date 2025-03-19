
import cv2 
imagen=cv2.imread("perritos3.jpg")
template=cv2.imread("templateperritos3.jpg")

#convertir imagenes a escala de grises
imagen2=cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY) 
template2=cv2.cvtColor(template, cv2.COLOR_BGR2GRAY) 

#metodo de comparacion 
metodos=[cv2.TM_SQDIFF, cv2.TM_CCORR_NORMED] #diferencia cuadrática minima y correlación minima 

#busqueda de la pantalla
for metodo in metodos:
    img_res=cv2.matchTemplate(imagen2, template2, method=metodo) #comparación de la imagen
    val_min,val_max,xy_min,xy_max=cv2.minMaxLoc(img_res)
    
    if metodo == cv2.TM_SQDIFF: #mejor coincidencia en valor min de x,y
        #calculo de rectangulos
        x1,y1=xy_min # coords izquierda
        x2,y2=xy_min[0]+template.shape[1],xy_min[1]+template.shape[0] #coords derecha
    else: #mejor coincidencia en valor max de x,y
        #calculo de rectangulos
        x1,y1=xy_max
        x2,y2=xy_max[0]+template.shape[1],xy_max[1]+template.shape[0]
    
#dibujar el rectágulo de localización
cv2.rectangle(imagen,(x1,y1),(x2,y2), (0,0,125),2)
    
#mostrar imagenes 
cv2.imshow("Imagen Original", imagen)
cv2.imshow("Template", template)
cv2.waitKey(0)

cv2.destroyAllWindows()

