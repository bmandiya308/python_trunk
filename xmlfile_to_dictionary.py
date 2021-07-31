# import module
import xmltodict

# open the file
fileptr = open("xml_1_input.xml", "r")

# read xml content from the file
xml_content = fileptr.read()
print("XML content is:")
print(xml_content)

# change xml format to ordered dict
my_ordered_dict = xmltodict.parse(xml_content)
print("Ordered Dictionary is:")
print(my_ordered_dict)
print("Year of plane is:")
print(my_ordered_dict['plane']['year'])

# Use contents of ordered dict to make python dictionary
my_plane = dict(my_ordered_dict['plane'])
print("Created dictionary data is:")
print(my_plane)
print("Year of plane is")
print(my_plane['year'])


##Dict to xml

# import module
import xmltodict

# define dictionary with all the attributes
mydict = {'root' : {'plane2': {'year': '1977', 'make': 'Cessna', 'model': 'Skyhawk', 'color': 'Light blue and white'},
          'plane1': {'year': '1977', 'make': 'Cessna', 'model': 'Skyhawk', 'color': 'Light blue and white'}
          }}
print("Original Dictionary of plane data is:")
print(mydict)


# create xml format
xml_format = xmltodict.unparse(mydict, pretty=True)
print("XML format data is:")
print(xml_format)

my_ordered_dict = xmltodict.parse(xml_content)
print("Ordered 2 Dictionary is:")
print(my_ordered_dict)

##How to convert XML to JSON
import json
print("XML content is:")
print(xml_format)

# change xml format to ordered dict
my_ordered_dict = xmltodict.parse(xml_format)
print("Ordered Dictionary is:")
print(my_ordered_dict)
json_data = json.dumps(my_ordered_dict)
print("JSON data is:")
print(json_data)
x = open("plane.json", "w")
x.write(json_data)
x.close()


#How to convert JSON data to XML

import json

# define dictionary with all the attributes
fileptr = open("plane.json", "r")
json_data = json.load(fileptr)
print("JSON data is:")
print(json_data)

# create xml format
xml_format = xmltodict.unparse(json_data, pretty=True)
print("XML format data is:")
print(xml_format)