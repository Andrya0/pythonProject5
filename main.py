summ = 0
ans = set()
for i in range(1, 1000):
    if i / 3 not in ans:
        ans.add(i)

print(len(ans))
