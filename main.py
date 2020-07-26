from modules import logSearch as search
from modules import logReader as reader

reader.url_reader(
    'https://remoteurl.com/log/filename_without_extension', 'desired_file_name')

search.log_search(
    'C:\route_to_file\logfile.log', 'keyword')
