a=2
list=[9,2,3,5,6]
for my in  'list':
    if my=='s':
        continue
    print(my)


str="lovr"
print(( str * 3))
lists=[9,2,3,5,6]
# list.reverse()
# print(list)
# print(list(reversed(lists)))

from collections import Counter
list=[9,9,9,2,2,3,5,6]
my_counter=Counter(list)
print(my_counter.most_common())
