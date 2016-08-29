README
======

Instructions for Generating logs:
--------------------------------
  Help
    python generateLogs -h
  Executing command
    python generateLogs.py [options]

    Ex: python generateLogs.py --logfile eventlog --date 2014-08-30

  Note : Logs will be generated in the same directory by default, otherwise please specify the complete
  path of the log file (Ex:/var/log/eventlog)

Instructions for querying logs:
-------------------------------
  Executing command:
    python query.py

    Enter a log file generated:<complete path of log file> (Ex: /var/log/eventlog)

    (Wait for prompt)

    >query 192.168.10.1 1 2016-08-17 00:00 2016-08-18 00:00

    >exit

Assumptions:
------------
The logs are written to one centralized log file, which has logs from all servers

The ip range used is 192.168.10.16 - 192.168.13.246 (1000 servers)

Logs are written every 0.057 second to simulate volume from 1000 servers logging every minute
(i.e 1000 logs per minute)

The scripts have been tested in a linux environment

Please use python version 3.5.2 (> 3.5)

The default log file name is syslog

The default date is 2014-10-31
