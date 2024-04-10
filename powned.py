import os  # Importa el módulo 'os' que proporciona funciones para interactuar con el sistema operativo.

def buscar_en_archivos(contraseña):  # Define una función llamada buscar_en_archivos que recibe una contraseña como argumento.
    try:  # Inicia un bloque de código que puede lanzar excepciones.
        archivos_encontrados = {}  # Inicializa un diccionario para almacenar las contraseñas encontradas junto con los archivos donde se encontraron.
        for root, dirs, files in os.walk(".", topdown=True):  # Itera sobre todos los archivos y directorios a partir del directorio actual.
            for archivo in files:  # Itera sobre los archivos en el directorio actual.
                if archivo.startswith("PDB-") and archivo.endswith(".txt"):  # Verifica si el archivo cumple con ciertas condiciones (comienza con "PDB-" y termina con ".txt").
                    ruta_archivo = os.path.join(root, archivo)  # Obtiene la ruta completa del archivo.
                    if verificar_contraseña(contraseña, ruta_archivo):  # Verifica si la contraseña está en el archivo.
                        if contraseña in archivos_encontrados:  # Verifica si la contraseña ya está en el diccionario de archivos encontrados.
                            archivos_encontrados[contraseña].append(ruta_archivo)  # Agrega la ruta del archivo al valor correspondiente de la contraseña en el diccionario.
                        else:
                            archivos_encontrados[contraseña] = [ruta_archivo]  # Agrega la contraseña y la ruta del archivo al diccionario si es la primera vez que se encuentra la contraseña.
        return archivos_encontrados  # Devuelve el diccionario de archivos encontrados.
    except Exception as e:  # Captura cualquier excepción que ocurra durante la ejecución del bloque try.
        print("Ocurrió un error:", e)  # Imprime un mensaje de error si ocurre una excepción.
        return {}  # Devuelve un diccionario vacío en caso de error.

def verificar_contraseña(contraseña, ruta_archivo):  # Define una función llamada verificar_contraseña que toma una contraseña y una ruta de archivo como argumentos.
    try:  # Inicia un bloque de código que puede lanzar excepciones.
        with open(ruta_archivo, 'rb') as archivo:  # Abre el archivo en modo de lectura binaria ('rb').
            for linea in archivo:  # Itera sobre cada línea del archivo.
                if contraseña.encode('utf-8') == linea.strip():  # Verifica si la contraseña codificada en UTF-8 coincide con la línea actual del archivo.
                    return True  # Devuelve True si la contraseña es encontrada en el archivo.
        return False  # Devuelve False si la contraseña no es encontrada en el archivo.
    except Exception as e:  # Captura cualquier excepción que ocurra durante la ejecución del bloque try.
        print(f"Error al abrir el archivo {ruta_archivo}: {e}")  # Imprime un mensaje de error si ocurre una excepción al abrir el archivo.
        return False  # Devuelve False en caso de error.

if __name__ == "__main__":  # Verifica si el script se está ejecutando directamente y no siendo importado como módulo.
    contraseña_introducida = input("Introduce la contraseña a verificar: ")  # Solicita al usuario introducir la contraseña a verificar.

    archivos_encontrados = buscar_en_archivos(contraseña_introducida)  # Llama a la función buscar_en_archivos para buscar la contraseña en los archivos.

    if archivos_encontrados:  # Verifica si se encontraron archivos que contienen la contraseña.
        print("La contraseña se encuentra en los siguientes archivos:")  # Imprime un mensaje indicando que la contraseña se encontró en algunos archivos.
        for contraseña, archivos in archivos_encontrados.items():  # Itera sobre el diccionario de archivos encontrados.
            print(f"Contraseña '{contraseña}' encontrada en los archivos:")  # Imprime la contraseña encontrada.
            for archivo in archivos:  # Itera sobre las rutas de los archivos donde se encontró la contraseña.
                print(archivo)  # Imprime la ruta del archivo.
    else:  # Si no se encontraron archivos que contienen la contraseña.
        print("La contraseña no se encuentra en ningún archivo.")  # Imprime un mensaje indicando que la contraseña no se encontró en ningún archivo.
