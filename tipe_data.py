
a = 5
print(a, "is of type", type(a))
a = 2.0
print(a, "is of type", type(a))
a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))




x=[0]*10005;              #inisialisasi array 0 sebanyak 10005; x[0]=0
x[1]=1;                   #x[1]=1
 
for j in range(2,10001):
      x[j]=x[j-1]+x[j-2]  # Fibonacci
print(x[10000])

b = 0.1234567890123456789
print(b)


s = "Hello World!"
print(s)
s= "Try Python!"
print(s)

x = [5,10,15,20,25,30,35,40]
print(x[5])
print(x[-1])
print(x[3:5])
print(x[:5])
print(x[-3:])
print(x[1:7:2])


#tuple
t = (5,'program', 1+3j)
t = (5,'program', 1+3j)
t[1]
t[0:3]


# Set
a = {1,2,2,3,3,3}
a

#Dictionary
d = {1:'value','key':2}
print(type(d))

d = {1:'value','key':2}
print(type(d))
print("d[1] = ", d[1]);
print("d['key'] = ", d['key']);