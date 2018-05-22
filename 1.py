s=[]
n=int(input("Enter the element range:"))
for i in range(0,n):
    b=(int(input("Enter element:")))
    s.append(b)
print(s)
z=int(len(s)/2)
q=[]
for i in range(0,z):
  q.append(s[i])
print(q)
print (len(q))
r=[]
for i in range(z,n):
  r.append(s[i])
print(r)
print(len(r))
p=sum(r)/len(r)
f=sum(q)/len(q)
if(p==f):
    print("YES")
else:
    print("NO")
  
