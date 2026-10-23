# data = [120,135,128,142,119,400,125]
# if len(data) >= 3:
#     data.remove(max(data))
#     data.remove(min(data))
# avg = sum(data) / len(data)
# print(round(avg,1))

def f(n):
    if n<5:
        return f(n+1) + f(n+2) + f(n+3)
    
    else:
        return n

s = f(2)
print(s)

