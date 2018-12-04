#!/usr/bin/env python
# -*- coding: utf_8 -
def getData(collection):
	print collection
	if not (collection["target_service_name"] or collection['target_id']) :
		print "error"
		return {"data":"target_id or target_service_name  is null","success":False}

	if(collection['way']=="sqlite"):
		import uuid
		import sqlite3
		import time
		conn=sqlite3.connect(str(collection['url']))  
		c=conn.cursor()
		sql = "delete from markup where target_service_name = '"+collection['target_service_name']+"' and target_id = '"+collection["target_id"]+"'"
		c.execute(sql)
		conn.commit()
		return {"data":"delete success","success":True}

	return {"data":"delete failed","success":False}