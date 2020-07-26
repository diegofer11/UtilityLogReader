def log_save(content, file_name, write_mode):
    """
    Creates a file and stores the content of the keyword search.

    Attributes:
        content (byte): content found according to the keywords
    """
    try:
        result_file = open(file_name + '.log', write_mode)
        result_file.write(content)
        result_file.close()
    except (OSError, IOError) as err:
        print('An error has occurred saving the file: ', err)