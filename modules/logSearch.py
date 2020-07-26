import modules.logSave as save
import io


def log_search(file_name, keyword):
    """
    Takes a file name and keyword to do a search, the result is a new file
    with the search result.

    Attributes:
        file_name (string): log file name.
        keyword (string): keyword to search inside the log file given.
    """
    with io.open(file_name, 'r', encoding="utf-8") as log_file:
        for line in log_file:
            if keyword in line:
                save.log_save(line, 'search_result', 'a+')
