def _push(a,n):
    '''
    :param a: given array
    :param n: given size of array
    :return: stack
    '''
    stack = []
    if not a:
        return stack
    current_min = a[0]
    for i in a:
        if i < current_min:
            current_min = i

        stack.append([i,current_min])
    return stack


    # code here
    
def _getMinAtPop(stack):
    '''
    :param stack: our stack
    :return: none, print the elements in order of pop one by one, new line is not required
    '''
    while stack:
        temp = stack.pop()
        print(temp[1],end = " ")
    print()
    # code here

stack = _push([1,6,46,-1,2,0,5],7)
_getMinAtPop(stack)