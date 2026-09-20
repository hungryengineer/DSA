str = "Mississipi"
map = {}
for i in str:
    if i in map:
        map[i] = map[i]+1
    else:
        map[i] = 1
#search in map and return the count
print(map['s'])
