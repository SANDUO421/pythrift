# _*_ coding:utf-8 _*_


from com.python.thrift import PersonService
from com.python.thrift import ttypes

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
# 解决乱码问题
import sys

# 解决乱码问题
reload(sys)
sys.setdefaultencoding('utf8')

try:
    tSocket = TSocket.TSocket('localhost', 9999)
    tSocket.setTimeout(600)
    transport = TTransport.TFramedTransport(tSocket)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = PersonService.Client(protocol)
    transport.open()

    person = client.getPersonByUsername("张三")
    print person.username
    print person.age
    print person.married
    print '-----------------'
    newPerson = ttypes.Person()
    newPerson.username = "李四"
    newPerson.age = 18
    newPerson.married = True

    client.savePerson(newPerson)
    transport.close()

except Thrift.TException, tx:
    print '%s' % tx.message
