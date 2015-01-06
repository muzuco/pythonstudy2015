# -*- coding: utf-8 -*-
for i in range(2, 10):
    print '#' + str(i) + ' 단'
    for j in range(1, 10):
        print '%d x %d = %d' % (i, j, i * j)
    print
        
