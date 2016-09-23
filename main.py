#list all the tags
#post the request
#get the url
#insert the database

#http://t.cn/hBoOmH
#http://t.cn/au02z5 get the request header
import requests as req
import re

def getShort(string):
    text = req.head("http://t.cn/" + str(string))
    head = text.headers
    #print(head)
    try:
        if head['location'] == 'http://weibo.com/sorry':
            return None
        return head['location']
    except:
        return None
if __name__ == '__main__':
    getShort('au02z5')
    getShort('aaaaaa')
