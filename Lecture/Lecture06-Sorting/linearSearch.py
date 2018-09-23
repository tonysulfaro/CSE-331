def linearSearch3(a,key):
    for i in range(len(a)):
        if(a[i]== key):
            return i
    return None

def recLinearSearch(alist, l, r, key):
    if r<l:
        return -1
    if alist[l]==key:
        return l
    return recLinearSearch(alist,l+1,r,key)


# Recursive function to search x in arr[l..r]
def recSearch(arr, l, r, x):
    if r < l:
        return -1
    if arr[l] == x:
        return l
    return recSearch(arr, l + 1, r, x)




def linearSearch2(a,v):
    i=0
    while i < len(a) and v !=a[i]:
        i=i+1
    if i>= len(a):
        i=None
    else:
        return i


def linearSearch(a, value):
    position = 0
    found = False
    while position < len(a) and not found:
        if a[position] == value:
            found = True
        position += 1
    return found





 # def linearSearch(a, value):
 #    position = 0
 #    found = False
 #    while position < len(a) and #your code goes here
 #        #your code goes here
 #            #your code goes here
 #        #your code goes here
 #    #your code goes here
 #






#alist = [2, 4, 93, 17, 77, 31, 44, 55, 20]
alist = [2, 4, 93, 17]
if not(linearSearch2(alist,100)==None):
  print("Found it at index:  ", linearSearch2(alist,17))
else:
    print("Not found")
n=len(alist)

if linearSearch(alist,100):
    print("Found")
else:
    print("Not found")


print(recLinearSearch(alist,0,n-1,100))





blist = [54,26,93]

