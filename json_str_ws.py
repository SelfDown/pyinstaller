#!/usr/bin/env python
# -*- coding: utf_8 -
count=1
import json
import datetime
class CJsonEncoder(json.JSONEncoder):

	def default(self, obj):
		if isinstance(obj, datetime.datetime):
			return obj.strftime('%Y-%m-%d %H:%M:%S')
		elif isinstance(obj, date):
			return obj.strftime("%Y-%m-%d")
		else:
			return json.JSONEncoder.default(self, obj)
def strJSONWS(Action=None,Data=None,Message=None,Level=None,Time=None,attribute=None,datavalue=None,Tags=None):
	
	dataSend = {}
	if Action != None:
		global count
		dataSend['Sn']=count
		count = count+1
		dataSend['Action']=Action
	if Data != None:
		dataSend['Data']=Data
	if Tags != None:
		dataSend["Tags"]=Tags	
	if Level != None:
		dataSend['Level'] = Level
	if Message != None:
		dataSend['Message'] = Message
	if Time != None:
		dataSend['Time'] = Time
	if attribute != None:
		dataSend['attribute'] = attribute
	if datavalue != None:
		dataSend['datavalue'] = datavalue
	#str_json=json.dumps(dataSend,encoding='utf-8',ensure_ascii=False),type(json.dumps(dataSend,encoding='utf-8',ensure_ascii=False))
	str_json=json.dumps(dataSend,encoding="utf8",ensure_ascii=False,cls=CJsonEncoder)
	return str_json