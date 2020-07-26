import ssl
import urllib.request

import modules.logSave as save_file


def url_reader(dir_remote, file_name):
    """
    Uses the given parameters to look for a log file and save it locally with
    the new name,

    Parameters:
        dir_remote (string): valid url to obtain the log file.
        file_name (string): file name to look in the location given.
    """
    ssl._create_default_https_context = ssl._create_unverified_context
    try:
        log_file = urllib.request.urlopen(dir_remote)
    except urllib.request.HTTPError as e:
        print('HTTPError = ' + str(e.code))
    except urllib.request.URLError as e:
        print('URLError = ' + str(e.reason))
    except Exception:
        import traceback
        print('an exception has occurred: ' + traceback.format_exc())

    try:
        save_file.log_save(log_file.read(), file_name, 'wb')
    except Exception:
        print('no content')
