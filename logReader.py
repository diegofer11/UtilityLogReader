import modules.logCreator as logger

logger.url_reader('https://srvvpcontrolcore.colsanitas.com/jboss/RIPSS/RipssScheduledTask.log', 'RipssTask')
#logger.url_reader('https://srvvpcontrolcore.colsanitas.com/jboss/RIPSS/catalina.out', 'Catalina')
#result = logger.log_search('RipssTask.log', '/persona')
#print(len(result))

