def reverse_stack(stack):
    if not stack:
        return stack
    temp = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, temp)

def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
        return
    temp = stack.pop()
    insert_at_bottom(stack, item)
    stack.append(temp)

# Example 
stack = [1, 2, 3, 4, 5]
reverse_stack(stack)
print(stack)  