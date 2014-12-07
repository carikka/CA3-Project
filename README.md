CA3-Project
===========
Put your code in here
------------------------------------------------------------------------------------------------------------------------------

import xml.etree.ElementTree as etree

def read_stations():
	"""
	Function to read the xml file and print the latitude and longitude
	"""
	xmlD = etree.parse("Stations.xml")
	root = xmlD.getroot()
	
	Stations = []
	lat_value = []
	long_value = []
	lat = []
	long = []
	line = []
	joke = []
	line_1 = []
	for item in root.findall('Station'):
		station = item.get('id')
		Stations.append(station)
	for item in root.findall('Station'):
		latitude = item.find('Latitude').text
		lat_value.append(latitude) # Here each Latitude value is appended into a list
	for item in lat_value:
		del lat_value[0] # Deletes the heading "Latitude" from the list
	for item in lat_value:
		c = float(item)
		lat.append(c) # Converts all the values into floats and appends into a list
	for item in root.findall('Station'):
		longitude = item.find('Longitude').text
		long_value.append(longitude)
	for item in long_value:
		del long_value[0]
	for item in long_value:
		d = float(item)
		long.append(d)
	for item in root.findall('Station'):
		lines = item.find('Line').text
		line.append(lines)
	return Stations, long, lat, line

#-----------------------------------------------------------------------------------------
read_stations()
