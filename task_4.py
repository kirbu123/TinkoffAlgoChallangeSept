n, m = list(map(int, input().split()))
nums = list(map(int, input().split()))
dp_reverse = [[[(0, 0, 0)] * 3 for i in range(m)] for j in range(n + 1)]
dp = [[[False] * 3 for i in range(m)] for j in range(n + 1)]
dp[0][0][0] = True
for i in range(n + 1):
    for j in range(m):
        for k in range(3):
            if j > 0:
                dp[i][j][k] = dp[i][j][k] or dp[i][j - 1][k]
                print(str([i, j - 1, k]) + ' -> ' + str([i, j, k]) + ' # 1')
            if i >= nums[j] and k > 0:
                dp[i][j][k] = dp[i][j][k] or dp[i - nums[j]][j][k - 1]
                print(str([i - nums[j], j, k - 1]) + ' -> ' + str([i, j, k]) + ' # 2')
ans = False
for i in range(m):
    if ans == True:
        break
    ans = dp[n][i][0] or dp[n][i][1] or dp[n][i][2]
for i in dp:
    for j in i:
        print(j, end=' ')
    print()
print(ans)