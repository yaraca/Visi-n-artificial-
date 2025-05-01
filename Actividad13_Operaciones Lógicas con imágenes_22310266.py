#Operadores BITWISE (AND-OR-NOT-XOR) con OpenCV y Python

#Crear imagenes de prueba
import cv2
import numpy as np  

img1 = np.zeros((400,600), dtype=np.uint8) #imagen negra
img1[100:300,200:400] = 255 #cuadro blanco
img2 = np.zeros((400,600), dtype=np.uint8) #imagen negra
img2 = cv2.circle(img2,(300,200),125,(255),-1) #circulo blanco
cv2.imshow('img1',img1) #muestra la imagen 1
cv2.imshow('img2',img2) #muestra la imagen 2
cv2.waitKey(0)
cv2.destroyAllWindows()


#AND ( cv2.bitwise_and )
#Operador AND entre las dos imagenes
img1 = np.zeros((400,600), dtype=np.uint8) #imagen negra
img1[100:300,200:400] = 255 #cuadro blanco
img2 = np.zeros((400,600), dtype=np.uint8) #imagen negra
img2 = cv2.circle(img2,(300,200),125,(255),-1) #circulo blanco
AND = cv2.bitwise_and(img1,img2) #operador AND entre las dos imagenes para obtener la intersección
cv2.imshow('AND', AND) #muestra la imagen AND
cv2.waitKey(0)
cv2.destroyAllWindows()

#NOT ( cv2.bitwise_not )
#Operador NOT entre la imagen 1
img1 = np.zeros((400,600), dtype=np.uint8) #imagen negra
img1[100:300,200:400] = 255 #cuadro blanco
img2 = np.zeros((400,600), dtype=np.uint8) #imagen negra
img2 = cv2.circle(img2,(300,200),125,(255),-1) #circulo blanco
NOT = cv2.bitwise_not(img1) #operador NOT entre la imagen 1 para obtener la negación de la imagen 1
cv2.imshow('NOT', NOT) #muestra la imagen NOT
cv2.waitKey(0)
cv2.destroyAllWindows()

#OR ( cv2.bitwise_or )
#Operador OR entre las dos imagenes
img1 = np.zeros((400,600), dtype=np.uint8) #imagen negra
img1[100:300,200:400] = 255 #cuadro blanco
img2 = np.zeros((400,600), dtype=np.uint8) #imagen negra
img2 = cv2.circle(img2,(300,200),125,(255),-1) #circulo blanco
OR = cv2.bitwise_or(img1,img2) #operador OR entre las dos imagenes para obtener la unión
cv2.imshow('OR', OR) #muestra la imagen OR
cv2.waitKey(0)
cv2.destroyAllWindows()

#XOR ( cv2.bitwise_xor ) 
#Operador XOR entre las dos imagenes
img1 = np.zeros((400,600), dtype=np.uint8) #imagen negra
img1[100:300,200:400] = 255 #cuadro blanco
img2 = np.zeros((400,600), dtype=np.uint8) #imagen negra
img2 = cv2.circle(img2,(300,200),125,(255),-1) #circulo blanco
XOR = cv2.bitwise_xor(img1,img2) #operador XOR entre las dos imagenes para obtener la diferencia simétrica
cv2.imshow('XOR', XOR) #muestra la imagen XOR
cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.bitwise_and y mask
#Operador AND entre las dos imagenes con mascara
captura = cv2.VideoCapture(0) #captura de video
mask = np.zeros((480,640),dtype=np.uint8) #crea una mascara negra
mask = cv2.circle(mask,(320,240),125,(255),-1) #crea un circulo blanco en la mascara
mask=cv2.bitwise_not(mask) #invierta la mascara para obtener el fondo
cv2.imshow('mask',mask) #muestra la mascara
while (captura.isOpened()): #verifica si la captura de video esta abierta
  ret,frame = captura.read() #lee un frame del video
  
  if ret == True: #verifica si se ha leido correctamente el frame
    imgMask = cv2.bitwise_and(frame,frame,mask=mask) #aplica la mascara al frame
    cv2.imshow('video',imgMask) #muestra el video con la mascara
    if cv2.waitKey(1) & 0xFF == ord('s'): #verifica si se ha presionado la tecla 's'
      break
  else: break
captura.release() #libera la captura de video
cv2.destroyAllWindows()  
