#Lodash for python
def unique(l):
	'''
	This function generate a list of unique values from l
	'''
	pass

def reverse(s):
	'''
	This function generates the reverse of s. s can be a string or a list. It returns the type given to it
	'''
	return s[::-1]

def intersection(a,b):
	'''
	This function returns the intersection of a and b - A list of common elements between a and b
	'''
	length_a = len(a)
	legth_b = len(b)
	c = []
	for x in a:
		for y in b:
			if x == y:
				c.append(x)
	return c
	
def generate(steps):
	pass

def parse_csv(csv_string):
	'''
	This function parses a CSV string as a list. The specification demands that the first row of data represents the column names
	'''
	pass

def frequency(needle, haystack):
	'''
	This function returns the number of times needle appears in haystack
	'''


def sort(l):
	'''
	This function returns a sorted version of l
	'''
	pass