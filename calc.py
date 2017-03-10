import operator

operators = {
'+' : operator.add,
'-' : operator.sub
}

def calculate(args):
	stack = list()
	for operand in args.split():
		try:
			operand = float(operand)
			stack.append(operand)
		except:
			arg1 = stack.pop()
			arg2 = stack.pop()
			stack.append(operators[operand](arg1, arg2))
	return stack.pop()


def main():
	while True:
		print("Result: " + str(calculate(input("rpn calc> "))))

if __name__ == '__main__':
	main()
