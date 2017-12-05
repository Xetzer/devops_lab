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

def listFiller(ran, keyv):
    for i in range(ran):
        while True:
            try:
                i = (input())
                if len(i) > 100:
                    raise ValueError
                break
            except ValueError:
                print("This word is too long")
        d[keyv].append(i)

listFiller(n, 'A')
listFiller(m, 'B')
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
