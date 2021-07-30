import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

y = re.search("^AB.*Spain$", txt)
str = " "

z = re.search("^$",str)
print(x)
print(y)
print(z)


txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)


import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
print(x)



txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)



txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
print(type(x))


txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)



txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)


txt = "Th8 ra10n i19 Sp100ain"
x = re.sub("\d", "CC", txt,2)
print(x)

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x) #this will print an object