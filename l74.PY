def fibonacci(n):
    if n==0:
        return 0
        # print("here")
    elif n==1:
        return 1
        # print("here")
    else:
        # print("l1")
        result = fibonacci(n-1) + fibonacci(n-2)
        return result

print(fibonacci(4))
