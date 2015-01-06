REFRAIN = '''
%d bottles of bear on the wall,
%d bottles of bear,
take one down, pass it around,
%d bottles of bear on the wall!
'''
bottles_of_bear = 99
while  bottles_of_bear > 1:
    print REFRAIN % (bottles_of_bear, bottles_of_bear, bottles_of_bear - 1)
    bottles_of_bear -= 1
