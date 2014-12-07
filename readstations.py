import xml.etree.ElementTree as etree

def read_stations():
	"""
	Function to read the xml file Stations and return all the Stations and Corresponding Lines
	Carissa
	"""
	xmlD = etree.parse("Stations.xml")
	root = xmlD.getroot()
	
	Stations = []
	line = []

	for item in root.findall('Station'):
		station = item.get('id')
		Stations.append(station)
	for item in root.findall('Station'):
		lines = item.find('Line').text
		line.append(lines)
	return Stations, line

#-----------------------------------------------------------------------------------------
read_stations()
