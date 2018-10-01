from Stack import Stack

def main():
   stu_stack = Stack(8)
   print(stu_stack)
   for i in range(0, 8):
       stu_stack.push(i)
       print(stu_stack)

   stu = stu_stack.pop()
   print(stu_stack)
   print(stu == 7)
   print(stu_stack.data == [0, 1, 2, 3, 4, 5, 6, None])
   print(stu_stack.size == 7)
   print("Printing stack after pop operation(s) --> ", str(stu_stack) )

   for i in range(0, 7):
       stu_stack.pop()

   print(stu_stack.pop() == None)
   print("Printing stack after pop operation(s) --> ", str(stu_stack) )

main()