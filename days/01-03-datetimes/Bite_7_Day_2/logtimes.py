from datetime import datetime
import sys
import os
import re
from pathlib import Path
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

this_file = Path(__file__).resolve()
app_path = this_file.parent
sys.path.insert(0, str(app_path))

# prep: read in the logfile
# logfile = os.path.join('/tmp', 'log')
logfile = app_path / 'tmp' / 'log.txt'


urllib.request.urlretrieve('http://bit.ly/2AKSIbf', filename=logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    int_list = list(map(int, re.findall(r'\d+',line)))
    dt = datetime(int_list[0], int_list[1], int_list[2], int_list[3], int_list[4], int_list[5])
    return dt


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    sd_list = []

    for line in loglines:
        if re.search('Shutdown',line) is not None:
            sd_list.append(line)
    first_sd = convert_to_datetime(sd_list[0])
    final_sd = convert_to_datetime(sd_list[-1])
    time_btw_sd = final_sd - first_sd
    return time_btw_sd