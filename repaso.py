import cv2

billete = cv2.imread("billete.jpeg")
rostro = cv2.imread("rostro.jpeg")
billete2 = cv2.resize(billete, (300, 300))
rostro2 = cv2.resize(rostro, (100, 100))    

#converti a escala de grises
billete_gris = cv2.cvtColor(billete2, cv2.COLOR_BGR2GRAY)
rostro_gris = cv2.cvtColor(rostro2, cv2.COLOR_BGR2GRAY)

#definir los métodos a utilizar
metodos = [cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF] #métodos de comparación 

for metodo in metodos: #recorrer los métodos
    #aplicar el template matching
    resultado = cv2.matchTemplate(billete_gris, rostro_gris, metodo) #aplicar el método
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado) #obtener los valores de la coincidencia
    if metodo == cv2.TM_SQDIFF: #si el método es TM_SQDIFF
        x1, y1 = min_loc #obtener las coordenadas
        X2, y2 = min_loc[0] + rostro_gris.shape[1], min_loc[1] + rostro_gris.shape[0] #coordenadas de la esquina inferior derecha
    else:
        x1, y1 = max_loc #obtener las coordenadas
        x2, y2 = max_loc[0] + rostro_gris.shape[1], max_loc[1] + rostro_gris.shape[0] #coordenadas de la esquina inferior derecha 

#dibujar el rectángulo    
cv2. rectangle(billete, (x1,y1), (x2,y2), (0,0,125), 2)# dibujar el rectángulo
    #mostrar las imágenes
cv2.imshow("Imagen original", billete)
cv2.imshow("Template", rostro)
cv2.waitKey()
cv2.destroyAllWindows() #cerrar las ventanas 