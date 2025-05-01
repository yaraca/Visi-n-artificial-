# #Detección de movimiento con operaciones morfológicas

import cv2 # Importar la librería OpenCV
import numpy as np # Importar la librería NumPy
import os # Importar la librería OS para manejar rutas de archivos

# Definir el path del video
vid_path = 'video1.mp4'  # Reemplaza con tu ruta
output_path = os.path.splitext(vid_path)[0] + '_out.mp4'  # Mismo nombre + "_out"

# Inicializar video y background subtractor
cap = cv2.VideoCapture(vid_path) # Cargar el video
backSub = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=True) # Crear el objeto de sustracción de fondo

# Verificar apertura
if not cap.isOpened():
    print("Error al abrir el video")
    exit()

# Obtener propiedades del video original para configurar el guardado
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # Ancho del video
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # Alto del video
fps = cap.get(cv2.CAP_PROP_FPS) # Frames por segundo

# Crear el objeto para escribir el video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height)) # Crear el objeto VideoWriter para guardar el video procesado

# Parámetros
min_contour_area = 800 # Área mínima del contorno para considerar un objeto
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)) # Elemento estructurante para operaciones morfológicas

# Fase de calentamiento
for _ in range(30): # Calentar el sustractor de fondo
    ret, frame = cap.read() # Leer el primer frame
    if not ret: # Si no se puede leer el frame, salir
        break
    backSub.apply(frame) # Aplicar el sustractor de fondo

# Bucle principal
while cap.isOpened(): # Mientras el video esté abierto
    ret, frame = cap.read() # Leer un frame
    if not ret: # Si no se puede leer el frame, salir
        break

    blurred = cv2.GaussianBlur(frame, (5, 5), 0) # Aplicar desenfoque gaussiano para reducir ruido
    fg_mask = backSub.apply(blurred) # Aplicar el sustractor de fondo
    _, mask_thresh = cv2.threshold(fg_mask, 200, 255, cv2.THRESH_BINARY) # Umbralizar la máscara de fondo
    mask_clean = cv2.morphologyEx(mask_thresh, cv2.MORPH_OPEN, kernel) # Operación morfológica de apertura para eliminar ruido
    mask_clean = cv2.morphologyEx(mask_clean, cv2.MORPH_CLOSE, kernel) # Operación morfológica de cierre para rellenar huecos
    contours, _ = cv2.findContours(mask_clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Encontrar contornos en la máscara limpia

    frame_out = frame.copy() # Copiar el frame original para dibujar los contornos
    for cnt in contours: # Para cada contorno encontrado
        area = cv2.contourArea(cnt) # Calcular el área del contorno
        if area > min_contour_area: # Si el área es mayor que el mínimo
            x, y, w, h = cv2.boundingRect(cnt) # Obtener el rectángulo delimitador del contorno
            if w > 20 and h > 20: # Si el ancho y alto son mayores que 20
                cv2.rectangle(frame_out, (x, y), (x + w, y + h), (0, 0, 255), 2) # Dibujar el rectángulo en el frame de salida

    # Mostrar en pantalla
    cv2.imshow('Deteccion de Movimiento', frame_out)

    # Guardar frame procesado
    out.write(frame_out)

    if cv2.waitKey(30) & 0xFF == ord('s'): # Esperar 30 ms y salir si se presiona 's'
        break

# Liberar recursos
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Video guardado como: {output_path}")






