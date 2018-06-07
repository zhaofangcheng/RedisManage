# RedisManage
python版本redis集群管理工具，使用WSGI协议不依赖其他外部服务，简洁快速。\<br>  
'''
>>@Version:0.1Beta\<br>  
>>@author:zhaofangcheng\<br>    
>>@e-mail:zhaofangcheng@126.com\<br>  
>>依赖类库：\<br>  
>>>>>async_timeout-3.0.0-py3-none-any.whl\<br>  
>>>>>attrs-18.1.0-py2.py3-none-any.whl\<br>  
>>>>>chardet-3.0.4-py2.py3-none-any.whl\<br>  
>>>>>idna-2.6-py2.py3-none-any.whl\<br>  
>>>>>idna-ssl-1.0.1.tar.gz\<br>  
>>>>>pytz-2018.4-py2.py3-none-any.whl\<br>  
>>>>>redis-2.10.6-py2.py3-none-any.whl\<br>  
>>>>>redis_py_cluster-1.3.4-py2.py3-none-any.whl\<br>  
redis助手，用来解决某些环境下redis集群只能连接上vpn才能查看的情况，可以将本程序部署在隔离区，通过隔离区连接到redis集群，用户访问隔离区就可以了\<br>  
使用方法:模糊查询：http://xxxx:8000/like?eshop\<br>  
         精准查询：http://xxxx:8000/query?eshop_floor, key必须存在，否则无法查到\<br>  
         精准删除：http://xxxx:8000/del?eshop_floor, key必须存在，否则无法删除\<br>  
'''\<br>  

人生苦短，python真快-java程序员感叹。\<br>  
![Alt text](https://github.com/zhaofangcheng/RedisManage/blob/master/redisManage.png)
