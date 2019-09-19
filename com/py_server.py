# _*_ coding:utf-8 _*_
__author__ = '作者'

from com.python.thrift import PersonService
from PersonServiceImpl import PersonServiceImpl

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from thrift.server import TServer

try:
    personServiceHandler = PersonServiceImpl()
    processor = PersonService.Processor(personServiceHandler)
    serverSocket = TSocket.TServerSocket(host='127.0.0.1',port=9999)
    transportFactory = TTransport.TFramedTransportFactory()
    protocolFactory = TCompactProtocol.TCompactProtocolFactory()

    server = TServer.TSimpleServer(processor, serverSocket, transportFactory, protocolFactory)
    print 'Thrift Server started !'
    server.serve()
except Thrift.TException, ex:
    print '%s' % ex.message
