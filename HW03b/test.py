def activity_selection(s, f, v):
    dp = {}
    n = len(s)
    last = None
    import pdb;pdb.set_trace()
    for i in sorted(list(set(s+f))):
        if last is None:
            dp[i] = 0
        else:
            dp[i] = last
            for j in range(n):
                if f[j] <= i:
                    dp[i] = max(dp[i], dp[s[j]] + v[j])
        last = dp[i]
    return last

# Driver code
s = [1, 2, 1, 2, 4]
f = [5, 3, 2, 3, 5]
v = [5, 3, 10, 3, 15]

last = activity_selection(s, f, v)
print("Sorted array:")
print(last)