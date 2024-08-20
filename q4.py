arr=[5,1,7,3,2]

def reverse(arr):
    stack =[]
    reversed_str=[]

    def push(test_string):
        for i in test_string:
            stack.append(i)

    def pop(stack):
        for i in range(len(stack)):
            reversed_str.append(stack[-1])
            stack.pop()
        print(reversed_str)

    push(arr)
    pop(stack)


reverse(arr)
