# data = [120,135,128,142,119,400,125]
# if len(data) >= 3:
#     data.remove(max(data))
#     data.remove(min(data))
# avg = sum(data) / len(data)
# print(round(avg,1))

# def f(n):
#     if n<5:
#         return f(n+1) + f(n+2) + f(n+3)
    
#     else:
#         return n

# s = f(2)
# print(s)

# points = [(0,0) , (3,0) , (3,4) , (0,4)]
# x , y = 0 ,0
# for px , py in points:
#     x += px
#     y += py

# print(x , y)

# A = [0]
# for i in range(10):
#     Ai = 9 - i
# for i in range(4):
#     k = A[i]
#     A[i] = A[9 - i]
#     A[9 - i] = k



def vote(d1,d2,d3):
    if abs(d1-d2) <= 1:
        return(d1+d2)//2
    elif abs(d1-d3) <= 1:
        return(d1+d3)//2
    elif abs(d2-d3) <= 1:
        return(d2+d3)//2
    else:
        return d1

print(vote(100,101,105))