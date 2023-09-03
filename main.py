import pyshorteners
import re

url = input("Enter the URL: ")
print("Your URL: ", url)

def shorten_url(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))
    

def is_valid_url(url):
    # Regular expression to check if the URL starts with "http" or "https"
    pattern = r'^https?://'
    return bool(re.match(pattern, url))

shorten_url(url)

while True:
    url = input("Enter the URL (or 'exit' to quit): ")
    if url.lower() == 'exit':
        break
    if not is_valid_url(url):
        print("Invalid URL! Please make sure the URL starts with 'http' or 'https'.")
        continue




