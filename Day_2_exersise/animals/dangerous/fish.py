class Fish:
	def __init__(self):
		''' Constructor for this class. '''
		# Create some member animals 
		self.members = ['Shark', 'Piranha', 'Electric Eel']

	def printMembers(self):
		print('Printing members of the dangerous Fish class')
		for member in self.members:
			print('\t%s ' % member)
