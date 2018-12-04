#!/usr/bin/env python
# -*- coding: utf_8 -
import sys
reload(sys) 
sys.setdefaultencoding('utf8')

import socketio
import eventlet
import eventlet.wsgi
from flask import Flask, render_template
from config import config
from json_str_ws import strJSONWS
from flask import request
from parse_json import parseJSON
import json
import copy


sio = socketio.Server()
app = Flask(__name__)
# config = readJSON()
array=[]
import sqlite3
conn = sqlite3.connect("database.db")


def delCollect(name,collection):
    data=[]

    module = __import__(name)
    data = module.getData(collection)                   
    return data

@app.route("/saveTemplte",methods = ['POST'])
def saveTemplte():
    
    global conn
    import time
    service = request.form["service"]
    collection_type = request.form["type"]
    template = request.form["template"]
    table_id = str(time.time())
    backup = request.form['backup']
    cursor = conn.cursor()
    cursor.execute("select * from collection_list where service='"+service+"' ")
    record = cursor.fetchone()
    if record != None:
        return  "{'success':false,'message':'service 已经存在'}"
    cursor.execute("insert into collection_list(id,type,service,template,backup) values(?,?,?,?,?)",(table_id,collection_type,service,template,backup))
    conn.commit()
    print service,collection_type,template
    return "{'success':true,'message':'添加成功'}"


@app.route("/updateTemplte",methods = ['POST'])
def updateTemplte():
    
    global conn
    import time
    service = request.form["service"]
    collection_type = request.form["type"]
    template = request.form["template"]
    table_id = str(time.time())
    backup = request.form['backup']
    cursor = conn.cursor()
    cursor.execute("select * from collection_list where service='"+service+"' ")
    record = cursor.fetchone()
    if record == None:
        return  "{'success':false,'message':'service 不存在'}"
    cursor.execute("delete from collection_list where service = '"+service+"'")
    cursor.execute("insert into collection_list(id,type,service,template,backup) values(?,?,?,?,?)",(table_id,collection_type,service,template,backup))
    conn.commit()
    print service,collection_type,template
    return "{'success':true,'message':'修改成功'}"

@app.route("/deleteTemplte",methods = ['POST'])
def deleteTemplte():
    
    global conn
    import time
    service = request.form["service"]
    cursor = conn.cursor()
    cursor.execute("delete from collection_list where service = '"+service+"'")
    conn.commit()
    return "{'success':true,'message':'删除成功'}"

@app.route("/getTemplte",methods = ['GET'])
def getTemplte():
    global conn

    collection_type = request.args.get("type")
    cursor = conn.cursor()
    cursor.execute("select id,service,type,template,backup from collection_list where type='"+collection_type+"' order by id desc")
    records = cursor.fetchall()
    data = parseJSON("id,service,type,template,backup",records)
    return json.dumps({'success':True,'data':data})


@app.route('/')
def index():
    """Serve the client-side application."""
    return render_template('test_client.html',ip=config['config']['ip'],port=config['config']['net_port'])

@app.route('/collection_list')
def collection_list():
    """Serve the client-side application."""
    return render_template('collection_list.html',ip=config['config']['ip'],port=config['config']['net_port'])

@sio.on('connect', namespace='/collection')
def connect(sid, environ):
   print sid+" connect success!"

@sio.on('message', namespace='/collection')
def message(sid, data):
    # try:
    result = json.loads(str(data))
    #前台传过来的
    V = result["Data"]["collect"]["V"]
    print V
    service = V['service']
    #查询数据库里的service
    cursor = conn.cursor()
    cursor.execute("select * from collection_list where service='"+service+"' ")
    record = cursor.fetchone()
    # 如果存在这填充不存在的内容
   
    if record:
        tmp = json.loads(list(record)[3])
        tmp = tmp["Data"]["collect"]["V"]
        for item in tmp.keys():
            # 如果不存在的key，由数据库记录填充
            if not V.has_key(item):
                V[item] = tmp[item]

    #转到 service
    if V.has_key("service_type"):
        service = V["service_type"] 
    
    if(not config['collection'].has_key(service)):
        print "service not exitst!"
        sio.emit('reply', room=sid,data ="service not exitst!",namespace="/collection")
     #修改参数
    collection = copy.copy(config['collection'][service])
    collection["service"]=service

    for key,value in V.items():
        if collection.has_key(key):
            collection[key] = value
    result = delCollect(service,collection)
    service = V["service"] 
    DataSend={"result":{service:result}}
    s = strJSONWS(Action="DataSend",Data=DataSend)
    sio.emit('reply', room=sid,data =s,namespace="/collection")
    # except Exception, e:
    #     sio.emit('reply', room=sid,data ="data error",namespace="/collection")
        

@sio.on('disconnect', namespace='/collection')
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    # wrap Flask application with engineio's middleware
    app = socketio.Middleware(sio, app)

    # deploy as an eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('', config['config']['port'])), app)