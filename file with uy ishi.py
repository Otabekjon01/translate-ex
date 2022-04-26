import pickle
import string
# 1masala
# f=open("1masalaa.txt","r")
# m=f.read()


# file=open("1sonlar.txt","w")
# x=m.split()
# t=int(x[0])
# for i in range(t):
#     file.write(int(x[1])*"*")
#     file.write("\n")


# 2masala

# n=int(input("N butun sonni kiriting:"))
# file=open("1harflar.txt","w")
# i=0
# for i in range(n):
#
#    file.write(string.ascii_lowercase[:i])
#    file.write("\n")

# 3masala

# n=int(input("N butun sonni kiriting:"))
# file=open("2harflar.txt","w")
# i=0
# for i in range(n):
#     i+=1
#     file.write(string.ascii_uppercase[:i]+(n-i)*"*")
#     file.write("\n")

# 4masala

# f=open("piton.txt","r")
# m=f.read()
# t=len(m.split())
# k=m.split()

# l=0
# h=0
# for i in range(t):
#     q=(k[i]).split()
#     h=len(q[0])
#     l+=h

# print("fileda ",t," ta satr va ",l," ta belgi bor")

# 5masala
# f=open("piton.txt","a")

# t=" Kiimm Booooor"

# f.write(t)

# 6masala

# f=open("piton.txt","a")
# file=open("savdo.txt","r")
# k=file.read()
# f.write(k)

# 9masala
# l=int(input("k sonni kiriting:::"))
# f=open("piton.txt","r")
# k=f.read()
# print(k)
# f=open("piton.txt","w")
# t=k[:l]+" "+k[l:]

# f.write(t)

# 10masala

# l=int(input("k sonni kiriting:::"))
# f=open("piton.txt","r")
# k=f.read()
# print(k)
# f=open("piton.txt","w")
# t=k[:l+1]+" "+k[l+1:]

# f.write(t)

# 11masala

# f=open("piton.txt","r")
# k=f.read()
# t=k.replace(" ", "  ")

# print(t)

# 53 masala
# f=open("piton.txt", "r")
# k = f.read()
# file=open("savdo1.txt", "w")


# for i in range(len(k)):
#     if k[i] not in string.ascii_lowercase[0:] and k[i] not in "0123456789":
#         file.write(k[i])
    
    
### 54masala
# f=open("piton.txt", "r")
# k = f.read()
# file=open("savdo1.txt", "w")

# t=list()
# for i in range(len(k)):
#     if k[i] not in string.ascii_lowercase[0:] and k[i] not in "0123456789":
#         t+=list(k[i])
 
# file.write(str(set(t)))

#### 55masala
import pickle
a=[1,5,86,4,5,54,"salom"]
with open("wert","wb") as file:
    pickle.dump(a, file)
    
with open("wert","rb") as f:
    print(pickle.load(f))









    
            
