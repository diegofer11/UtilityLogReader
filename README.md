# Utility Log Reader

Utility Log Reader is a Python program for dealing with log files, it allows to load the file from a url or a local file.

## Usage

```python
from modules import logSearch as search
from modules import logReader as reader

reader.url_reader(
    'https://remoteurl.com/log/filename_without_extension', 'desired_file_name')

search.log_search(
    'C:\route_to_file\logfile.log', ['keyword', 'another_keyword'])

```
It will create a file called search_result.log.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
