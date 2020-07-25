This is a simple Python utlity to load log files from a url or to searh keyword in a local log file.

This web service receives earth time formatted in Y-m-d H:i:s.u, then returns the mars sol date and mars coordinated time.

`Example of use:`

```
import logUtility.modules.logSearch as search

search.log_search('route_to_file\file_name.log', 'keyword')

```
It will create a file called search_result.log.