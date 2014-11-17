# x   x
#  x x
#   x
#  x x
# x   x


# using:
# 2 for loops
# some if statements
# only 2 "x" strings
# possibly else/if else



# for i in range(0,5):
#    for j in range(1,i+1):
#         print " ",
#    print "x"
# sprintf
# print "%3d" %(n,)

# def draw_x(size):
# 	for r in range(0,size):
# 		for c in range(0,size):
# 			if (c == (-r + size - 1) or c == r):
# 			    print "x",
# 			else:
# 				print " ",    
# 		print

# draw_x(5)

# for i in range(1,100):
#     if (i%15== 0):
#         print "fizzbuzz"
#     elif (i%3== 0):
#     	print "fizz"
#     elif (i%5== 0):
#     	print "buzz"
#     else:
#     	print str(i)

# print "%3s %3s" %("*","|"),
# for c in range(0,10):
# 	print "%3d" %(c),
# print

# print "%3s %3s" %("-","+"),
# for c in range(0,10):
# 	print "%3s" %("-"),
# print
# for r in range(0,10):
# 	print "%3d %3s" %(r,"|"),
# 	for c in range(0,10):
# 		print "%3d" %(c * r),
# 	print 

def multable (rows,columns):
	print "%3s %3s" %("*","|"),
	for c in range(0,columns):
		print "%3d" %(c),
	print

	print "%3s %3s" %("-","+"),
	for c in range(0,columns):
		print "%3s" %("-"),
	print
	for r in range(0,rows):
		print "%3d %3s" %(r,"|"),
		for c in range(0,columns):
			print "%3d" %(c * r),
		print 

multable(12,5)
