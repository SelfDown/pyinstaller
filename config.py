#!/usr/bin/env python
# -*- coding: utf_8 -
piServer = {
	#{ip:Server}
}

def readJSON():
	import json
	file=open("config.json")
	content=file.read()
	# print content
	data=json.loads(content)
	return data
config = readJSON()

def getTemplate(name):
	global config
	return config["collection"][name]