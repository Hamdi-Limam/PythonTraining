# Import the regular expression module
import re

# Function to add request dictionary to a list
def list_requests():
    request_list = []
    with open("example.log", "r") as file:
        for line in file:
            r = re.match(r'^(?P<date>\d{1,2}\/\d{2}\/\d{4})\s(?P<time>\d{2}:\d{2})\s(?P<request>\w+)\s\w+\s(?P<status>\w+=\d+)$', line)
            if r.group(4).find("success") != -1:
                request_list.append(r.groupdict())
    return request_list

# Function to extract request details form the list
def extract_request(request_item):
        hours = int(request_item['time'][0:2])
        request_name = request_item['request']
        date = request_item['date']
        return  date, hours, request_name

# Function to count success per request and hour
def count_sucess_per_hour_name(date, hours, request_name, request_list, success):
    j = 0
    while int(request_list[j]['time'][0:2]) - hours == 0:
        if request_name==request_list[j]['request']:
            success += int(request_list[j]['status'][len(request_list[j]['status'])-1])
            request_list.remove(request_list[j])
            if len(request_list) == 0:
                return success
            elif len(request_list) == 1:
                j = 0
        elif len(request_list) == 1 and request_name!=request_list[0]['request']:
            return success
        else:
            j += 1
    return success


if __name__ == "__main__":
    request_list = list_requests()

    while len(request_list) != 0:
        date, hours, request_name = extract_request(request_list[0])
        success = count_sucess_per_hour_name(date, hours, request_name, request_list, 0)
        print(f"{date} {hours}:00 {request_name} {success}")
        
