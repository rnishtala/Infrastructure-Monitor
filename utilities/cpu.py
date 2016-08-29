# @Author: rnishtala
# @Date:   2016-08-18T19:30:16-04:00
# @Last modified by:   rnishtala
# @Last modified time: 2016-08-18T23:06:17-04:00

import random
from random import randrange

class cpu:
    """
    This class has methods that generate random cpu id and usage
    
    It is called from the generateLogs module
    """
    def random_cpu(self):
        """
         * generates cpu id
         * @return {int} (cpu id)
         """
        return randrange(0, 2)


    def random_usage(self):
        """
         * Generate random CPU usage
         * @return {int} (cpu usage)
        """
        return randrange(0, 101)
