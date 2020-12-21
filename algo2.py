def solution(A,B):#donné deux tableaux A et B non vides
  fib = [0] * (max(A)+2)
  fib[1] = 1
  for i in range(2, max(A) + 2):
    fib[i] = fib[i - 1] + fib[i - 2]
  resultat = [0] * len(A)
  for pas in range(len(A)):
    resultat[pas] = fib[A[pas]+1] & ((1 << B[pas]) - 1) #nombre de manières différentes de monter sur l'échelle avec les échelons A [I] modulo 2B [I]*
  return(resultat)


"""test"""
print(solution([4,4,5,5,1],[3,2,4,3,1]))
