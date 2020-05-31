
def log_search(file_name, keyword):
    """
    Función que recibe como parámetro un nombre de archivo de log, y una palabra clave para realizar
    la búsqueda y crea un archivo nuevo con el resultado de la búsqueda.

    Atributos: 
        file_name (string): nombre del archivo log.
        keyword (string): palabra clave a buscar dentro del archivo cargado.
    """
    search_result = ""
    with open(file_name, 'r') as log_file:
        for line in log_file:
            line = line.decode()
            if keyword in line:
                search_result.join(line)
    #to fix