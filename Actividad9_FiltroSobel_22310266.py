import cv2
 
#Leer la imagen original
imagen = cv2.imread('perrito2.jpg')
img = cv2.resize(imagen, (456,289)) #redimensionar la imagen
#Mostrar la imagen original
cv2.imshow('Original', img)
cv2.waitKey(0)
 
#Convertir a escala de grises
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Difuminar la imagen para tener mejores resultados
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
 
#Detectar bordes usando el operador Sobel
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) #Eje X
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) #Eje Y
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) #Combinación de Ejes X y Y
#MOstrar imagenes con el operador Sobel en los ejes
cv2.imshow('Sobel X', sobelx) #Imagen en eje x
cv2.waitKey(0)
cv2.imshow('Sobel Y', sobely) #Imagen en eje y
cv2.waitKey(0)
cv2.imshow('Sobel X Y', sobelxy)  #Imagen en eje x y y
cv2.waitKey(0)
 
#Deteccion de bordes Canny
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) #detecta bordes
#Mostrar imagenes con el operador Canny
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
 
cv2.destroyAllWindows()