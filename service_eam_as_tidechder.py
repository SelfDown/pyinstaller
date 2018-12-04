#!/usr/bin/env python
# -*- coding: utf_8 -
from json_str_ws import strJSONWS
from position import getPosition
from parse_json import parseJSON
def readSQL():
	f = open("eam_where.sql")
	return f.read()

def getData(collection):
	print collection
	# 判断页数是否正确
	page = int(collection['page'])
	limit = int(collection['limit'])
	if page<=0 or limit < 1:
		return {"data":[],"page":page,"total":0,"success":False}
	start = (page-1)*limit
	where  = readSQL()

	if collection['search']:
		where += " and (EQUIPMENT_NUMBER like '%"+collection['search']+"%' or EQUIPMENT_NAME like '%"+collection['search']+"%')";
	
	

	if collection['way']=="sqlite":
		import sqlite3
		import json
		sql ="select "+str(collection['fields'])+" from "+str(collection['view_or_table'])+" "+where+" limit "+str(limit)+" offset "+str(start)
		print sql
		# 查询总数
		countSql='SELECT count('+str(collection["ID"])+') FROM '+str(collection['view_or_table'])+''+where
		conn=sqlite3.connect(str(collection['url']))    
		c=conn.cursor()
		c.execute(sql)
		data = c.fetchall()
		data = parseJSON(str(collection['fields']),data)
		data =json.loads((json.dumps(data)))
		c.execute(countSql)
		count = c.fetchone()
		c.close()
		#data = getPosition(data,collection['view_or_table'],collection['ID'])
		return {"page":page,"count":list(count)[0],"data":data,"success":True}
	if collection['way']=="hana":
		import pyhdb
		import json
		where +=' and  REVISION_STATUS=\''+'已发布'.decode("utf-8")+'\' '
		sql ="select "+str(collection['fields'])+" from "+str(collection['view_or_table'])+" "+where+" limit "+str(limit)+" offset "+str(start)
		print sql
		# 查询总数
		countSql='SELECT count('+str(collection["ID"])+') FROM '+str(collection['view_or_table'])+''+where
		conn=pyhdb.connect(host=str(collection['host']),port=int(collection['port']),user=str(collection['user']),password=str(collection['password']))	 
		c=conn.cursor()
		c.execute(sql)
		data = c.fetchall()
		data = parseJSON(str(collection['fields']),data)
		data =json.loads((json.dumps(data)))
		c.execute(countSql)
		count = c.fetchone()
		c.close()
		#data = getPosition(data,collection['view_or_table'],collection['ID'])
		return {"page":page,"count":list(count)[0],"data":data,"success":True}
	return {"data":[],"page":page,"count":0,"success":False}