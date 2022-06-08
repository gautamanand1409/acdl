def quick(a,start,end):
    if(start<end):
        p=partiton(a,start,end)
        quick(a,start,p-1)
        quick(a,p+1,end)
        
def partiton(a,start,end):
    i=start-1
    pivot=a[end]
    
    for j in range(start,end):
        if(a[j]<=pivot):
            i=i+1
            a[i],a[j]=a[j],a[i]
        
    a[i+1],a[end]=a[end],a[i+1]
    return i+1
    
def printarr(a):
    for i in range(len(a)):
        print(a[i],end=' ')
        
    
if __name__ == '__main__':
    a=[45,32,85,8,14]
    
    quick(a,0,len(a)-1)
    printarr(a)
    
    