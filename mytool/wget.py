import requests as req
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

# def getShort(string):
#     text = req.head("http://t.cn/" + str(string))
#     head = text.headers
#     #print(head)
#     try:
#         if head['location'] == 'http://weibo.com/sorry':
#             return None
#         return head['location']
#     except:
#         return None
go   = lambda url : req.get(url).text
top = lambda string : (req.head("http://t.cn/" + str(string)).headers)['location']
#print(go('http://baidu.com'))