import os
#import urllib3
import urllib.parse
import urllib.request
import re

#http = urllib3.PoolManager()

cmd='figlet mpv-youtube'
os.system(cmd)

print("Search:")
query_string = urllib.parse.urlencode({'search_query' : input()})
search_url="https://www.youtube.com/results?" + query_string
print(search_url)
html_content=urllib.request.urlopen(search_url)
#print(html_content.read().decode())
search_results = re.findall(r'"videoId":"(.{11})"',html_content.read().decode())
urls=['https://www.youtube.com/watch?v='+ x for x in search_results[::4]]
#print(urls)
for x in range(0,len(urls)):
    print(x,'-',urls[x])

print('Choice:')
cmd='mpv '+urls[int(input())]
print(cmd)
os.system(cmd)
