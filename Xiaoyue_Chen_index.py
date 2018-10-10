import sys
import json
from lxml import etree as ET

script,xmlfile,index_name = sys.argv

tree = ET.parse(xmlfile)
index=ET.Element('index')
dic = { }
for node in tree.xpath('//laureate'):
	motivation = node.xpath('./motivation/text()')
	id_name = int(node.get('id',''))
	if(motivation!=[]):
		words = ''.join(motivation).split(' ')
		for i in range(len(words)):
			if(words[i] not in['','.']):
				words[i] = words[i].replace('\"','')
				words[i] = words[i].replace(',','')

				words[i] = words[i].lower()
				id_name = int(node.get('id',''))
				if words[i] in dic:
					dic[words[i]].append(id_name)
				else:
					dic[words[i]]=[]
					dic[words[i]].append(id_name)

for key,value in dic.items():
	entry = ET.SubElement(index,'entry')
	keyword = ET.SubElement(entry,'keyword')
	keyword.text=key
	ids = ET.SubElement(entry,'ids')
	v = []
	for id_ in value:
		if(id_ not in v):
			id_num = ET.SubElement(ids,'id')
			id_num.text = str(id_)
			v.append(id_)
		
tree = ET.ElementTree(index)
tree.write(index_name, pretty_print=True)
