import sys

try:
    total=sum(int(arg) for arg in sys.argv[1:])
    print 'sum =', total
except ValueError:
    print 'Please supply integer arguments' 

#print 'hello {name}'.format(name=sys.argv[1])