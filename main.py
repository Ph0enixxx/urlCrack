#list all the tags
#post the request ok
#get the url ok
#insert the database

#http://t.cn/hBoOmH
#http://t.cn/au02z5 get the request header
import mytool.wget as wget
import mytool.Gen  as Gen
from concurrent.futures import ThreadPoolExecutor

class App(object):
    #线程池
    def __init__(self,start=1001,end=2000):
        self.start = start
        self.end   = end
        self.pool = ThreadPoolExecutor(1000)
        self.urlGen = Gen.gen(start=1000000,end=10000000)

    def _start(self,sid):
        #global conf
        print("Start thread..id:" + str(sid))
        print(wget.top(self.urlGen.__next__()))


    def run(self):
        for i in range(self.start,self.end):
            res = self.pool.submit(self._start,i)
            print(str(i)+ " " +str(res.result()))
        pass
    pass


if __name__ == '__main__':
    #getShort('au02z5')
    #getShort('aaaaaa')
    urlGen = Gen.gen()
    #while True:
     #   print(1)
    a =  App()
    a.run()
    #for i in range(1,100):
    #    print(wget.top(urlGen.__next__()))
    # for i in range(0,10):
    #     print(wget.top('a32Z' + str(i)))
