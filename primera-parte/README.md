
# Documentación del Script de Procesamiento de Datos de Spotify de Taylor Swift

Este script de Python está diseñado para procesar datos extraídos de la API de Spotify relacionados con los álbumes y pistas de Taylor Swift, y guardar esta información en un archivo CSV.

## Estructura del Código

El código se divide en varias partes, cada una con una función específica:

### Importaciones

```python
import pandas as pd
import json
import os
```

Estas son las bibliotecas necesarias para el script:

- `pandas`: Utilizada para la manipulación de datos y para guardar los datos procesados en un archivo CSV.
- `json`: Necesaria para cargar y parsear los datos desde un archivo JSON.
- `os`: Usada para verificar la existencia del archivo CSV antes de intentar escribir en él.

### Función `load_data`

```python
def load_data(json_file):
    """Carga y devuelve los datos del archivo JSON."""
    with open(json_file, 'r') as file:
        return json.load(file)
```

- `json_file`: Ruta al archivo JSON que contiene los datos de Spotify.
- Esta función abre el archivo JSON, carga los datos usando `json.load` y los devuelve.
- Utiliza un bloque `with` para asegurar que el archivo se cierre correctamente después de cargar los datos.

### Función `process_data`

```python
def process_data(data):
    """Procesa los datos JSON y devuelve una lista de registros de pistas."""
    return [
        {
            # ... (campos del registro de la pista)
        }
        for album in data['albums'] for track in album['tracks']
    ]
```

- `data`: Datos JSON cargados de Spotify.
- Esta función utiliza una comprensión de lista para iterar sobre cada álbum y cada pista dentro del álbum.
- Para cada pista, se crea un diccionario que contiene información relevante como el número de disco, duración, popularidad, ID de la pista, características de audio, etc.
- Devuelve una lista de estos diccionarios.

### Función `save_to_csv`

```python
def save_to_csv(df, csv_file):
    """Guarda el DataFrame en un archivo CSV, lo crea si no existe y lo edita si existe."""
    file_exists = os.path.isfile(csv_file)
    with open(csv_file, 'a' if file_exists else 'w', newline='', encoding='utf-8') as f:
        df.to_csv(f, header=not file_exists, index=False)
```

- `df`: DataFrame de Pandas que contiene los datos procesados.
- `csv_file`: Ruta al archivo CSV donde se guardarán los datos.
- Esta función verifica primero si el archivo CSV ya existe.
- Abre el archivo CSV en modo de añadir (`'a'`) si ya existe o en modo de escritura (`'w'`) si no existe.
- Guarda el DataFrame en el archivo CSV, asegurándose de no duplicar los encabezados si el archivo ya existe.

### Procesamiento Principal

```python
# Configuración
json_file_name = 'taylor_swift_spotify.json'
csv_file_name = 'dataset.csv'

# Procesamiento
try:
    data = load_data(json_file_name)
    tracks_data = process_data(data)
    df_tracks = pd.DataFrame(tracks_data)
    save_to_csv(df_tracks, csv_file_name)
except Exception as e:
    print(f"Error: {e}")
```

- Define los nombres de los archivos JSON y CSV.
- Envuelve el proceso de carga, procesamiento y guardado de datos en un bloque `try-except` para manejar cualquier error que pueda ocurrir durante el proceso.
- Carga los datos desde el archivo JSON, procesa estos datos para obtener los registros de las pistas, crea un DataFrame de Pandas con estos registros, y luego guarda este DataFrame en un archivo CSV.
