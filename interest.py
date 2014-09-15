# p = principal
# n = number of times interest is compounded per year
# r = rate of interest
# return the accrued amount
# t = time
# c = contributed amount per period

def accrued(p,r,n,c,t):
	return (p * (1 + (r/n)) ** (n * t)) + (c * ((1 + (r/n)) ** (n * t) - 1) * (n/r))


print accrued(6.25, 0.07, 12, 1000, (65 - 22))