#encoding:utf-8
import copy

class Train(object):
	def __init__(self, arg):
		super(Train, self).__init__()
		self.__hashmap = arg

	def getProperties(self):
		return copy.deepcopy(self.__hashmap)

	def getPropertyByName(self, name):
		if self.__hashmap.has_key(name):
			return copy.deepcopy(self.__hashmap[name])
		return None

	def setPropertyByName(self, name, value):
		if self.__hashmap.has_key(name):
			self.__hashmap[name] = value
			return True
		return False
	
if __name__ == '__main__':
#	train = Train({'xx': 'yy'})
#	print train.getProperties()
	pass