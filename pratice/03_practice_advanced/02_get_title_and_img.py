import urllib2
from BeautifulSoup import BeautifulSoup, SoupStrainer

url = 'http://pirates.netmarble.net/community/screenshot/bbsListView.asp'
soup = BeautifulSoup(urllib2.urlopen(url))
print 'Title :', soup.title.string
print 'img URLs :'
for i, link in enumerate(soup.findAll('link')):
    print '    %2d %s' % (i, link.get('href'))
