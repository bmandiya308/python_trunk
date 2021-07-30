orders = {
	'cappuccino': 54,
	'latte': 56,
	'espresso': 72,
	'americano': 48,
	'cortado': 41
}

sort_orders = sorted(orders.items(), key=lambda x: x[1], reverse=True)

for i in sort_orders:
	print(i[0], i[1])


print("This is diff")

sort_orders1= sorted(orders.items(), key=lambda x: x[0], reverse=True)
for i in sort_orders1:
	print(i[0], i[1])



list_a = [12,34,11,7,26,11,30,29]

import functools

print(functools.reduce(lambda x,y : x if x < y else y,list_a))

list_b = list(range(11))

print(functools.reduce(lambda x,y : x + y,list_b))

print(sorted(list_a,reverse=0))

print(list(filter(lambda x: (x%2==0),list_a)))




print("#######################################################")

#repeatation count

dict_a  = [
	[1, 'google'],
	[2,'yahoo'],
	[3,'yahoo'],
	[4,'google'],
	[5,'yahoo'],
	[6,'khangaon']
]

sample = {}
ids = {}
for i in dict_a:
	if i[1]  in sample:
		sample[i[1]] += 1
		ids[i[1]].append(i[0])
	else:
		sample[i[1]] = 1
		ids[i[1]] = [i[0]]

for i in sorted(sample.items(),key=lambda x: x[1],reverse=True):
	print(i[0],i[1])
	print(ids[i[0]])






