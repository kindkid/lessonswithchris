import math

def add_complex(a,b):
	return [(a[0] + b[0]), (a[1] + b[1])]


#x and y are complex numbers (2 element arrays)
def mult_complex(a,b):
	return [(a[0] * b[0] - a[1] * b[1]), (a[0] * b[1] + b[0] * a[1])]


def sub_complex(a,b):
	return [(a[0] - b[0]), (a[1] - b[1])]
 
def sqr_complex(a):
    return mult_complex(a,a)

def dist(a,b):
    return math.sqrt((b[1] - a[1]) * (b[1] - a[1])  + (b[0] - a[0]) * (b[0] - a[0]))

#returns how many iterations until transgretion
# or negative value if reached max iterations 

def mand(C, max_distance, max_iterations):
    pass

# Z = C
# Z = add_complex(sqr_complex(2), C)


if (add_complex([1,1], [2,2]) != [3,3]):
	print "add_complex Fail"

if (add_complex([1,4], [2,5]) != [3,9]):
	print "add_complex Fail"

if (sub_complex([0,82], [42,42]) != [-42, 40]):
	print "sub_complex Fail"

if (sub_complex([9,9], [0,13]) != [9, -4]):
	print "sub_complex Fail"

if (mult_complex([3,5], [6,7]) != [-17, 51]):
	print "Mult_complex Fail"

if (dist([-2,-3], [-4,4]) != math.sqrt(53)):
	print dist([-2,-3], [-4,4])
