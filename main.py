from modules import logSearch as search
from modules import logReader as reader

reader.url_reader(
    'https://srvvpcontrolcore.colsanitas.com/jboss/RIPSS/RipssPrestacionesEconomicasRS.log', 'PrestacionesEconomicas')

search.log_search(
    'C:\Repositorios\python\logfile.log', 'keyword')
