#!/usr/bin/env python
# -*- coding: utf_8 -

from parse_json import parseJSON
def getData(collection):
	print collection
	# 判断页数是否正确
	page = int(collection['page'])
	limit = int(collection['limit'])
	if not (page or limit):
		return {"data":[],"page":page,"total":0,"success":False}
	start = (page-1)*limit
	if collection["way"] == "sqlite":
		import sqlite3
		conn = sqlite3.connect('position.db')
		c = conn.cursor()	
		sql = "select "+str(collection['fields'])+" from "+collection['view_or_table']+" "
		sql += " limit "+str(limit)+" offset "+str(start)
		c.execute(sql)
		data = c.fetchall()
		countSql='SELECT count('+str(collection["ID"])+') FROM '+str(collection['view_or_table'])
		c.execute(countSql)
		count = c.fetchone()
		data = parseJSON(str(collection['fields']),data)
		c.close()
		return {"data":data,"count":list(count)[0],"success":True}