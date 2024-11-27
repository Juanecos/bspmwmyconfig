
import os
import re

def renombrar(old,new):
    try:
        os.rename(old,new)
        print(f"Archivo renombrado de '{old}' a '{new}'.")
    except FileNotFoundError:
          print(f"El archivo '{old}' no existe.")
    except PermissionError:
          print("No tienes permisos para renombrar este archivo.")
    except Exception as e:
         print(f"Ocurrió un error: {e}")

# Ruta de la carpeta a leer


ruta = "musichere"

#ruta_carpeta = os.path.join(os.getcwd(), ruta)
ruta_carpeta= input("Ingresse la ruta de la carpeta con musica a la cual renombrar: ")
try:
    # Obtener la lista de archivos y carpetas
    print(f"Contenido de '{ruta_carpeta}':")
    
    for elemento in os.listdir(ruta_carpeta):
        
        sin_corchetes = re.sub(r'\s*\[.*?\]\s*', ' ', elemento)
        resultado = re.sub(r'\s+\.', '.', sin_corchetes).strip()
        ruta_absoluta=(ruta_carpeta+"/")
        renombrar(ruta_absoluta+elemento,ruta_absoluta+resultado)

              
except FileNotFoundError:
    print(f"La carpeta '{ruta_carpeta}' no existe.")
except PermissionError:
    print(f"No tienes permisos para acceder a la carpeta '{ruta_carpeta}'.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
