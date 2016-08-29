# @Author: rnishtala
# @Date:   2016-08-13T09:14:44-04:00
# @Last modified by:   rnishtala
# @Last modified time: 2016-08-19T09:36:23-04:00


import os
import datetime
import yaml
import socket
import utilities

def runQuery(query, parsed_ips):
    """
     * Parses through the dictionary of IP addresses and retrives timestamp and CPU usage
     * @param  {string} query (query entered by user)
     * @param  {dictionary} parsed_ips (dictionary of IP addresses with timestamp and CPU data)
     * Format of the dictionary: {ip:{timestamp:(cpu_usage,cpu_id)}}
     * @return {none}  none
     """
    cpu0 = {}
    cpu1 = {}
    cpu1Usage = {}
    cpu0Usage = {}
    ip = query.split(" ")[1]
    cpu_id = query.split(" ")[2]
    start_time_str = query.split(" ")[3] + " " + query.split(" ")[4]
    # Capture seconds as 00
    start_time_str = start_time_str + ":00"
    end_time_str = query.split(" ")[5] + " " + query.split(" ")[6]
    end_time_str = end_time_str + ":00"
    # capture start and end times
    start_time = datetime.datetime.strptime(
        start_time_str, '%Y-%m-%d %H:%M:%S')
    end_time = datetime.datetime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S')
    usageTimes = parsed_ips.get(ip)
    # if ip not found
    if usageTimes == None:
        print("IP not found")
        return
    # for queried IP store usage times for both CPU IDs
    for usageTime in usageTimes:
        timeKeyStr = list(usageTime.keys())[0]
        timeKey = datetime.datetime.strptime(timeKeyStr, '%Y-%m-%d %H:%M:%S')
        if timeKey >= start_time and timeKey <= end_time:
            if usageTime.get(timeKeyStr)[1] == 1:
                cpu1Usage[timeKey] = usageTime.get(timeKeyStr)[0]
            else:
                cpu0Usage[timeKey] = usageTime.get(timeKeyStr)[0]
    for usageTime in usageTimes:
        timeKeyStr = list(usageTime.keys())[0]
        if usageTime.get(timeKeyStr)[1] == 1:
            cpu1 = {'CPU 1 usage on ' + ip: cpu1Usage}
        else:
            cpu0 = {'CPU 0 usage on ' + ip: cpu0Usage}
    # Display and store results
    if cpu1 and cpu_id == '1':
        print(yaml.dump(cpu1, default_flow_style=False))
        with open(ip + '-summary.yml', 'w') as outfile:
            outfile.write(yaml.dump(cpu1, default_flow_style=False))
    if cpu0 and cpu_id == '0':
        print(yaml.dump(cpu0, default_flow_style=False))
        with open(ip + '-summary.yml', 'a') as outfile:
            outfile.write(yaml.dump(cpu0, default_flow_style=False))
    print(ip + "-summary.yml generated")
    outfile.close()


def main():
    """
     * This function parses lines and stores ip addresses in a dictionary
     * It also starts a while loop to query until the user chooses to exit
     * @return {none} none
    """
    validate = utilities.validate()
    ipv4check =  utilities.ipv4check()

    ipAddrs = {}
    query = ""
    try:
        filename = input("Enter a log file generated:")
        print('Reading from file: ' + filename)
        with open(filename, 'r') as file:
            lines = file.readlines()
    except(IOError, OSError) as e:
        print('File not found')
        exit()

        # Parse through lines and store IP addresses with CPU id and usage in a
        # dictionary
    for line in lines:
        timeUsage = {}
        ipFound = line.split(" ")[1]
        time = line.split(" ")[0]
        timeconvert = utilities.convertTime()
        convertedTime = timeconvert.convertTime(time)
        cpuUsage = int(line.split(" ")[3])
        cpu_id = int(line.split(" ")[2])
        timeUsage[convertedTime] = ("(" + str(cpuUsage) + "%" + ")", cpu_id)
        if ipAddrs.get(ipFound) == None:
            ipAddrs[ipFound] = [timeUsage]
        else:
            ipAddrs.get(ipFound).append(timeUsage)
    # Enter query to begin parsing
    while True:
        query = input(">")
        print("query entered: " + query)

        if query == "exit" or query == "EXIT":
            exit()
        elif query == "":
            print(
                "Query Format: query <ip> <cpu_id(0/1)> <start datetime(Y-m-d H:M)> <end datetime(Y-m-d H:M)>")
            continue
        elif len(query.split(" ")) != 7:
            print(
                "Query Format: query <ip> <cpu_id(0/1)> <start datetime(Y-m-d H:M)> <end datetime(Y-m-d H:M)>")
            continue
        elif query.split(" ")[0] != "query" and query.split(" ")[0] != "QUERY":
            print(
                "Query Format: query <ip> <cpu_id(0/1)> <start datetime(Y-m-d H:M)> <end datetime(Y-m-d H:M)>")
            continue
        elif not ipv4check.isValid_ipv4(query.split(" ")[1]):
            print(
                "Query Format: query <ip> <cpu_id(0/1)> <start datetime(Y-m-d H:M)> <end datetime(Y-m-d H:M)>")
            continue
        elif query.split(" ")[2] != "0" and query.split(" ")[2] != "1":
            print(
                "Query Format: query <ip> <cpu_id(0/1)> <start datetime(Y-m-d H:M)> <end datetime(Y-m-d H:M)>")
            continue
        elif not validate.validate(query.split(" ")[3] + " " + query.split(" ")[4]) and validate.validate(query.split(" ")[5] + " " + query.split(" ")[6]):
            print(
                "Query Format: query <ip> <cpu_id(0/1)> <start datetime(Y-m-d H:M)> <end datetime(Y-m-d H:M)>")
            continue
        runQuery(query, ipAddrs)

if __name__ == "__main__":
    main()
