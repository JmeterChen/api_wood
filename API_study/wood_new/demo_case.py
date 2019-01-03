# -*- ecoding=utf-8 -*-
# Author:Chen Bolin


class School(object):
	
	age = 100
	
	def __init__(self, name):
		self.name = name
		
		
class Hong(School):
	#
	# def __init__(self, name):
	# 	super(Hong, self).__init__(name)
	# 	self.name = name
	#
	@classmethod
	def print_name(cls):
		print(cls.age)

	def print_age(self):
		print(self.age)
	
a = Hong('haha')
a.print_age()