# @Author: rnishtala
# @Date:   2016-08-18T14:09:11-04:00
# @Last modified by:   rnishtala
# @Last modified time: 2016-08-18T23:07:24-04:00

import socket

class ipv4check:
    """
     This class has a method to check if an ipv4 address is valid

     It uses the socket library

     The class is called from the query module
    """
    def isValid_ipv4(self,address):
        """
         * Checks if ipv4 is valid
         * @param  {string}  address (ipv4)
         * @return {Boolean}
        """
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return True
