#!/usr/bin/env python
# -*- coding: utf_8 -
from json_str_ws import strJSONWS
from position import getPosition
from parse_json import parseJSON
from service_http_avatar_login import getData as login
from config import getTemplate
import json
import urllib2
# # 改成数据库
# def getTemplate(name):
# 	from config import config
# 	return config["collection"][name]
def getData(collection):
	print collection
	# todo: 改成数据库
	service_name = collection["login_Service"]
	templ = getTemplate(service_name)
	# 检查是否登录
	result = login(templ)
	visituser = templ["data"]['userName']
	if collection["visituser"]:
		visituser = collection["visituser"]
	access_url = collection["url"]+"?metaObjectName="+collection["metaObjectName"]
	headers={'Content-Type':'application/json',"authorization":result["data"],"systemcode":templ["data"]['userName'],"visituser":visituser}
	access_data = collection["data"]
	req = urllib2.Request(url=access_url,headers=headers,data=json.dumps(access_data))
	result = urllib2.urlopen(req)
	result = result.read()
	result = json.loads(result)
	if not result["data"]:
		return {"success":"false","data":"avatar数据请求失败","count":0}
	print result
	count = result["data"]["totalCount"]
	#中文对照
	if collection.has_key("dict_type") and collection["dict_type"] == "zh":
		arr = result["data"]["metaAttrNames"]
	else:#英文对照
		arr = result["data"]["mappingAttrNames"]
	result = parseJSON(','.join(arr),result["data"]["dataRows"])
	#print result
	# 如果是中文对照，ID 名称替换一下
	ID=collection["ID"]
	if collection.has_key("dict_type") and collection["dict_type"] == "zh" and collection["ID"] == 'DR_KEY':
		ID = "主键"
	else: 
		result = getPosition(result,collection['service'],ID)

	return {"success":"true","data":result,"count":count}
