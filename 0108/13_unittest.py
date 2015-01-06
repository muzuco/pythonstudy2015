import unittest

def median(pool):
    print 
    print 'start!'
    copy = sorted(pool)
    print 'copy :', copy
    size = len(copy)
    print 'size :', size
    if size % 2 == 1:
        print 'if end!'
        return copy[(size - 1) / 2]
        print '?'
    else:
        print 'else end!'
        return (copy[(size / 2) - 1] + copy[size / 2]) / 2
    
class TestMedian(unittest.TestCase):
    def testMedian(self):
        print 'median result :' + str(median([2, 9, 9, 7, 9, 2, 4, 5, 8]))
        result1 = self.failUnlessEqual(median([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7)
        print 'class result 1 :' + str(result1)
        result2 = self.failIfEqual(median([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7)
        print 'class result 2 :' + str(result2)

if __name__ == '__main__':
    unittest.main()
