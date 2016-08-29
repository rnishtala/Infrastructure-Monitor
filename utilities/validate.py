# @Author: rnishtala
# @Date:   2016-08-18T14:10:00-04:00
# @Last modified by:   rnishtala
# @Last modified time: 2016-08-18T23:06:50-04:00

import datetime

class validate:
    """
     This class has a method to validate if a user has entered the date and time
     in proper format.

     The format is (Y-m-d H:M)

     This class is used in the query module
    """
    def validate(self,date_text):
        """
         * Check if datetime is valid
         * @param  {string} date_text
         * @return {Boolean}
        """
        try:
            if date_text != datetime.datetime.strptime(date_text, '%Y-%m-%d %H:%M').strftime('%Y-%m-%d %H:%M'):
                raise ValueError
            return True
        except ValueError:
            return False
