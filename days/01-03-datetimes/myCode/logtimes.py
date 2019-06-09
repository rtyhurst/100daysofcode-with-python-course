from datetime import datetime, timedelta
import os
import urllib.request
from typing import List

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
# logfile = os.path.join('/tmp', 'log')
logfile = os.path.join('./tmp', 'log')
file = os.path.isfile(logfile)
if not file:
    urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    log_lines: List[str] = f.readlines()


# for you to code:

def convert_to_datetime(line):
    """
       Extract timestamp from log_line and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
       :param line:
       :return: datetime
    """
    dt = line.split()[1]
    # dt = datetime(line.split()[1])
    return datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S')


def time_between_shutdowns(logLines):
    """
       Extract shutdown events ("Shutdown initiated") from log_lines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
       :param logLines: 
       :return: datetime.timedelta
    """
    shutdown: List[datetime] = []
    for line in logLines:
        if SHUTDOWN_EVENT in line:
            shutdown.append(convert_to_datetime(line))

    td = shutdown[1] - shutdown[0]
    return td


t_delta: timedelta = time_between_shutdowns(log_lines)
print(t_delta)
