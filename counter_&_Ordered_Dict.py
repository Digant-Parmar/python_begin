from collections import OrderedDict
from collections import Counter

d=OrderedDict()
total = Counter()

for _ in range(int(input())):
    
    items=input()
    total[items]+=1
    d[items]=d.get(items,0)+int(0)


print(len(d.items()))
for key,value in total.items():
    print(value, end = " ")