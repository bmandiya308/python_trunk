# Using dicttoxml for converting Python
#  Dictionary to XML
from dicttoxml import dicttoxml

# Data to be parsed
data = {'a': 2,
        'b': {
            'c': 'as',
            'f': True},
        'd': 7,
        }

xml = dicttoxml(data)
print(xml)

# Pretty printing XML after parsing
# it from dictionary
from xml.dom.minidom import parseString
from dicttoxml import dicttoxml

# Data to be parsed
data = {'a': 2,
        'b': {
            'c': 'as',
            'f': True},
        'd': 7,
        }

xml = dicttoxml(data)
dom = parseString(xml)

print(dom.toprettyxml())

# Removing Type Attribute from parsed XML (int,str from above)
from xml.dom.minidom import parseString

# attr_type = False is used
# to remove type attributes
xml = dicttoxml(data, attr_type=False)

print(parseString(xml).toprettyxml())

# Converting Python Dictionary to
# XML and saving to a file
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString

# Variable name of Dictionary is data
xml = dicttoxml(data)

# Obtain decode string by decode()
# function
xml_decode = xml.decode()

xmlfile = open("xml_input.xml", "w")
xmlfile.write(xml_decode)
xmlfile.close()

from dicttoxml import dicttoxml
from xml.dom.minidom import parseString

# Defining custom names for lists
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString

# Dictonary to be converted
obj = {'mylist': [u'foo', u'bar', u'baz'],
       'mydict': {
           'foo': u'bar',
           'baz': 1},
       'ok': True}

# custom function for defining
# item names
my_item_func = lambda x: 'list_item'
xml = dicttoxml(obj, item_func=my_item_func)

# Pretty formating XML
xml_format = parseString(xml).toprettyxml()

print(xml_format)

# Using parent name in dictionary
# as tag name in xml

from dicttoxml import dicttoxml
from xml.dom.minidom import parseString

# Dictionary to be converted
data = {
    'month': ['Jan', 'Feb',
              'Mar', 'Apr',
              'May', 'Jun',
              'Jul', 'Aug',
              'Sep', 'Oct',
              'Nov', 'Dec']
}

# Here x is the parent, you can chose
# to do some prcessing or use a part
# of the parent name for tag name
my_item_func = lambda x: x + 's'
xml = dicttoxml(data, item_func=my_item_func)

print(parseString(xml).toprettyxml())