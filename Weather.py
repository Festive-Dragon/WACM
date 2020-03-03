from urllib.request import urlopen

link = 'http://www.wttr.in/Perth?A'

wget = urlopen(link)

webtext= wget.read()

print(webtext.decode('utf-8'))