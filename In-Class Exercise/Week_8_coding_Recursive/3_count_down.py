# def countdown(n):
#     for i in range(n, 0, -1):
#         print(i)

def countdown(n):
    if n == 0:
        return
    else:
        print(n)
        countdown(n-1)

countdown(5)
 