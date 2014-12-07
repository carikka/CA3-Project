import xml.etree.ElementTree as etree

def read_stations():
	"""
	Function to read the xml file Stations and return the Stations, latitude and longitude
	Carissa
	"""
	xmlD = etree.parse("Stations.xml")
	root = xmlD.getroot()
	
	Stations = []
	lat_value = []
	long_value = []
	latitude = []
	longitude = []
	line = []
	for item in root.findall('Station'):
		station = item.get('id')
		Stations.append(station)
	for item in root.findall('Station'):
		lat1 = item.find('Latitude').text
		lat_value.append(lat1) # Here each Latitude value is appended into a list
	for item in lat_value:
		del lat_value[0] # Deletes the heading "Latitude" from the list
	for item in lat_value:
		c = float(item)
		lat.append(c) # Converts all the values into floats and appends into a list
	for item in root.findall('Station'):
		long1 = item.find('Longitude').text
		long_value.append(long1)
	for item in long_value:
		del long_value[0]
	for item in long_value:
		d = float(item)
		longitude.append(d)
	for item in root.findall('Station'):
		lines = item.find('Line').text
		line.append(lines)
	return Stations, longitude, latitude, line

#-----------------------------------------------------------------------------------------
read_stations()
