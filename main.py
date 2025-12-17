import sys
from pathlib import Path
print('Ejecutando el script de python')
nombre = sys.argv[1]
edad = sys.argv[2]
# file_path = Path(sys.argv[3])

# if not file_path.exists():
#     raise FileNotFoundError(f"No existe el archivo: {file_path}")

# with file_path.open() as f:
#     for line in f:
#         print(line.strip())
        
print('Mostrando variables de parametros')
print(f"El nombre pasado por parámetros es : {nombre}")
print(f"La edad pasada por parámetro es : {edad}")
