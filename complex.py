def add_complex(a,b):
	return [(a[0] + b[0]), (a[1] + b[1])]


#x and y are complex numbers (2 element arrays)
def mult_complex(a,b):
	return [(a[0] * b[0] - a[1] * b[1]), (a[0] * b[1] + b[0] * a[1])]


def sub_complex(a,b):
	return [(a[0] - b[0]), (a[1] - b[1])]

def dev_complex(a,b):
	pass


if (add_complex([1,1], [2,2]) != [3,3]):
	print "add_complex pooped itself"

if (add_complex([1,4], [2,5]) != [3,9]):
	print "add_complex pooped itself"

if (sub_complex([0,82], [42,42]) != [-42, 40]):
	print "sub_complex pooped itself"

if (sub_complex([9,9], [0,13]) != [9, -4]):
	print "sub_complex pooped itself"

if (mult_complex([3,5], [6,7]) != [-17, 51]):
	print "mult_complex pooped itself"

if (dev_complex([]))