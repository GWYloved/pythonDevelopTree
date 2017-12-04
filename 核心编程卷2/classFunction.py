class FooClass(object):
	version = 0.1
	def __init__(self, nm='John Doe'):
		self.name = nm
		print 'Created a class instance for', nm

	def showname(self):
		print 'Your name is ',self.name

	def showver(self):
		print self.version

	def addMe2Me(self, x):
		return x+x

# foo1 = FooClass()

# foo1.showname()

# foo1.showver()

# foo1.addMe2Me('xsf')
