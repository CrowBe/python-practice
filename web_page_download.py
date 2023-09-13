# Basic web scraper to practice using standard python modules for more advanced implementations
# https://docs.python.org/3.11/library/urllib.html#module-urllib

from urllib import request

target_url = "http://" + input("Enter a web page url to download: ")
# Fetch the http response
web_page = request.urlopen(target_url)

data = web_page.read()

file_name = input("Enter a file name: ") + '.html'
file_to_write = open(file_name, 'w+')
file_to_write.write(data.decode('utf-8'))
file_to_write.close()