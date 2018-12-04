#!/usr/bin/env python
# -*- coding: utf_8 -
import time
import uuid
def getData(collection):
	print collection
	user_id = collection["user_id"]
	if not user_id:
		print "user_id is empty"
	settings = collection["settings"]
	key = collection['key']
	value = collection['value']
	if len(settings)==0:
		if not key :
			print "key is empty"
		if not value:
			print "value is not empty"
	settings[key] = value
	if collection["way"] == "sqlite":
		import sqlite3
		conn = sqlite3.connect('position.db')
		c = conn.cursor()
		for key in settings.keys():
			value = settings[key]
			sql = "select * from user_info_setting where user_id = '"+user_id+"' and key = '"+key+"'"
			c.execute(sql)
			setting = c.fetchone()
			if  setting:
				sql_update="update user_info_setting\n"\
							"set value = '"+value+"',update_time='"+str(time.time())+"'\n"\
							"where key = '"+key+"' and user_id = '"+user_id+"'"
				c.execute(sql_update)
			else:
				sql_insert ="insert into user_info_setting(ID,KEY,VALUE,USER_ID,UPDATE_TIME) values('"+str(uuid.uuid1())+"','"+str(key)+"','"+str(value)+"','"+str(user_id)+"','"+str(time.time())+"')"
				c.execute(sql_insert)
		conn.commit()
		c.close()
		return {"data":"add success","success":True}