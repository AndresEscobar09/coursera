import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verrify_mode =ssl.CERT_NONE


url = 'http://py4e-data.dr-chuck.net/comments_1812510.xml'

uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
tree = ET.fromstring(data)

lst = tree.findall('comments/comment')

numbers = list()
for item in lst:
	x = item.find('count').text
	x = int(x)
	numbers.append(x)
total = 0
for num in numbers:
	total = total + num
print('total of numbers is:',total)



