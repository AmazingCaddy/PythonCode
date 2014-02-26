import itertools

city_list = [
	('Decatur', 'AL'),
	('Huntsville', 'AL'),
	('Selma', 'AL'),
	('Anchorage', 'AK'),
	('Nome', 'AK'),
	('Flagstaff', 'AZ'),
	('Phoenix', 'AZ'),
	('Tucson', 'AZ')
]


import functools

def log (message, subsystem):
	"Write the contents of 'message' to the specified subsystem."
	print '%s: %s' % (subsystem, message)

server_log = functools.partial(log, subsystem='server')
server_log('Unable to open socket')

def get_state ((city, state)):
	return state

for i in itertools.groupby(city_list, get_state):
	print i[1]