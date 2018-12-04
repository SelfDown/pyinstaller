#!/usr/bin/env python
# -*- coding: utf_8 -
from json_str_ws import strJSONWS
from position import getPosition
from parse_json import parseJSON
from config import getTemplate
from service_3dmark_get import getData as get3DMarkup
import MySQLdb
import json
last_database_ip = ""
conn = None
def getData(collection):
	print collection
	# 判断页数是否正确
	page = int(collection['page'])
	limit = int(collection['limit'])
	if page<=0 or limit < 1:
		return {"data":[],"page":page,"total":0,"success":False}
	start = (page-1)*limit
	where = " where 1=1 " 
	if collection['search']:
		where +=" and ("
		fields = collection["search_fields"].split(",")
		first = True
		for item in fields:
			if first:
				where  +=' '+item+" like '%"+collection["search"]+"%'"
				first = False
			else:
				where +="or "+item+" like '%"+collection["search"]+"%'"
		where += " ) "
	
	if collection["search5"]:
		where +=" and ("
		fields5 = collection["search5_fields"]
		where += fields5+" in ("
		for item in collection["search5"].split(","):
			where +=" '"+item+"',"
		where +=" '6bb61e3b7bce0931da574d19d1d82c88')"
		where +=" ) "

	sql ="select "+str(collection['fields'])+" from "+str(collection['view_or_table'])+" "+where+" limit "+str(limit)+" offset "+str(start)
	print sql
	# 查询总数
	countSql='SELECT count('+str(collection["ID"])+') FROM '+str(collection['view_or_table'])+' '+where
	global conn
	if last_database_ip != collection['host']:
		if conn:
			conn.close()
		conn=MySQLdb.connect(collection['host'],collection['user'],collection['password'],collection['database'], charset='utf8')
		last_database_ip == collection["host"]
		   
	c=conn.cursor()
	c.execute(sql)
	data = c.fetchall()
	data = parseJSON(str(collection['fields']),data)
	# 添加位置
	data = getPosition(data,collection['service'],collection['ID'])
	# 添加3d_markup
	if(collection.has_key("has_3d_markup") and collection["has_3d_markup"]=='1'):
		template = getTemplate("service_3dmark_get")
		template["target_service_name"] = collection["service"]
		
		for item in data:
			ids=item[collection["ID"]]
			template["target_id"] = ids
			result = get3DMarkup(template)
			item["has_3d_markup"] = len(result['data']) 

	c.execute(countSql)


	count = c.fetchone()
	
	return {"page":page,"count":list(count)[0],"data":data,"success":True}
	