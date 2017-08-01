import sys
import requests
import json
import re
import time

## Convert every urls written in the input text file
## Usage : urlShortener.py [file_path]

API_key="[REPLACE WITH YOUR GOOGLE URL SHORTENER API KEY]"
GoogleURL = "https://www.googleapis.com/urlshortener/v1/url?key=" + API_key

def main(argv):
    originalFile = open(argv[1], 'r')
    convertedFile = open("./converted_" + time.strftime("%d-%m-%Y") + ".txt", 'w')
    while True:
        line = originalFile.readline()
        if not line: break
        shortedLine = replaceUrlWithShortened(line)
        convertedFile.write(shortedLine)

def replaceUrlWithShortened(string):
    extractedUrls = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', str(string))

    # return original string if it contains no url
    if not extractedUrls:
        return string

    for extractedUrl in extractedUrls:
        shortenedUrl = getShortUrl(extractedUrl)
        string = string.replace(extractedUrl, shortenedUrl)

    return string

def getShortUrl(url):
    data = json.dumps({'longUrl': url})
    result = requests.post(GoogleURL, headers={'content-type': 'application/json'}, data=data)
    shortURL = result.json()['id']
    return shortURL

if __name__ == '__main__':
  main(sys.argv)
