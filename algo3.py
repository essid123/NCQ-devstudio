def solution(A):

    M = 0
    for i in range(len(A)):
        A[i] = abs(A[i])
        M = max(A[i], M)
    S = sum(A)
    count = [0] * (M + 1)
    for i in range(len(A)):
        count[A[i]] += 1
    dp = [-1] * (S + 1)
    dp[0] = 0
    for j in range(1, M + 1):
        if count[j] > 0:
            for k in range(S):
                if dp[k] >= 0:
                    dp[k] = count[j]
                elif (k >= j and dp[k - j] > 0):
                    dp[k] = dp[k - j] - 1
    resultat = S
    for i in range(S // 2 + 1):
      if dp[i] >= 0:
        resultat = min(resultat, S - 2 * i)
    return resultat


"""test"""
print(solution([1,5,2,-2]))
