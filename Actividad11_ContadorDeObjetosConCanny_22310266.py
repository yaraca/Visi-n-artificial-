import cv2

# Leer la imagen original
imagen = cv2.imread('pelotas.jpg')
#Cambiar a escala de grises
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
#Aplicar un filtro gaussiano para eliminar ruido
bordes = cv2.Canny(grises, 100, 200)


ctns, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #Encontrar contornos

#Dibujar los contornos encontrados en la imagen original
cv2.drawContours(imagen, ctns, -1, (0,0,255), 2)
print('Número de contornos encontrados: ', len(ctns)) #Imprimir el número de contornos encontrados
texto = 'Contornos encontrados: '+ str(len(ctns)) 
cv2.putText(imagen, texto, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, #
  (255, 0, 0), 1) #Agregar texto a la imagen
#Mostrar la imagen con los contornos encontrados
cv2.imshow('Imagen', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()