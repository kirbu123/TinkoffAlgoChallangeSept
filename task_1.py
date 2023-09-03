border = list(map(int, input().split()))[1]
arr = list(map(int, input().split()))
ans = 0
for i in arr:
    if ans < i and i <= border:
        ans = i
print(ans)
