import requests, xmltodict, json

def loadRSS():
    # API url to grab user data
    request = "https://www.learnsteps.com/feed/"
    # Sending get request
    response = requests.get(request)
    return response

def parseXML(response):
    data = xmltodict.parse(response.text)
    return data

def main():
    response = loadRSS()
    newsitems = json.dumps(parseXML(response), indent=4)
    print(newsitems)

if __name__ == "__main__":
    main()