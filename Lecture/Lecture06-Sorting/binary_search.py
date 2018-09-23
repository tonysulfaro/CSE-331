"""Return True if target is found in indicated portion of a Python list.
  The search only considers the portion from data[low] to data[high] inclusive.
  """


def recBinarySearch(data, target, low, high):
  if low > high:
    return False
  else:
    mid = (low + high) // 2
    if target == data[mid]:
      return True
    elif target < data[mid]:
      return recBinarySearch(data, target, low, mid - 1)
    else:
      return recBinarySearch(data, target, mid + 1, high)




#sorted list
alist = [17, 20, 26, 31, 44, 54, 55, 77, 93]


#sorted list
#alist = [26,44,47]
#empty list
#alist=[]
low=0
high=len(alist)-1
#target =77
target=78
if recBinarySearch(alist,target,low,high):
  print("Target value found")
else:
  print("Target value not found")

