#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server
from rediscluster import StrictRedisCluster

import sys
'''
@Version:0.1Beta
@auther:zhaofangcheng
@e-mail:zhaofangcheng@126.com
依赖类库：
            async_timeout-3.0.0-py3-none-any.whl
            attrs-18.1.0-py2.py3-none-any.whl
            chardet-3.0.4-py2.py3-none-any.whl
            idna-2.6-py2.py3-none-any.whl
            idna-ssl-1.0.1.tar.gz
            pytz-2018.4-py2.py3-none-any.whl
            redis-2.10.6-py2.py3-none-any.whl
            redis_py_cluster-1.3.4-py2.py3-none-any.whl
redis助手，用来解决某些环境下redis集群只能连接上vpn才能查看的情况，可以将本程序部署在隔离区，通过隔离区连接到redis集群，用户访问隔离区就可以了
使用方法:模糊查询：http://xxxx:8000/like?eshop
         精准查询：http://xxxx:8000/query?eshop_floor, key必须存在，否则无法查到
         精准删除：http://xxxx:8000/del?eshop_floor, key必须存在，否则无法删除
'''
#处理模糊查询
def likeQuery(keyname,redisconn):
    returnstr = redisconn.keys(pattern='*' + keyname + '*')
    list = "<table cellSpacing='0' border='1px' width='1600px' align='center'>"
    list += "<tr bgcolor='lightgray'><td colspan=4 align='center'><h3>找到"+str(len(returnstr))+"条记录</h3></td></tr>"
    list += "<tr bgcolor='lightgray' align='center'><td >&nbsp;序号&nbsp;</td><td >*****key*****</td><td >*****value*****</td><td width=100px>**操作**</td></tr>"
    i=1
    for item in returnstr[:]:
        list += '<tr>'
        list +='<td width=20px align=center >'+str(i)+ '</td>'
        list +='<td width=20px>'+item.decode() + '</td>'
        list += '<td ><textarea style=width:900px;height:200px>'+redisconn.get(item.decode()).decode()+'</textarea></td>'
        list += '<td  align=center > <a href=query?' + item.decode() + '>查询</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href=del?' + item.decode() + '> 删除</a></td>'
        list += '</tr>'
        i=i+1
    list += "</table>"
    return list
#query del like 业务处理调度
def bizHandler(method,keyname,redisconn):
    try:
        if method == 'query':
            returnstr = redisconn.get(keyname)
            if (returnstr is None):
                ss = '找不到对应的key：'+keyname
                return ss;
            else:
                ss = returnstr
            return ss.decode("utf-8");
        elif method == "del":
            returnstr = redisconn.delete(keyname)
            return returnstr;
        elif method == "like":
            return likeQuery(keyname, redisconn);
    except Exception as ee:
        print("连接异常：", ee);
#redis集群操作
def redis_cluster(keyname,method):
    ip = '10.0.204.195'
    redis_nodes = [{'host': ip, 'port': 6379},
                   {'host': ip, 'port': 6380},
                   {'host': ip, 'port': 6381},
                   {'host': ip, 'port': 6382},
                   {'host': ip, 'port': 6383},
                   {'host': ip, 'port': 6384},
                   {'host': ip, 'port': 6385}
                   ]
    try:
        redisconn = StrictRedisCluster(startup_nodes=redis_nodes)
    except Exception:
        print("connection error")
        sys.exit(1)
    return bizHandler(method,keyname,redisconn)
#入口路由规则
def router(param,method):
    if (param == 'favicon.ico'):
        print("key有问题：", param);
    else:
        body = redis_cluster(param, method)
        if body:
            if method == "del":
                body = 'key已经删除，影响行数 %s' % (body or 'web')
            else:
                body = ' %s' % body
        else:
            body = '没这个key： %s' % (param or 'web')
            print('null piointer')
        return [body.encode('utf-8')]
#web应用配置器
def webServer_init(environ, start_response):
    try:
        start_response('200 OK', [('Content-Type','text/html; charset=utf-8')])
        param=environ['QUERY_STRING']
        #处理是删除还是查询方法
        method=environ['PATH_INFO'][1:]
        return router(param,method)
    except Exception as e:
        print("参数获取异常:",e)
#经验证只有8000端口可以访问
port =8000
httpd = make_server('', port, webServer_init)
print('redis助手启动成功:',port)
httpd.serve_forever()
