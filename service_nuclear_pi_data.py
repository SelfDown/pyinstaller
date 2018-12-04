#!/usr/bin/env python
# -*- coding: utf_8 -
from json_str_ws import strJSONWS
from position import getPosition
from parse_json import parseJSON
def getData(collection):
	print collection
	# 判断页数是否正确
	page = int(collection['page'])
	limit = int(collection['limit'])
	if page<=0 or limit < 1:
		return {"data":[],"page":page,"total":0,"success":False}
	start = (page-1)*limit


	where = " " 
	if where:
		where =" where number like '%"+str(collection['search'])+"%' or title like '%"+str(collection['search'])+"%'"

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
		data = getPosition(data,collection['service'],collection['ID'])
		# data =json.loads((json.dumps(data)))
		c.execute(countSql)
		count = c.fetchone()
		c.close()
		return {"page":page,"count":list(count)[0],"data":data,"success":True}
	if collection['way']=="mysql":
		import MySQLdb
		import json
		sql ="select "+str(collection['fields'])+" from "+str(collection['view_or_table'])+" "+where+" limit "+str(limit)+" offset "+str(start)
		print sql
		# 查询总数
		countSql='SELECT count('+str(collection["ID"])+') FROM '+str(collection['view_or_table'])+''+where
		conn=MySQLdb.connect(collection['host'],collection['user'],collection['password'],collection['database'], charset='utf8')    
		c=conn.cursor()
		c.execute(sql)
		data = c.fetchall()
		data = parseJSON(str(collection['fields']),data)
		data = getPosition(data,collection['service'],collection['ID'])
		# data =json.loads((json.dumps(data)))
		c.execute(countSql)
		count = c.fetchone()
		c.close()
		return {"page":page,"count":list(count)[0],"data":data,"success":True}
	return {"data":[],"page":page,"count":0,"success":False}