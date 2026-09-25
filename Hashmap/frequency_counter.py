# str = "Mississipi"
# map = {}
# for i in str:
#     if i in map:
#         map[i] = map[i]+1
#     else:
#         map[i] = 1
# #search in map and return the count
# print(map['s'])
# print (map)
































str = "mississippi"
freq_map = {}
for i in str:
    if i in freq_map:
        freq_map[i] = freq_map[i]+1
    else:
        freq_map[i] = 1
print(freq_map['m'])