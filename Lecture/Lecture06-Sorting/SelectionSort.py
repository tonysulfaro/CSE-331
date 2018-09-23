
def select_sort(alist,n):

   if (n <=1):
       return
   posn =0
   max =alist[posn]
   i=1
   while(i < n ):
       if alist[i] > max :
           posn=i
           max = alist[posn]
       i +=1

   # temp=alist[n-1]
   # alist[n-1]=alist[posn]
   # alist[posn]=temp
   alist[n-1],alist[posn]=alist[posn],alist[n-1]
   select_sort(alist, n-1)



mylist=[100, 1, 2 ,10, 4, 78, 2,118  ]
n=len(mylist)

select_sort(mylist,n )
print(mylist)