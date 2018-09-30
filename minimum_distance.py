def input_data():    
    n,max_diff=[int(x) for x in input().split()]
    A=[]
    for i in range(n):
        A.append(int(input()))
    return(n,max_diff,A)

def min_dist_100(n=None,max_diff=None,A=None):
    if (n==None)or(max_diff==None)or(A==None):
        n,max_diff,A=input_data()
    if max_diff>max(A)-min(A):
        distance="max_diff is too high."
    elif max(A)>100:
        distance="max(A) is too high."
    else:
        distance=float('inf')
        for i in range(max(A)+1):
            B=A.copy()
            for j,x in enumerate(B):
                if x==min(A):
                    B[j]=i
                if x>i+max_diff:
                    B[j]=i+max_diff
                if x<i:
                    B[j]=i
            c=sum(map(lambda x,y : (x-y)**2, A,B))
            if (c<distance) and (c>0):
                distance=c
            if c>distance:
                break
    return(distance)

def min_dist(n=None,max_diff=None,A=None):
    if (n==None)or(max_diff==None)or(A==None):
        n,max_diff,A=input_data()
    if max_diff>max(A)-min(A):
        distance="max_diff is too high."
    else:
        if max(A)<=100:
            distance=min_dist_100(n,max_diff,A)
        else:
            d=float('inf')
            for i in range(0,max(A)+1,100):
                B=A.copy()
                for j,x in enumerate(B):
                    if x==min(A):
                        B[j]=i
                    if x>i+max_diff:
                        B[j]=i+max_diff
                    if x<i:
                        B[j]=i
                c=sum(map(lambda x,y : (x-y)**2, A,B))
                if (c<d) and (c>0):
                    d=c
                    C=B.copy()
                if c>d:
                    break

            D=C.copy()
            for j,x in enumerate(C):
                if x==min(C):
                    D[j]=x-100
                if x==max(C):
                    D[j]=x+100
            distance=float('inf')
            for i in range(min(D),max(D)+1):
                B=D.copy()
                for j,x in enumerate(B):
                    if x==min(D):
                        B[j]=i
                    if x>i+max_diff:
                        B[j]=i+max_diff
                    if x<i:
                        B[j]=i
                c=sum(map(lambda x,y : (x-y)**2, A,B))
                if (c<distance) and (c>0):
                    distance=c
                if c>distance:
                    break
    return(distance)


if __name__ == "__main__":
    min_distance()
    min_distance100()
    
