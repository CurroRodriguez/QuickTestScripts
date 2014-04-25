import urlparse


url = 'http://api.infraworks.com/resource'
furl = url + '?select=name;description&bbox=1,2,3,4&filter=name="foo"'
o = urlparse.urlparse(furl)
print o
q = urlparse.parse_qs(o.query)
print q

