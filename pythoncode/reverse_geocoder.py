import geocoder
import unicodecsv
import logging


lat = '33.909'
lon = '-118.333'
g = geocoder.google([lat,lon], method='reverse')
print(g[0])
address = ((str(g[0]).split(',')))
address = address[0][1:]
max_index = 0
for index in range(len(address)):
    if address[index].isdigit() == True:
        max_index = index
    else:
        break
if max_index != 0:
    max_index += 2
street_name = "".join(address[max_index:len(address)])
print(street_name)
