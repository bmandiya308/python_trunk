import json
dict_a = {'1':'bhaskar','2':'ketna kumar','3':'Sachin'}
print(type(dict_a))
print(dict_a)
json_d = json.dumps(dict_a)
print(type(json_d))
print(json_d)
dict_b = json.loads(json_d)
print(type(dict_b))
print(dict_b)
