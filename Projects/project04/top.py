from Stack import Stack

def main():
	stack = Stack()
	assert stack.top() == None
	stack.push(1)
	assert stack.top() == 1
	stack.push(2)
	assert stack.top() == 2
main()