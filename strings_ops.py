str_a = 'this is the Bhaskar Mandiya'
print(str_a)

print("Get string")
print(str_a[0]) #"t"
print(str_a[0:8]) #"this is "
print(str_a[0:16:1])  #"this is the Bhas"
print(str_a[0:16:2])  #"ti steBa"
print(str_a[::])  #"this is the Bhaskar Mandiya"
print(str_a[1::]) #"his is the Bhaskar Mandiy"
print(str_a[:7])  #"this is"
print(str_a[:7:1]) #"this is"
print(str_a[:7:-1]) #"ayidnaM raksahB eht"

print("Next Pattern")
str_b = "looking for code Word just refer 23556 and verify "
print("Original - ",str_b)
print(str_b.upper())
print(str_b.count('r'))
print(len(str_b))
print(len(str_b.strip()))
print(str_b.capitalize())
print(str_b.index('2')) #23 index number
print(str_b.casefold()) #looking for code word just refer 23556 and verify - all small
x = str_b.center(50) #print after 50 spaces
print(x)

print("Encoding started -  Default is UTF-8")
str_b = "looking for code Word just refer 23556 and verify / \ ?"
print(str_b.encode()) # default
print(str_b.encode(encoding="ascii",errors="backslashreplace")) #- uses a backslash instead of the character that could not be encoded
print(str_b.encode(encoding="ascii",errors="ignore")) #- uses a backslash instead of the character that could not be encoded
print(str_b.encode(encoding="ascii",errors="namereplace")) #- replaces the character with a text explaining the character
print(str_b.encode(encoding="ascii",errors="replace")) #- Default, raises an error on failure
print(str_b.encode(encoding="ascii",errors="xmlcharrefreplace")) #- replaces the character with a questionmark
print(str_b.encode(encoding="ascii",errors="strict")) # - replaces the character with an xml character

print("endswith check")
str_c = "Bhaskar\tMandiya\tKhangaon."
print(str_c)
print(str_c.expandtabs(20))
print(str_c.endswith('Khangaon')) #False
print(str_c.endswith('Khangaon.'))  #True
print(str_c.endswith('Bhaskar Mandiya Khangaon.'))  #False
print(str_c.endswith("Bhaskar\tMandiya\tKhangaon."))  #True

print('Find in str')
print(str_c.find('Mand')) #8

str_c = "{x} : Bhaskar {y} : Mandiya {z} : Pune Price : {price:.2f}"
print("format")
dict_c = {'x' : 'FirstName', 'y' : 'LastName', 'z' : 'City','price': 123.233}
print(str_c)
print(str_c.format(x='FirstName',y='LastName',z='City',price=34980.777865))
print(str_c.format_map(dict_c))

str_c = 'Bhaskar Mandiya 420'
print("number check in string")
print(str_c)
str_c = '76747646420'
print("isalnum - ",str_c)
print(str_c.isalnum())
str_c = 'bhaskar'
print("isalpha - ",str_c)
print(str_c.isalpha()) #only alfabets not bhaskar mandiya
str_c = 'Bhaskar Mandiya 420'
print("isascii - ",str_c)
print(str_c.isascii())
str_c = "3534856"
print("isdecimal - ",str_c)
print(str_c.isdecimal())
str_c = '3534856'
print("isdigit - ",str_c)
print(str_c.isdigit())
str_c = 'True'
print("isidentifier - ",str_c)
print(str_c.isidentifier())
str_c = 'bhaskar mandiya'
print("islower - ",str_c)
print(str_c.islower())
str_c = '35348'
print("isnumeric - ",str_c)
print(str_c.isnumeric())
str_c = '3534856.76454'
print("isprintable - ",str_c)
print(str_c.isprintable())
str_c = '    '
print("isspace - ",str_c)
print(str_c.isspace())
str_c = 'Bhaskar308'
print("istitle - ",str_c)
print(str_c.istitle())  #Should start with caps
str_c = 'BHASKAR MANDIYA'
print("isupper - ",str_c)
print(str_c.isupper())


print("split string")
str_c = "I am Bhaskarchandra Mandiya Chandravashi from Khangaon Yavatamal"
print(str_c)
print(str_b.split(' '))

print("rstrip and lstrip")
str_c = " Bhaskar Mandiya "
print(str_c," - ",len(str_c))
print(len(str_c.rstrip()))
print(len(str_c.lstrip()))
print("Replace string")
str_c = "I am Bhaskarchandra Mandiya Chandravashi from Khangaon Yavatamal"
print(str_c)
str_c.replace('Bhaskarchandra','Bhaskarrao')
print(str_c.replace('Bhaskarchandra','Bhaskarrao'))
print("string join")
print(str_c.join([' How - ',' can - ',' you - ',' say - ',' that - ']))

print("rsplit result")
txt = "apple, banana, cherry, any, body, banana, banana"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
print(txt)
x = txt.rsplit(", ", -1)
print(x)

#str_b.maketrans()
# example dictionary works with unicode number
dict = {"a": "123", "b": "456", "c": "789", "d": "801"}
string = "abc"
print(string.maketrans(dict))  #{97: '123', 98: '456', 99: '789'}

# example dictionary
dict = {97: "123", 98: "456", 99: "789"}
string = "xyz"
print(string.maketrans(dict)) #{97: '123', 98: '456', 99: '789'}

print("ljust and rjust to make fix width file and fill with provided -  100 len")
print(str_c.ljust(100,'1'))
print(len(str_c.ljust(100,'1')))
print(str_c.rjust(100,'1'))
print(len(str_c.rjust(100,'1')))

print("rfind give max index find if not found then -1")
str_b = "Learn Java from Javatpoint"
print(str_b)
print(str_b.rfind("Java"))  ## 16 Javatpoint start index if found then -1

print("last ocurance of string - rindex")
print(str_b.rindex("Java")) # 16 Javatpoint start index if not found then None

print("rpartition - fetch tuple with 3 itens before, match and after match")
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)

list_a = [1,2,3,4,5,76,87]
s = [str(i) for i in list_a]
print('-'.join(s))
print(int(''.join(s)))
