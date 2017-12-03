from collections import defaultdict
d = defaultdict(list)
n, m = map(int, input("Please enter n and m separated by space:").split())

for i in range(n):
    d['A'].append(input())
for j in range(m):
    d['B'].append(input())
listA = list(d.get('A'))
listB = list(d.get('B'))

for k in range(m):
    st = []
    if listB[k] not in listA:
        print("-1")
    else:
        for l in range(n):
            if listA[l] == listB[k]:
                st.append(l+1)
        print(*st)
