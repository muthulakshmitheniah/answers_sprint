test_string = input("Enter the string you want to reverse: ")
print(test_string[::-1])


def reverse(input):
    stack =[]
    reversed_str=[]

    def push(test_string):
        for i in test_string:
            stack.append(i)

    def pop(stack):
        for i in range(len(stack)):
            reversed_str.append(stack[-1])
            stack.pop()
        

    push(input)
    pop(stack)
    str=""
    for i in range (len(reversed_str)):
        str+=reversed_str[i]
    print(str)
    
reverse(test_string)
