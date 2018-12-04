#!/usr/bin/env python
# -*- coding: utf_8 -
import time
import uuid
def getData(collection):
	print collection
	if not  (collection 
		or collection['target_service_name'] 
		or collection['target_id'] 
		or collection['stepLength'] 
		or collection['velocity']
		or collection['json_content'] 
		or collection['type']):
		print "error"
		return {"data":"add failed","success":False}
	print collection
	if(collection['way']=="sqlite"):
		import uuid
		import sqlite3
		import time
		conn=sqlite3.connect(str(collection['url']))  
		c=conn.cursor()
		sql_select = "select * from markup where target_service_name = '"+collection["target_service_name"]+"' and target_id = '"+collection["target_service_name"]+"' order by create_time desc limit 1"
		c.execute(sql_select)
		data = c.fetchone()
		st = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		if not data:
			sql="insert into "+collection['view_or_table']+"(ID,target_service_name,target_id,stepLength,velocity,type,resource_id,model_key,json_content,create_time,guid) values('"+str(uuid.uuid1())+"','"+collection['target_service_name']+"','"+collection['target_id']+"','"+collection['stepLength']+"','"+collection['velocity']+"','"+collection['type']+"','"+collection['resource_id']+"','"+collection['model_key']+"','"+collection['json_content']+"','"+st+"','"+collection['guid']+"')"
			print sql
		else:
			sql = "update markup set json_content = '"+collection["json_content"]+"' and guid = '"+collection["guid"]+"' where target_service_name = '"+collection["target_service_name"]+"' and target_id = '"+collection["target_id"]+"'"
		c.execute(sql)
		conn.commit()
		return {"data":"add success","success":True}

	return {"data":"add failed","success":False}