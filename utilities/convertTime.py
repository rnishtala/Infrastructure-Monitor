# @Author: rnishtala
# @Date:   2016-08-18T14:06:12-04:00
# @Last modified by:   rnishtala
# @Last modified time: 2016-08-18T23:07:01-04:00

import datetime
from time import strftime
import time

class convertTime:
    """
     This class has a method to convert unix time to a human readable format

     The format is (Y-m-d H:M:S)

     This class is called from the query module
    """
    def convertTime(self,time):
        """
         * converts unix time to human readable date and time in format Y-m-d H:M:S
         * @param  {float} time (unix time)
         * @return {datetime}  (date and time)
        """
        return datetime.datetime.fromtimestamp(float(time)).strftime('%Y-%m-%d %H:%M:%S')
