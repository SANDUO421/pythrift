# 项目介绍
1、服务端是Java，客户端是python 
2、服务端是springboot 中的springboot-netty-4
3、使用的python的2.7 插件同时thrift
### 需求
1、客户端接收服务端的信息，并给服务端发送信息
### 服务端是python ,客户端是Java 
#### 错误1 TTransportException: java.net.ConnectException: Connection refused: connect
* 原因：py服务器建socket的参数多了host
* 解决方案 (添加一个服务器的地址host就ok)
```python
serverSocket = TSocket.TServerSocket(host='127.0.0.1',port=9999)
```
