# Task 3: Given tasl.log file, try to parse them and get unique IP from where the requests are coming.
# Using string manipulation
def get_unique_ip_using_string_manipulation(file):
    log_ips = []
    for line in file:
        ip = line.split(" ")[2]
        if log_ips.count(ip) == 0:
            log_ips.append(ip)
    return log_ips

# Using regex
import re

def get_unique_ip_using_regex(file):
    log_ips = []
    for line in file:
        ip = re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
        if log_ips.count(ip.group()) == 0:
            log_ips.append(ip.group())
    return log_ips

with open("task3.log","r") as file:
    print("Getting unique IP using string manipulation:")
    print("\n".join(get_unique_ip_using_string_manipulation(file)))
with open("task3.log","r") as file:
    print("Getting unique IP using regex:")
    print("\n".join(get_unique_ip_using_regex(file)))