import modules.logSave as save
import io


def log_search(file_name, keyword):
    """
    Takes a file name and a list of keywords to perform a search, the result is a new file
    with the search result called search_result.log.

    Attributes:
        file_name (string): log file name.
        keywords (list): keywords to be used as search terms inside the log file given.
    """
    with io.open(file_name, 'r', encoding="utf-8") as log_file:
        for line in log_file:
            for key in keyword:
                if key in line:
                    save.log_save(line, 'search_result', 'a+')
