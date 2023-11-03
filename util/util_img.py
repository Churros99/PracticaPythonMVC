import os
from PIL import Image, ImageTk

# Ruta de la carpeta que contiene las imágenes
carpeta_imagenes = './img'

# Crear una lista para almacenar los atributos de las imágenes
lista_imagenes = []

# Recorrer los archivos en la carpeta
for archivo in os.listdir(carpeta_imagenes):
    # Comprobar si el archivo es una imagen (puedes ajustar las extensiones según tus necesidades)
    if archivo.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        ruta_completa = os.path.join(carpeta_imagenes, archivo)
        nombre = os.path.basename(ruta_completa).split('.')[0]

        # Agregar los atributos a la lista de imágenes
        lista_imagenes.append({
            'Imagen': nombre,
            'Ruta': ruta_completa
        })

# Imprimir la lista de imágenes con los atributos
for imagen in lista_imagenes:
    print(imagen)
    print('\n')
    

class Img:
    Imagen:str
    Ruta:str

    def getImage(self, nombre, size):
        return ImageTk.PhotoImage(Image.open(self.Ruta).resize(size, Image.ADAPTIVE))
    
    def __init__(self, nombre, ruta):
        self.nombreImagen = nombre
        self.Ruta = ruta

