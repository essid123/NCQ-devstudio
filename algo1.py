
def solution(N,A):
  resultat= [0]*N # initialiser la liste 0 
  for i in range (len(A)) :
    if (A[i]>=1) and (A[i]<=N) : #  si la  condition de x soit >=1 et x <= n 
      resultat[A[i]-1]+=1 # compteur est incrementé de 1 
    elif (A[i]== N+1): # sinon si A[i]= N+1 
      maximum=max(resultat)
      resultat=[maximum]*N # tous les compteurs sont réglés sur la valeur maximale de n'importe quel compteur
  return(resultat)

"""---test---"""
#print(solution(5,[3,1,4,4,6,1,4,4]))
