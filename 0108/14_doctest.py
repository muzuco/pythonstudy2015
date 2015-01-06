def median(pool):
    '''Statistical median to demonstrate doctest.
    >>> median([2,9,9,10,9,2,4,5,8])
    copy : [2, 2, 4, 5, 8, 9, 9, 9, 10]
    size : 9
    (size-1) / 2 = 4
    size % 2 = 1
    return : 4
    8
    '''
    copy = sorted(pool)
    print 'copy : ' + str(copy)
    size = len(copy)
    print 'size : ' + str(size)
    print '(size-1) / 2 = ' + str((size-1) / 2)
    print 'size % 2 = ' + str(size % 2)
    if size % 2 == 1:
        print 'return : ' + str((size - 1) / 2)
        return copy[(size - 1) / 2]
    else:
        print 'return : ' + str((copy[size / 2 - 1] + copy[size / 2]) / 2)
        return (copy[size / 2 - 1] + copy[size / 2]) / 2

if __name__ == '__main__':
    import doctest
    doctest.testmod()
