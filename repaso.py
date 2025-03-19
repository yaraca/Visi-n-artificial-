import cv2

billete = cv2.imread("billete.jpg")
rostro = cv2.imread("rostro.jpg")

#converti a escala de grises
billete_gris = cv2.cvtColor(billete, cv2.COLOR_BGR2GRAY)
rostro_gris = cv2.cvtColor(rostro, cv2.COLOR_BGR2GRAY)

#definir los métodos a utilizar
metodos = [cv2.TM_CCOEFF_NORMED, cv2.TM_SQDIFF] #métodos de comparación 

for metodo in metodos: #recorrer los métodos
    #aplicar el template matching
    resultado = cv2.matchTemplate(billete_gris, rostro_gris, metodo) #aplicar el método
