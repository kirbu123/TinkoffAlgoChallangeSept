n = int(input())
orig = list(map(int, list(input())))
copy = list(map(int, list(input())))
l = 0
r = n - 1
while (l < n and orig[l] == copy[l]):
    l += 1
while (r >= 0 and orig[r] == copy[r]):
    r -= 1
if l > r:
    print('YES')
else:
    if sorted(orig[l:r + 1]) == copy[l:r + 1]:
        print('YES')
    else:
        print('NO')
        

