#!/usr/bin/env python
# -*- coding: utf_8 -

from parse_json import parseJSON
conn = sqlite3.connect('position.db')
def getData(collection):
	print collection
	# 判断页数是否正确
	target_service_name = collection['target_service_name']
	target_id = collection['target_id']
	if not (target_service_name or target_id):
		return {"data":[],"success":False}
	ids = target_id.split(",")
	ids = [ "'"+item+"'" for item in ids]
	sql_in = ",".join(ids)
	where =" where target_service_name = '"+target_service_name+"' and target_id in ("+sql_in+") order by create_time desc"
	if collection["way"] == "sqlite":
		import sqlite3
		global conn
		c = conn.cursor()	
		sql = "select "+str(collection['fields'])+" from "+collection['view_or_table']+" "
		sql += where
		c.execute(sql)
		data = c.fetchall()
		data = parseJSON(str(collection['fields']),data)
		#c.close()
		return {"data":data,"success":True}