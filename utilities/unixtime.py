# @Author: rnishtala
# @Date:   2016-08-18T19:19:49-04:00
# @Last modified by:   rnishtala
# @Last modified time: 2016-08-18T23:06:37-04:00

import time

class unixtime:
    """
     This class has a method that ingests a datetime string
     and converts it into unixtime.

     This is called from the generateLogs module
    """
    def unixtime(self,current_datetime):
        """
         * calculates unix time
         * @return {timestamp} unix time
        """
        unixtime = time.mktime(current_datetime.timetuple())
        return unixtime
