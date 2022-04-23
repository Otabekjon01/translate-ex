#Archa
# n=int(input())
# for i in range(n):
#     print((n-i)*" "+(2*i+1)*"*")
# for j in range(n):
#     print((n-1)*" "+3*"*")
#     if j==2:
#         break

#Archa2
n=int(input())
for i in range(n):
    print((n-i)*"*"+(2*i+1)*" "+(n-i)*"*")
for j in range(n):
    print((n-1)*"*"+3*" "+(n-1)*"*")
    if j==2:
        break
print((2*n+1)*"*")




















