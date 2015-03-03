# coding=utf-8
"""
>>> import urllib
>>> u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
>>> data= u.read()
>>> with open('rt22.xml', 'wb') as f:
...     f.write(data)

...
>>> from xml.etree.ElementTree import parse
>>> doc = parse('rt22.xml')
>>> for bus in doc.findall('bus'):
...     d = bus.findtext('d')
...     lat = float(bus.findtext('lat'))
...
"""