#Operaciones geométricas

#redimensionalización de imagenes
import numpy as np
import cv2
 
img = cv2.imread('perritos3.jpg') #Cargar la imagen
#Indicar el factor de escala
res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC) #redimensionar la imagen
#indicar manualmente el nuevo tamaño deseado de la iamgen
height, width = img.shape[:2] #obtener el tamaño de la imagen original
res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC) #redimensionar la imagen
cv2.imshow('imgagen original',img) #mostrar la imagen redimensionada
cv2.imshow('imgagen redimensionada',res) #mostrar la imagen redimensionada
cv2.waitKey(0)
cv2.destroyAllWindows()


#traslación de imagenes	
img = cv2.imread('perritos3.jpg',0) #Cargar la imagen
rows,cols = img.shape #obtener el tamaño de la imagen
M = np.float32([[1,0,210],[0,1,20]]) #definir la matriz de transformación
dst = cv2.warpAffine(img,M,(cols,rows))  #aplicar la transformación a la imagen
cv2.imshow('imgagen trasladada',dst) #mostrar la imagen trasladada
cv2.waitKey(0)
cv2.destroyAllWindows()



#rotación de imagenes
img = cv2.imread('perritos3.jpg',0) #Cargar la imagen
rows,cols = img.shape #obtener el tamaño de la imagen
M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1) #definir la matriz de transformación
dst1 = cv2.warpAffine(img,M,(cols,rows)) #aplicar la transformación a la imagen
cv2.imshow('imagen rotada',dst1) #mostrar la imagen rotada
cv2.waitKey(0)
cv2.destroyAllWindows()


#transformación afín de imagenes
import matplotlib.pyplot as plt #carga la librería para graficar
img = cv2.imread('cuadricula.png') #Cargar la imagen
rows,cols,ch = img.shape #obtener el tamaño de la imagen
 
pts1 = np.float32([[100,400],[400,100],[100,100]]) #definir los puntos de la imagen original
pts2 = np.float32([[50,300],[400,200],[80,150]]) #definir los puntos de la imagen transformada
 
M = cv2.getAffineTransform(pts1,pts2) #definir la matriz de transformación
dst = cv2.warpAffine(img,M,(cols,rows)) #aplicar la transformación a la imagen
 
plt.subplot(121),plt.imshow(img),plt.title('Input') #mostrar la imagen original
plt.subplot(122),plt.imshow(dst),plt.title('Output') #mostrar la imagen transformada
plt.show()



#transformación de perspectiva de imagenes
img = cv2.imread('perrito4.jpeg') #Cargar la imagen
rows,cols,ch = img.shape #obtener el tamaño de la imagen
 
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])  #definir los puntos de la imagen original
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]]) #definir los puntos de la imagen transformada
 
M = cv2.getPerspectiveTransform(pts1,pts2) #definir la matriz de transformación
 
dst = cv2.warpPerspective(img,M,(300,300)) #aplicar la transformación a la imagen
  
plt.subplot(121),plt.imshow(img),plt.title('Input') #mostrar la imagen original
plt.subplot(122),plt.imshow(dst),plt.title('Output') #mostrar la imagen transformada
plt.show()
