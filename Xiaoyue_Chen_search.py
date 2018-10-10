# encoding: utf-8
import json
import sys
from lxml import etree as ET
result = set() #create a set to store results
script,xmlfile,keys = sys.argv  # get the input xmlfile and keys

tree = ET.parse(xmlfile)
keys = keys.split(' ')
for k in keys:
	k = k.lower() #not case-sensitive
	res = tree.xpath('//keyword[text()="'+k+'"]')  
	if(res != None):
		Xpath = '//entry[keyword = "'+k+'"]/ids/id/text()'
		for id in tree.xpath(Xpath):
			result.add(id.encode('utf-8'))


#if do not find keywords, give an arlert
if len(result) is 0:
	print("no such keywords :(")
else:
	print("list of ids of prizes:",result)