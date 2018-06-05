# RedisManage
python版本redis集群管理工具，使用WSGI协议不依赖其他外部服务，简洁快速。
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

人生苦短，python真快-java程序员感叹。
![Alt text](https://github.com/zhaofangcheng/RedisManage/blob/master/redisManage.png)
