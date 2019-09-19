# _*_ coding:utf-8 _*_

__author__ = '作者'

from com.python.thrift import ttypes

import sys

reload(sys)
sys.setdefaultencoding('utf8')


class PersonServiceImpl:
    def getPersonByUsername(self, username):
        print "get client username: " + username

        person = ttypes.Person()
        person.username = "王五"
        person.age = 19
        person.married = True
        return person

    def savePerson(self, person):
        print "get client username: "
        print person.username
        print person.age
        print person.married
