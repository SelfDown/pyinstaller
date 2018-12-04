#!/usr/bin/env python
# -*- coding: utf_8 -
import time
from parse_json import parseJSON
def getData(collection):
	print collection
	user_id = collection["user_id"]
	if not user_id:
		print "user_id is empty"
	if collection["way"] == "sqlite":
		import sqlite3
		conn = sqlite3.connect('position.db')
		c = conn.cursor()	
		sql = "select "+str(collection['fields'])+" from user_info_setting where user_id = '"+user_id+"'"
		c.execute(sql)
		data = c.fetchall()
		data = parseJSON(str(collection['fields']),data)
		c.close()
		return {"data":data,"success":True}