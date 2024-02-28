class Fishes:
	def __init__(self):
		''' Constructor for this class. '''
		# Create some member animals
		self.members = ['Salmon', 'Satin', 'silk']
	def printMembers(self):
		print('Printing members of the Fishes class')
		for member in self.members:
			print('\t%s ' % member)