import redis
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


class Data(object):
	"""Data Middle class for Redis"""
	def __init__(self,domain="127.0.0.1",secret="",db=0,port=6379,hashName="urlCrack"):
		self.hashName = hashName
		self.redis = redis.Redis(host=domain,port=port, db=db,decode_responses=True)
	def set(self,key,value):
		status = self.redis.hset(self.hashName,key,value)
		return status
	def get(self,key):
		try:
			return self.redis.hget(self.hashName,key).decode('ascii')
		except:
			try:
				return self.redis.hget(self.hashName,key).decode('utf-8')
			except:
				return self.redis.hget(self.hashName,key)
	def test(self):
		#self.redis.set('aaa','123')
		self.set('aaa','213')
		print(self.get('aaa'))
		print(self.get('aa'))
		print(self.set('bbb','啊啊啊'))
		print(self.get('bbb'))
		print(self.redis.hgetall(self.hashName))
if __name__ == '__main__':
	a = Data()
	a.test()