def sort(S):
    for i in range(0,len(S)):
        minimumIndex=i
        for x in range(i+1,len(S)):
            if S[x]<S[minimumIndex]:
                minimumIndex=x
        S[i],S[minimumIndex] = S[minimumIndex],S[i]
        print(S)        
    

S=[3,3,6,3,6,2,3,8,9,5,45,5,6,7,754,3]
sort(S)
print(S)
    
# find minimumIndex and swap with current , move next and find minimumIndex and swap with current.