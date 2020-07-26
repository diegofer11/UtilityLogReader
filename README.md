This is a simple Python utlity to load log files from a url or to searh keyword in a local log file.

`Example of use:`

```
from modules import logSearch as search
from modules import logReader as reader

reader.url_reader(
    'https://remoteurl.com/log/filename_without_extension', 'desired_file_name')

search.log_search(
    'C:\route_to_file\logfile.log', 'keyword')

```
It will create a file called search_result.log.