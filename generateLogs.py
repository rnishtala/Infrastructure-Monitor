# @Author: rnishtala
# @Date:   2016-08-10T22:25:33-04:00
# @Last modified by:   rnishtala
# @Last modified time: 2016-08-19T09:36:36-04:00

import logging
from optparse import OptionParser
from time import strftime
import time
from datetime import timedelta, date, datetime
import ipaddress
import utilities


def generate_log(logfile, current_datetime, ip):
    """
     * This function generates logs in the format {unixtime IP CPU_id usage}
     * @param  {string} logfile
     * @param {datetime} datetime
     * @return {none}  none
    """
    logging.basicConfig(filename=logfile,
                        format='%(message)s',
                        level=logging.INFO)

    unixtime = utilities.unixtime()
    cpu = utilities.cpu()

    logging.info('%s %s %s %s' % (unixtime.unixtime(current_datetime), ip , cpu.random_cpu(), cpu.random_usage()))


def read_options():
    """
     * This functions adds user entered options or uses default options to generate logs
     * The default options are {--logfile eventlog.log --date 2014-10-31}
     * As shown above the options are the <complete_path_of_log_with_name> and <date>
     * @return {OptionParser} (options)
    """
    parser = OptionParser(usage="usage: python generate_logs.py [options] ",
                          version="1.0")
    parser.add_option("-f", "--logfile", dest="logfile", help="Specify a log. Default = ./syslog",
                      default="syslog",
                      type="string")
    parser.add_option("-d", "--date", dest="datevar", help="Specify a date, default = 2014-10-31",
                      default="2014-10-31", type="string")
    (options, args) = parser.parse_args()
    return options


def main():
    """
     * This function reads command line options and generates IP addresses
     * The IP address range is 192.168.10.16 - 192.168.13.246
     * The logs are written every 0.057 of a second which estimates to 1000
     * logs per per minute
     * Each of the logs within a minute are from different servers
     * @return {none} none
    """
    options = read_options()
    current_date_string = options.datevar
    current_datetime_string = options.datevar + " 00:00:00"
    current_datetime = datetime.strptime(
        current_datetime_string, "%Y-%m-%d %H:%M:%S")
    run_time = current_datetime + timedelta(hours=24)
    print("Run until:" + run_time.strftime("%Y-%m-%d %T:%M:%S"))
    print("Log generation will complete in ~ 140 seconds")
    count = 0
    num_servers = 1000
    start_ip = ipaddress.IPv4Address('192.168.10.16')
    ip = start_ip
    while(current_datetime < run_time):
        generate_log(options.logfile, current_datetime, str(ip))
        current_datetime = current_datetime + timedelta(seconds=0.057)
        count = count + 1
        if count == num_servers-1:
            count = 0
        ip = start_ip + count
    print("Log file: " + options.logfile + " generated")


if __name__ == "__main__":
    main()
