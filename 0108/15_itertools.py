from itertools import groupby
lines = '''
this is the
first paragraph.

this is the second.
'''.splitlines()

print len(lines)

print '-------------'
for i,tmp in enumerate(lines):
    print 'line {num} : {str}'.format(num=i, str=tmp)
    
print '-------------' 

for has_chars, frags in groupby(lines, bool):
    if has_chars:
        print ' '.join(frags)