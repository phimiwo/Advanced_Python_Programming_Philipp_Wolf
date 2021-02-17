class Birds:
	def __init__(self):
		''' Constructor for this class. '''
		# Create some member animals
		self.members = ['Eagle', 'Goose', 'Swan']

	def printMembers(self):
		print('Printing members of the dangerous Birds class')
		for member in self.members:
			print('\t%s ' % member)
