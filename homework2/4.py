from collections import defaultdict
d = defaultdict(list)

while True:
    try:
        n, m = map(int, input("Please enter n and m separated by space:").split())
        if n < 1 or n > 10000 or m < 1 or m > 100:
            raise ValueError
        break
    except ValueError:
        print("This values are incorrect, try again.")

for i in range(n):
    while True:
        try:
            a = (input())
            if len(a) > 100:
                raise ValueError
            break
        except ValueError:
            print("This word is too long")
    d['A'].append(a)
for j in range(m):
    while True:
        try:
            b = (input())
            if len(b) > 100:
                raise ValueError
            break
        except ValueError:
            print("This word is too long")
    d['B'].append(b)

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
