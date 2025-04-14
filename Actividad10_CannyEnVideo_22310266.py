import cv2

# Captura de video desde la cámara
captura = cv2.VideoCapture(0) # 0 para la cámara por defecto, 1 para la cámara externa
salida = cv2.VideoWriter('videoSalida.avi',cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480)) # Guardar el video en un archivo

while (captura.isOpened()):  # Verifica si la cámara está abierta
  ret, imagen = captura.read() # Lee un frame de la cámara
  if ret == True: # Verifica si se ha leído correctamente el frame
    cv2.imshow('video', imagen) # Muestra el frame en una ventana
    salida.write(imagen) # Guarda el frame en el archivo de salida
    if cv2.waitKey(1) & 0xFF == ord('s'): # Espera a que se presione la tecla 's' para salir
      break
  else: break
captura.release() # Libera la cámara
salida.release() # Libera el archivo de salida
cv2.destroyAllWindows()