import urllib.request
import ssl

def url_reader(dir_remota, file_name):
    """
    Función que recibe como parámetro una URL donde se encuentra un log.

    Atributos: 
        dir_remota (string): url válida para realizar la obtención del archivo. 
        file_name (string): nombre del archivo.
    """
    ssl._create_default_https_context = ssl._create_unverified_context
    try: 
        log_file = urllib.request.urlopen(dir_remota)
    except urllib.request.HTTPError as e:
        print('HTTPError = ' + str(e.code))
    except urllib.request.URLError as e:
        print('URLError = ' + str(e.reason))
    except Exception:
        import traceback
        print('ocurrión una excepción: ' + traceback.format_exc())
    
    try:
        log_save(log_file.read(), file_name, 'wb')
    except Exception:
        print('no existe contenido para el archivo')
    
    
def log_save(content, file_name, write_mode):
    """
    Función que crea un archivo y almacena el contenido obtenido por log_reader.

    Atributos:
        content (byte): contenido encontrado 
    """
    try:
        result_file = open(file_name+'.log', write_mode)
        result_file.write(content)
        result_file.close()
    except (OSError, IOError) as err:
        print('Ocurrió un error al guardar el archivo: ', err)

def log_search(file_name, keyword):
    """
    Función que recibe como parámetro un nombre de archivo de log, y una palabra clave para realizar
    la búsqueda y crea un archivo nuevo con el resultado de la búsqueda.

    Atributos: 
        file_name (string): nombre del archivo log.
        keyword (string): palabra clave a buscar dentro del archivo cargado.
    """
    search_result = []
    with open(file_name, 'r') as log_file:
        for line in log_file:
            if keyword in line:
                search_result.append(line)
    return search_result
    #log_save(search_result, 'SearchResult', 'w') 