# coding=utf-8
import sys
import json
from lxml import etree as ET

#get the filename and output xml name
args = sys.argv[:]
filename = args[1]
xmlname=args[2]

#open the json file
f = open(filename)
prize_data = json.load(f)  

#get the root node
for key,value in prize_data.items():
    root = ET.Element(key)
#recursion 
for index in prize_data['prizes']:
	category = ET.SubElement(root,index['category'])
	for lau in index['laureates']:
		attribute = {'id':lau['id'],"year":index['year']}
		laureates = ET.SubElement(category,'laureate',attrib=attribute)
		for subele,val in lau.items():
			if(subele not in['id']):
				v = ET.SubElement(laureates,subele)
				v.text = val


#generate the tree
tree = ET.ElementTree(root)
tree.write(xmlname, pretty_print=True,xml_declaration=True,encoding="utf-8")


