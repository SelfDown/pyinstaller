#!/usr/bin/env python
# -*- coding: utf_8 -
from json_str_ws import strJSONWS
from position import getPosition
from parse_json import parseJSON
import json
import urllib2
def getData(collection):
	print collection
	access_data = collection["data"]
	headers={'Content-Type':'application/json'}
	#{userName: "admin", passWord: "123456"}
	access_url =  collection["url"]
	#access_data = urllib.urlencode(access_data)
	req = urllib2.Request(url=access_url,headers=headers,data=json.dumps(access_data))
	res_data = urllib2.urlopen(req)
	result = res_data.read()
	result = json.loads(result)
	return {"success":"true","data":result["data"]}