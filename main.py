
n = int(input())
lst = sorted([list(map(int, input().split())) for i in range(n)], key=lambda x: max([x[1]]))
a = set(min([[i[1]] for i in lst]))
for i in lst[1:]:
    lst.remove(i) if i[0] <= sorted(list(a))[-1] else a.add(i[1])
print(len(a))
for x in sorted(a):
    print(x, end=' ')
